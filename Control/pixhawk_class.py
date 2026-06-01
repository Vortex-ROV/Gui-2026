from PySide6.QtCore import QThread, Signal
from pymavlink import mavutil
import pymavlink.dialects.v10.ardupilotmega
import pymavlink.dialects.v20.ardupilotmega
import pymavlink.dialects.v10.all
import pymavlink.dialects.v20.all
import time


class PID:
    def __init__(self, kp=0.35, ki=0.0, kd=0.12, output_limit=400):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.output_limit = output_limit
        self.integral = 0
        self.last_error = 0
        self.last_time = None

    def compute(self, error):
        now = time.time()

        if self.last_time is None:
            self.last_time = now
            self.last_error = error
            return 0

        dt = now - self.last_time
        if dt <= 0:
            return 0

        self.integral += error * dt
        derivative = (error - self.last_error) / dt

        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )

        output = max(-self.output_limit, min(self.output_limit, output))

        self.last_error = error
        self.last_time = now

        return output

    def reset(self):
        self.integral = 0
        self.last_error = 0
        self.last_time = None


class Pixhawk(QThread):
    arm_state_changed  = Signal(bool)   # True = armed, False = disarmed
    mode_changed       = Signal(str)    # "MANUAL" | "STABILIZE" | "ALT_HOLD"
    connection_changed = Signal(bool)   # True = connected, False = disconnected
    gain_changed       = Signal(int)    # current gain 20–100

    def __init__(self):
        self.__running = False
        if __name__ != "__main__":
            super().__init__()
        self.__roll_value = 1500
        self.__throttle_value = 1500
        self.__yaw_value = 1500
        self.__forward_value = 1500
        self.__lateral_value = 1500
        self.__armed = False
        self.__last_time_seen = 0
        self.__connected = False
        self.__pwm_value_range = 400
        self.__gain = 100
        self.__rov_flip_value = 1
        self.sent_armed = False
        self.sent_mode = ""
        self.__rov_flip_lateral = 1
        self.__rov_flip_forward = 1

    def get_gain(self): return self.__gain

    def increase_gain(self):
        if self.__gain < 100:
            self.__gain += 20
            if self.__gain > 100: self.__gain = 100
            self.gain_changed.emit(self.__gain)
        else:
            print("gain is maximum")

    def decrease_gain(self):
        if self.__gain > 20:
            self.__gain -= 20
            if self.__gain < 20: self.__gain = 20
            self.gain_changed.emit(self.__gain)
        else:
            print("gain is minimum")

    def set_gain(self, value):
        if value > 100:   self.__gain = 100
        elif value < 20:  self.__gain = 20
        else:             self.__gain = value
        self.gain_changed.emit(self.__gain)

    def set_pwm_value_range(self, value):
        self.__pwm_value_range = int(value)
        if value > 400: self.__pwm_value_range = 400
        elif value < 0: self.__pwm_value_range = 0

    def get_pwm_value_range(self): return self.__pwm_value_range

    def set_roll_value(self, value):
        self.__roll_value += int(value * (self.__gain / 100))

    def set_throttle_value(self, value):
        self.__throttle_value += int(value * (self.__gain / 100))

    def set_yaw_value(self, value):
        self.__yaw_value += int(value * (self.__gain / 100))

    def set_forward_value(self, value):
        self.__forward_value += int(value * self.__rov_flip_forward * (self.__gain / 100))

    def set_lateral_value(self, value):
        self.__lateral_value += int(value * self.__rov_flip_lateral * (self.__gain / 100))

    def __check_and_correct_movement_values(self):
        limit = lambda v: max(
            1500 - int(self.__pwm_value_range * (self.__gain / 100)),
            min(1500 + int(self.__pwm_value_range * (self.__gain / 100)), v)
        )
        self.__roll_value     = limit(self.__roll_value)
        self.__throttle_value = limit(self.__throttle_value)
        self.__yaw_value      = limit(self.__yaw_value)
        self.__forward_value  = limit(self.__forward_value)
        self.__lateral_value  = limit(self.__lateral_value)

    def movements_values_reset(self):
        self.__roll_value = self.__throttle_value = self.__yaw_value = \
        self.__forward_value = self.__lateral_value = 1500

    def control_arm_disarm(self):
        if self.__connected:
            self.__pixhawk.arducopter_disarm() if self.__armed else self.__pixhawk.arducopter_arm()

    def control_arm(self):
        self.__pixhawk.arducopter_arm() if self.__armed == 0 else print("pixhawk already armed")

    def control_disarm(self):
        self.__pixhawk.arducopter_disarm() if self.__armed else print("pixhawk already disarmed")

    def control_manual_mode(self):
        mode_id = self.__pixhawk.mode_mapping()['MANUAL']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def control_stabilize_mode(self):
        mode_id = self.__pixhawk.mode_mapping()['STABILIZE']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def control_depth_hold_mode(self):
        mode_id = self.__pixhawk.mode_mapping()['ALT_HOLD']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def control_flip_rov_forward(self): self.__rov_flip_forward *= -1
    def control_flip_rov_lateral(self): self.__rov_flip_lateral *= -1

    def run(self):
        self.__running = True
        while self.__running:
            try:
                self.__pixhawk = mavutil.mavlink_connection(
                    "udp:192.168.33.2:14550", autoreconnect=True, source_system=1)
                print("Waiting to connect to the pixhawk...")
                self.__pixhawk.wait_heartbeat()
            except OSError:
                continue

            print("Got a heartbeat")
            self.__last_time_seen = time.time()

            while self.__running:
                msg = self.__pixhawk.recv_match()
                if msg:
                    if msg.get_type() == 'HEARTBEAT' and \
                            msg.type != mavutil.mavlink.MAV_TYPE_GCS:

                        if not self.__connected:
                            self.__connected = True
                            self.connection_changed.emit(True)
                            print("connected to pixhawk")

                        self.__armed = self.__pixhawk.motors_armed()
                        if self.__armed != self.sent_armed:
                            self.sent_armed = self.__armed
                            self.arm_state_changed.emit(bool(self.__armed))
                            print("armed" if self.__armed else "disarmed")

                        self.mode = mavutil.mode_string_v10(msg)
                        if self.mode == "Mode(0x00000000)":
                            self.mode = self.sent_mode
                        if self.mode != self.sent_mode:
                            self.sent_mode = self.mode
                            self.mode_changed.emit(self.mode)
                            print(self.mode)

                        self.__last_time_seen = time.time()

                if time.time() - self.__last_time_seen > 3:
                    if self.__connected:
                        self.__connected = False
                        self.sent_mode = ""
                        self.connection_changed.emit(False)
                        print("Disconnected, trying to reconnect to the pixhawk...")

    def move_rov(self):
        if self.__armed and self.__connected:
            self.__check_and_correct_movement_values()
            rc_channel_values = [
                1500, self.__roll_value, self.__throttle_value,
                self.__yaw_value, self.__forward_value, self.__lateral_value,
                65535, 65535, 65535
            ]
            self.__pixhawk.mav.rc_channels_override_send(
                self.__pixhawk.target_system,
                self.__pixhawk.target_component,
                *rc_channel_values)
            self.movements_values_reset()

    def track_transect(self, rect_center_x, rect_center_y, rect_angle, frame_width, frame_height):
        if not self.__armed or not self.__connected:
            return

        camera_center_x = frame_width / 2
        camera_center_y = frame_height / 2

        error_x = rect_center_x - camera_center_x
        error_y = rect_center_y - camera_center_y
        angle_error = rect_angle

        if abs(error_x) < self.center_deadzone:
            error_x = 0
        if abs(error_y) < self.center_deadzone:
            error_y = 0
        if abs(angle_error) < self.angle_deadzone:
            angle_error = 0

        lateral_correction = self.pid_lateral.compute(error_x)
        forward_correction = self.pid_forward.compute(error_y)
        yaw_correction     = self.pid_yaw.compute(angle_error)

        self.__lateral_value = self.__limit_pwm(1500 + lateral_correction)
        self.__forward_value = self.__limit_pwm(1500 + forward_correction)
        self.__yaw_value     = self.__limit_pwm(1500 + yaw_correction)
        self.__throttle_value = 1500

        print(
            "error_x:", int(error_x),
            "error_y:", int(error_y),
            "angle_error:", int(angle_error),
            "lateral_pwm:", self.__lateral_value,
            "forward_pwm:", self.__forward_value,
            "yaw_pwm:", self.__yaw_value
        )

        self.move_rov()

    def stop_transect_tracking(self):
        self.pid_lateral.reset()
        self.pid_forward.reset()
        self.pid_yaw.reset()

        self.__throttle_value = 1500
        self.__yaw_value      = 1500
        self.__forward_value  = 1500
        self.__lateral_value  = 1500

        self.move_rov()

    def stop(self):
        if self.__connected:
            self.__connected = False
            self.control_disarm()
            self.__pixhawk.close()
        self.__running = False