from PySide6.QtCore import QThread, Signal
import socket
import threading
import time


class PCB(QThread):
    connection_changed    = Signal(bool)   # True = bottom connected, False = disconnected
    gripper_state_changed = Signal(dict)   # {"a": bool, "b": bool, "c": bool, "d": bool}
    rotating_tool_changed = Signal(bool)   # True = rotating, False = stopped

    BOTTOM_IP          = "192.168.33.1"
    BOTTOM_PORT        = 5000
    BIND_PORT          = 5002
    HB_INTERVAL        = 1
    HB_TIMEOUT         = 5
    RECONNECT_INTERVAL = 3

    def __init__(self):
        if __name__ != "__main__":
            super().__init__()

        self.__gripper_a    = False
        self.__gripper_b    = False
        self.__gripper_c    = False
        self.__gripper_d    = False
        self.__rotate_tool  = False
        self.armed          = False
        self.connected      = False

        self.__sock                 = None
        self.__stop_event           = threading.Event()
        self.__last_hb_from_bottom  = 0.0
        self.__reconnect_attempts   = 0

    # ── helpers ──────────────────────────────────────────────────────────────

    def __get_gripper_dict(self):
        return {
            "a": self.__gripper_a,
            "b": self.__gripper_b,
            "c": self.__gripper_c,
            "d": self.__gripper_d,
        }

    def __make_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("", self.BIND_PORT))
        sock.settimeout(1.0)
        return sock

    def __send_udp(self, message: str):
        if self.__sock is None:
            return
        try:
            self.__sock.sendto(message.encode(), (self.BOTTOM_IP, self.BOTTOM_PORT))
        except OSError as e:
            print(f"[WARN] Send failed: {e}")

    def __send_command(self, cmd: str, description: str):
        if not self.connected:
            print("[WARN] Bottom-side not connected — command not sent")
            return
        self.__send_udp(cmd + "\n")
        print(f"[CMD] Sent '{cmd}' → {description}")

    # ── gripper / tool controls ───────────────────────────────────────────────

    def control_gripper_a(self):
        self.__gripper_a = not self.__gripper_a
        cmd = "E" if self.__gripper_a else "e"
        self.__send_command(cmd, f"Gripper A {'OPEN' if self.__gripper_a else 'CLOSE'} (MOSFET 3)")
        self.gripper_state_changed.emit(self.__get_gripper_dict())
        print("Gripper A:", self.__gripper_a)

    def control_gripper_b(self):
        self.__gripper_b = not self.__gripper_b
        cmd = "G" if self.__gripper_b else "g"
        self.__send_command(cmd, f"Gripper B {'OPEN' if self.__gripper_b else 'CLOSE'} (MOSFET 2)")
        self.gripper_state_changed.emit(self.__get_gripper_dict())
        print("Gripper B:", self.__gripper_b)

    def control_gripper_c(self):
        self.__gripper_c = not self.__gripper_c
        cmd = "F" if self.__gripper_c else "f"
        self.__send_command(cmd, f"Gripper C {'OPEN' if self.__gripper_c else 'CLOSE'} (MOSFET 6)")
        self.gripper_state_changed.emit(self.__get_gripper_dict())
        print("Gripper C:", self.__gripper_c)

    def control_gripper_d(self):
        self.__gripper_d = not self.__gripper_d
        cmd = "D" if self.__gripper_d else "d"
        self.__send_command(cmd, f"Gripper D {'OPEN' if self.__gripper_d else 'CLOSE'} (MOSFET 4)")
        self.gripper_state_changed.emit(self.__get_gripper_dict())
        print("Gripper D:", self.__gripper_d)

    def control_rotating_tool(self):
        self.__rotate_tool = not self.__rotate_tool
        cmd = "C" if self.__rotate_tool else "c"
        self.__send_command(cmd, f"Rotating Tool {'ON' if self.__rotate_tool else 'OFF'} (MOSFET 5)")
        self.rotating_tool_changed.emit(self.__rotate_tool)
        print("Rotating Tool:", "rotating" if self.__rotate_tool else "not rotating")

    def send_state(self):
        pass  # UDP version sends immediately in each control_* method; stub kept for joystick compatibility

    def control_raise_camera(self):  pass
    def control_lower_camera(self):  pass
    def control_camera_stop(self):   pass

    # ── heartbeat threads ─────────────────────────────────────────────────────

    def __heartbeat_sender(self):
        last_reconnect_log = 0.0
        while not self.__stop_event.is_set():
            self.__send_udp("HB_TOP\n")
            if not self.connected:
                now = time.time()
                if now - last_reconnect_log >= self.RECONNECT_INTERVAL:
                    self.__reconnect_attempts += 1
                    print(f"[RECONNECT] Attempt #{self.__reconnect_attempts} — "
                          f"waiting for bottom-side at {self.BOTTOM_IP}:{self.BOTTOM_PORT} ...")
                    last_reconnect_log = now
            time.sleep(self.HB_INTERVAL)

    def __heartbeat_receiver(self):
        while not self.__stop_event.is_set():
            try:
                data, addr = self.__sock.recvfrom(1024)
                msg = data.decode().strip()

                if msg in ("HB_BOT", "PONG"):
                    self.__last_hb_from_bottom = time.time()

                    if not self.connected:
                        self.connected = True
                        self.__reconnect_attempts = 0
                        label = " (reconnected)" if msg == "PONG" else ""
                        print(f"[INFO] Bottom-side connected from {addr[0]}{label}")
                        self.connection_changed.emit(True)

            except socket.timeout:
                pass
            except Exception as e:
                print(f"[WARN] Receiver error: {e}")

            if self.connected and \
                    (time.time() - self.__last_hb_from_bottom) > self.HB_TIMEOUT:
                self.connected = False
                self.connection_changed.emit(False)
                print("[WARN] Bottom-side heartbeat lost — waiting to reconnect ...")

    # ── QThread run / stop ────────────────────────────────────────────────────

    def run(self):
        self.__stop_event.clear()
        self.__sock = self.__make_socket()

        print(f"[INFO] PCB thread started — "
              f"listening on :{self.BIND_PORT}, "
              f"target {self.BOTTOM_IP}:{self.BOTTOM_PORT}")

        sender_thread   = threading.Thread(target=self.__heartbeat_sender,
                                           daemon=True, name="pcb-hb-sender")
        receiver_thread = threading.Thread(target=self.__heartbeat_receiver,
                                           daemon=True, name="pcb-hb-receiver")
        sender_thread.start()
        receiver_thread.start()
        self.__stop_event.wait()
        sender_thread.join(timeout=2)
        receiver_thread.join(timeout=2)

    def stop(self):
        self.__stop_event.set()
        self.connected = False
        if self.__sock:
            try:
                self.__sock.close()
            except OSError:
                pass
            self.__sock = None
        self.exit()