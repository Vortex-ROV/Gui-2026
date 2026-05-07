import pygame
import platform
from PySide6.QtCore import QThread
from Control.gui_mappings import *
from Control.pcb_class import PCB
from Control.pixhawk_class import Pixhawk

class Joystick(QThread):

    def __init__(self):
        if __name__ != "__main__": super().__init__()
        self.__running = False
        self.platform = platform.system()
        
        pygame.init()
        pygame.joystick.init()

        self.__controller_buttons_count = 0
        self.__controller_axes_count = 0
        self.__controller_buttons_data = []
        self.__controller_last_buttons_data = []
        self.__controller_raw_axes_data = []
        self.__controller_mapped_axes_data = []
        self.__controller_hat_data = [0, 0]
        self.__controller_last_hats_data = 0
        self.__controller_connected = False
        self.__controller_name = ""
        self.__controllers_count = 0
        self.__gain = 100

        self.pcb = PCB()
        self.pcb.start()
        self.pixhawk = Pixhawk()
        self.pixhawk.start()

        self.__rov_actions = {
            GUIControllerButtonActions.GRIPPER_A:       self.pcb.control_gripper_a,
            GUIControllerButtonActions.GRIPPER_B:       self.pcb.control_gripper_b,
            GUIControllerButtonActions.GRIPPER_C:       self.pcb.control_gripper_c,
            GUIControllerButtonActions.GRIPPER_D:       self.pcb.control_gripper_d,
            GUIControllerButtonActions.ROTATE_TOOL:     self.pcb.control_rotating_tool,
            GUIControllerButtonActions.SERVO_UP:        self.pcb.control_raise_camera,
            GUIControllerButtonActions.SERVO_DOWN:      self.pcb.control_lower_camera,
            GUIControllerButtonActions.SERVO_STOP:      self.pcb.control_camera_stop,
            GUIControllerButtonActions.GAIN_INCREASE:   self.pixhawk.increase_gain,
            GUIControllerButtonActions.GAIN_DECREASE:   self.pixhawk.decrease_gain,
            GUIControllerButtonActions.ARM_DISARM:      self.pixhawk.control_arm_disarm,
            GUIControllerButtonActions.MANUAL_MODE:     self.pixhawk.control_manual_mode,
            GUIControllerButtonActions.STABILIZE_MODE:  self.pixhawk.control_stabilize_mode,
            GUIControllerButtonActions.DEPTH_HOLD_MODE: self.pixhawk.control_depth_hold_mode,
            GUIControllerButtonActions.FLIP_ROV:        self.pixhawk.control_flip_rov,
            GUIControllerButtonActions.NONE:            "none"
        }

        self.__rov_movements = {
            GUIControllerMovementActions.THROTTLE: self.pixhawk.set_throttle_value,
            GUIControllerMovementActions.YAW:      self.pixhawk.set_yaw_value,
            GUIControllerMovementActions.FORWARD:  self.pixhawk.set_forward_value,
            GUIControllerMovementActions.LATERAL:  self.pixhawk.set_lateral_value,
            GUIControllerMovementActions.NONE:     ""
        }

        self.__button_action_mapping = {
            JoystickButtons.A.value:      self.__rov_actions[GUIControllerButtonActions.GRIPPER_A],
            JoystickButtons.B.value:      self.__rov_actions[GUIControllerButtonActions.GRIPPER_D],
            JoystickButtons.X.value:      self.__rov_actions[GUIControllerButtonActions.GRIPPER_B],
            JoystickButtons.Y.value:      self.__rov_actions[GUIControllerButtonActions.GRIPPER_C],
            JoystickButtons.LT.value:     self.__rov_actions[GUIControllerButtonActions.ROTATE_TOOL],
            JoystickButtons.RT.value:     self.__rov_actions[GUIControllerButtonActions.ARM_DISARM],
            JoystickButtons.BACK.value:   self.__rov_actions[GUIControllerButtonActions.STABILIZE_MODE],
            JoystickButtons.START.value:  self.__rov_actions[GUIControllerButtonActions.MANUAL_MODE],
            JoystickButtons.XBOX.value:   self.__rov_actions[GUIControllerButtonActions.NONE],
            JoystickButtons.LSTCIK.value: self.__rov_actions[GUIControllerButtonActions.NONE],
            JoystickButtons.RSTCIK.value: self.__rov_actions[GUIControllerButtonActions.FLIP_ROV],
            JoystickHats.HATUP:           self.__rov_actions[GUIControllerButtonActions.SERVO_UP],
            JoystickHats.HATDOWN:         self.__rov_actions[GUIControllerButtonActions.SERVO_DOWN],
            JoystickHats.HATRIGHT:        self.__rov_actions[GUIControllerButtonActions.GAIN_INCREASE],
            JoystickHats.HATLEFT:         self.__rov_actions[GUIControllerButtonActions.GAIN_DECREASE]
        }

        self.__button_name_mapping = {
            "A":      JoystickButtons.A.value,
            "B":      JoystickButtons.B.value,
            "X":      JoystickButtons.X.value,
            "Y":      JoystickButtons.Y.value,
            "LT":     JoystickButtons.LT.value,
            "RT":     JoystickButtons.RT.value,
            "BACK":   JoystickButtons.BACK.value,
            "START":  JoystickButtons.START.value,
            "XBOX":   JoystickButtons.XBOX.value,
            "LSTICK": JoystickButtons.LSTCIK.value,
            "RSTICK": JoystickButtons.RSTCIK.value
        }

        # PCB-related actions — only these trigger send_state()
        self.__pcb_actions = {
            self.pcb.control_gripper_a,
            self.pcb.control_gripper_b,
            self.pcb.control_gripper_c,
            self.pcb.control_gripper_d,
            self.pcb.control_rotating_tool,
            self.pcb.control_raise_camera,
            self.pcb.control_lower_camera,
            self.pcb.control_camera_stop,
        }

        # Reverse lookup: GUIControllerButtonActions → hat key or button index
        # Used by wrap_action to find where an action lives in the mapping.
        self.__action_to_key = {
            GUIControllerButtonActions.GRIPPER_A:       JoystickButtons.A.value,
            GUIControllerButtonActions.GRIPPER_D:       JoystickButtons.B.value,
            GUIControllerButtonActions.GRIPPER_B:       JoystickButtons.X.value,
            GUIControllerButtonActions.GRIPPER_C:       JoystickButtons.Y.value,
            GUIControllerButtonActions.ROTATE_TOOL:     JoystickButtons.LT.value,
            GUIControllerButtonActions.ARM_DISARM:      JoystickButtons.RT.value,
            GUIControllerButtonActions.STABILIZE_MODE:  JoystickButtons.BACK.value,
            GUIControllerButtonActions.MANUAL_MODE:     JoystickButtons.START.value,
            GUIControllerButtonActions.FLIP_ROV:        JoystickButtons.RSTCIK.value,
            GUIControllerButtonActions.GAIN_INCREASE:   JoystickHats.HATRIGHT,
            GUIControllerButtonActions.GAIN_DECREASE:   JoystickHats.HATLEFT,
            GUIControllerButtonActions.SERVO_UP:        JoystickHats.HATUP,
            GUIControllerButtonActions.SERVO_DOWN:      JoystickHats.HATDOWN,
        }

        self.__axis_action_mapping = {
            JoystickAxes.LEFTVERTICAL.value:    self.__rov_movements[GUIControllerMovementActions.FORWARD],
            JoystickAxes.LEFTHORIZONTAL.value:  self.__rov_movements[GUIControllerMovementActions.LATERAL],
            JoystickAxes.RIGHTVERTICAL.value:   self.__rov_movements[GUIControllerMovementActions.THROTTLE],
            JoystickAxes.RIGHTHORIZONTAL.value: self.__rov_movements[GUIControllerMovementActions.YAW]
        }

        print("initialized class")

    # ── Public API ────────────────────────────────────────────────────────────

    def get_name(self): return self.__controller_name

    def get_mapped_outputs(self): return self.__controller_mapped_axes_data

    def get_button_mapping(self, button: str):
        if button not in self.__button_name_mapping:
            print("Button not available")
            return
        return self.__button_action_mapping[self.__button_name_mapping[button]].__name__

    def set_button_mapping(self, button: str, mapping):
        """Replace the action for a named button with a new callable."""
        if button not in self.__button_name_mapping:
            print("Button not available")
            return
        self.__button_action_mapping[self.__button_name_mapping[button]] = mapping

    def wrap_action(self, action: GUIControllerButtonActions, extra_fn):
        """
        Keep the existing action for *action* AND also call *extra_fn* after it.
        Works for both button and hat mappings.
        """
        key = self.__action_to_key.get(action)
        if key is None:
            print(f"wrap_action: no key found for {action}")
            return
        original = self.__button_action_mapping.get(key)
        if original is None or original == "none" or original == "":
            print(f"wrap_action: no existing mapping for {action}, setting extra only")
            self.__button_action_mapping[key] = extra_fn
            return

        def _wrapped():
            original()
            extra_fn()

        self.__button_action_mapping[key] = _wrapped

    # ── Private helpers ───────────────────────────────────────────────────────

    def __map_value(self, value, from_low, from_high, to_low, to_high):
        return round(((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low), 2)

    def __press_event(self, method):
        method()
        # Only send PCB state for actions that actually involve the PCB,
        # and only when the PCB is connected — a socket error here would
        # crash the entire joystick thread.
        if method in self.__pcb_actions and self.pcb.connected:
            try:
                self.pcb.send_state()
            except OSError as e:
                print(f"[Joystick] send_state failed: {e}")

    def __release_event(self, method): method()

    def __axis_event(self, method, args): method(args)

    # ── Main loop ─────────────────────────────────────────────────────────────

    def run(self):
        self.__running = True
        while self.__running:
            pygame.event.pump()
            self.__controllers_count = pygame.joystick.get_count()
            if self.__controllers_count:
                self.__controller_connected = True
                self.__controller = pygame.joystick.Joystick(0)
                self.__controller.init()
                self.__controller_name = self.__controller.get_name()
                if "Xbox 360 Controller" not in self.__controller_name:
                    print("please plug in only a single xbox 360 controller.")
                    self.__controller.quit()
                    pygame.time.Clock.tick(10)
                    continue
                self.__controller_buttons_count = self.__controller.get_numbuttons()
                self.__controller_axes_count = self.__controller.get_numaxes()
                self.__controller_last_buttons_data.clear()
                self.__controller_last_buttons_data = [0] * self.__controller_buttons_count
                self.__controller_last_hats_data = [0, 0]
                self.__controller_mapped_axes_data = [0, 0, 0, 0, 0]
                print(self.__controller_name)

            while self.__controller_connected:
                pygame.event.pump()
                self.__controllers_count = pygame.joystick.get_count()
                if self.__controllers_count == 0:
                    self.__controller_connected = False
                    print("joystick disconnected")
                    break

                # Read buttons
                for i in range(self.__controller_buttons_count):
                    self.__controller_buttons_data.append(self.__controller.get_button(i))

                # Read axes (with deadzone)
                for i in range(self.__controller_axes_count):
                    raw = self.__controller.get_axis(i)
                    self.__controller_raw_axes_data.append(raw if abs(raw) > 0.1 else 0)

                # Read hat
                self.__controller_hat_data = self.__controller.get_hat(0)

                # ── Button press/release ──────────────────────────────────────
                for i in range(self.__controller_buttons_count):
                    if self.__controller_buttons_data[i] == 1 and self.__controller_last_buttons_data[i] == 0:
                        action = self.__button_action_mapping[i]
                        if action != "none":
                            self.__press_event(action)
                        else:
                            print("mapping is none")
                    # release branch intentionally left for future use

                # ── Hat press/release ─────────────────────────────────────────

                # Hat up
                if self.__controller_hat_data[1] == 1 and self.__controller_last_hats_data[1] == 0:
                    action = self.__button_action_mapping[JoystickHats.HATUP]
                    if action != "":
                        self.__press_event(action)
                elif self.__controller_hat_data[1] == 0 and self.__controller_last_hats_data[1] == 1:
                    self.__release_event(self.pcb.control_camera_stop)

                # Hat down
                if self.__controller_hat_data[1] == -1 and self.__controller_last_hats_data[1] == 0:
                    action = self.__button_action_mapping[JoystickHats.HATDOWN]
                    if action != "":
                        self.__press_event(action)
                elif self.__controller_hat_data[1] == 0 and self.__controller_last_hats_data[1] == -1:
                    self.__release_event(self.pcb.control_camera_stop)

                # Hat right
                if self.__controller_hat_data[0] == 1 and self.__controller_last_hats_data[0] == 0:
                    action = self.__button_action_mapping[JoystickHats.HATRIGHT]
                    if action != "":
                        self.__press_event(action)

                # Hat left
                if self.__controller_hat_data[0] == -1 and self.__controller_last_hats_data[0] == 0:
                    action = self.__button_action_mapping[JoystickHats.HATLEFT]
                    if action != "":
                        self.__press_event(action)

                # ── Axis remapping (OS-dependent) ─────────────────────────────
                if self.platform == "Linux":
                    self.__controller_raw_axes_data[2] = self.__map_value(self.__controller_raw_axes_data[2], -1, 1, 0, 1)
                    self.__controller_raw_axes_data[5] = self.__map_value(self.__controller_raw_axes_data[5], -1, 1, 0, 1)
                    self.__controller_mapped_axes_data[0] += int(-400 * self.__controller_raw_axes_data[1])
                    self.__controller_mapped_axes_data[1] += int( 400 * self.__controller_raw_axes_data[0])
                    self.__controller_mapped_axes_data[2] += int(-400 * self.__controller_raw_axes_data[4])
                    self.__controller_mapped_axes_data[3] += int( 400 * self.__controller_raw_axes_data[3])
                    self.__controller_mapped_axes_data[4] += int( 400 * self.__controller_raw_axes_data[5] + -400 * self.__controller_raw_axes_data[2])

                elif self.platform == "Windows":
                    self.__controller_raw_axes_data[4] = self.__map_value(self.__controller_raw_axes_data[4], -1, 1, 0, 1)
                    self.__controller_raw_axes_data[5] = self.__map_value(self.__controller_raw_axes_data[5], -1, 1, 0, 1)
                    self.__controller_mapped_axes_data[0] += int(-400 * self.__controller_raw_axes_data[1])
                    self.__controller_mapped_axes_data[1] += int( 400 * self.__controller_raw_axes_data[0])
                    self.__controller_mapped_axes_data[2] += int(-400 * self.__controller_raw_axes_data[3])
                    self.__controller_mapped_axes_data[3] += int( 400 * self.__controller_raw_axes_data[2])
                    self.__controller_mapped_axes_data[4] += int(-400 * self.__controller_raw_axes_data[4] + 400 * self.__controller_raw_axes_data[5])

                # ── Send movement values ──────────────────────────────────────
                for i in range(4):
                    action = self.__axis_action_mapping[i]
                    if action != "":
                        self.__axis_event(action, self.__controller_mapped_axes_data[i])

                self.pixhawk.move_rov()

                # ── Reset for next tick ───────────────────────────────────────
                self.__controller_last_buttons_data = self.__controller_buttons_data.copy()
                self.__controller_last_hats_data[0] = self.__controller_hat_data[0]
                self.__controller_last_hats_data[1] = self.__controller_hat_data[1]
                self.__controller_buttons_data.clear()
                self.__controller_raw_axes_data.clear()
                self.__controller_mapped_axes_data = [0, 0, 0, 0, 0]

                pygame.time.Clock().tick(200)

    def stop(self):
        if self.__controller_connected:
            self.__controller.quit()
            self.__controller_connected = False
        pygame.joystick.quit()
        pygame.quit()
        self.pixhawk.stop()
        self.pcb.stop()
        self.__running = False


if __name__ == "__main__":
    try:
        controller = Joystick()
        controller.run()
    except KeyboardInterrupt:
        print("quitting...")
        controller.stop()