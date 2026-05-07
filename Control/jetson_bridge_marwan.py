import socket
import serial
import time
import threading

# ================= CONFIG =================
HOST = "0.0.0.0"
PORT = 12345

SERIAL_PORT = "/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0"
BAUD_RATE = 115200

RECONNECT_DELAY = 2
HEARTBEAT_TIMEOUT = 3   # seconds (set None to disable)

# ==========================================

serial_lock = threading.Lock()
arduino = None
last_msg_time = time.time()


# 🔌 Connect / Reconnect Arduino
def connect_serial():
    global arduino

    while True:
        try:
            print("🔌 Connecting to Arduino...")
            arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)

            time.sleep(2)  # allow Arduino reset

            arduino.reset_input_buffer()
            arduino.reset_output_buffer()

            print("✅ Arduino connected")
            return

        except Exception as e:
            print(f"❌ Serial connection failed: {e}")
            time.sleep(RECONNECT_DELAY)


# 📤 Safe write
def write_to_arduino(data):
    global arduino

    try:
        with serial_lock:
            arduino.write(data.encode())

    except Exception as e:
        print(f"⚠️ Serial write failed: {e}")

        try:
            arduino.close()
        except:
            pass

        connect_serial()


# 👂 Read Arduino (debug / telemetry)
def read_from_arduino():
    global arduino

    while True:
        try:
            if arduino and arduino.in_waiting:
                line = arduino.readline().decode(errors="ignore").strip()
                if line:
                    print(f"[Arduino] {line}")

        except Exception as e:
            print(f"⚠️ Serial read failed: {e}")
            connect_serial()


# ❤️ Heartbeat / failsafe monitor
def heartbeat_monitor():
    global last_msg_time

    if HEARTBEAT_TIMEOUT is None:
        return

    while True:
        if time.time() - last_msg_time > HEARTBEAT_TIMEOUT:
            # ⚠️ FAILSAFE ACTION (customize this)
            print("💀 Heartbeat lost! Sending STOP")

            write_to_arduino('{"failsafe":1}\n')

            last_msg_time = time.time()

        time.sleep(1)


# 🌐 Handle client
def handle_client(conn, addr):
    global last_msg_time

    print(f"🌐 Client connected: {addr}")
    buffer = ""

    try:
        while True:
            data = conn.recv(1024).decode()

            if not data:
                break

            buffer += data

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()

                if line:
                    print(f"[RX] {line}")

                    last_msg_time = time.time()

                    write_to_arduino(line + "\n")

    except Exception as e:
        print(f"⚠️ Client error: {e}")

    finally:
        print(f"🔌 Client disconnected: {addr}")
        conn.close()


# 🚀 Main server
def main():
    connect_serial()

    # Threads
    threading.Thread(target=read_from_arduino, daemon=True).start()
    threading.Thread(target=heartbeat_monitor, daemon=True).start()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(5)

    print(f"🚀 Server listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True
            ).start()

    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")

    finally:
        server.close()
        if arduino:
            arduino.close()


if __name__ == "__main__":
    main()