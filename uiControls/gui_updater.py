"""
gui_updater.py
──────────────
Updates all status labels in the bottom bar and announces
arm/disarm + mode changes via VoiceAnnouncer.
"""

import platform
import pygame
from PySide6.QtCore import QTimer
from PySide6.QtGui  import QPixmap
from voice.voice_announcer import VoiceAnnouncer

_DEADZONE    = 0.15
_POLL_MS     = 50
_TIMER_MS    = 1000
_DEFAULT_SEC = 15 * 60


class GUIUpdater:

    def __init__(self, ui, joystick):
        self._ui       = ui
        self._joystick = joystick
        self._pixhawk  = joystick.pixhawk
        self._pcb      = joystick.pcb
        self._is_win   = platform.system() == "Windows"
        self._voice    = VoiceAnnouncer()

        # ── State tracking for announcements ──────────────────────────────
        self._last_mode  = ""
        self._last_armed = None

        self._pm = self._load_pixmaps()
        self._init_labels()

        # ── Poll timer ────────────────────────────────────────────────────
        self._poll_timer = QTimer()
        self._poll_timer.setInterval(_POLL_MS)
        self._poll_timer.timeout.connect(self._refresh)
        self._poll_timer.start()

        # ── Mission countdown ─────────────────────────────────────────────
        self._remaining     = _DEFAULT_SEC
        self._timer_running = False
        self._countdown     = QTimer()
        self._countdown.setInterval(_TIMER_MS)
        self._countdown.timeout.connect(self._tick)
        self._wire_timer_buttons()

    # ─────────────────────────────────────────────────────────────────────
    # Pixmap loader
    # ─────────────────────────────────────────────────────────────────────

    def _load_pixmaps(self) -> dict:
        paths = {
            "forward":        ":/Icons/iCONS/forward.png",
            "forward_on":     ":/Icons/iCONS/forwardgreen.png",
            "backward":       ":/Icons/iCONS/down.png",
            "backward_on":    ":/Icons/iCONS/downgreen.png",
            "left":           ":/Icons/iCONS/left.png",
            "left_on":        ":/Icons/iCONS/leftright.png",
            "right":          ":/Icons/iCONS/right.png",
            "right_on":       ":/Icons/iCONS/rightgreen.png",
            "up":             ":/Icons/iCONS/two-arrow (1).png",
            "up_on":          ":/Icons/iCONS/two-arrow (1) green.png",
            "down":           ":/Icons/iCONS/two-arrow down.png",
            "down_on":        ":/Icons/iCONS/two-arrow downgreen.png",
            "yaw_neutral":    ":/Icons/iCONS/neutralmode.png",
            "yaw_left":       ":/Icons/iCONS/anticlockwise.png",
            "yaw_right":      ":/Icons/iCONS/clockwise.png",
            "g1_open":        ":/Icons/iCONS/firstgripper.png",
            "g1_closed":      ":/Icons/iCONS/firstgripperclosed.png",
            "g2_open":        ":/Icons/iCONS/secondgripper.png",
            "g2_closed":      ":/Icons/iCONS/secondgripperclosed.png",
            "g3_open":        ":/Icons/iCONS/thirdgripper.png",
            "g3_closed":      ":/Icons/iCONS/thirdgripperclosed.png",
            "g4_open":        ":/Icons/iCONS/fourthgripper.png",
            "g4_closed":      ":/Icons/iCONS/fourthgripperclosed.png",
            "mode_manual":    ":/Icons/iCONS/manualmode.png",
            "mode_stabilize": ":/Icons/iCONS/stabilizemode.png",
            "mode_depth":     ":/Icons/iCONS/depthholdmode.png",
        }
        pm = {}
        for key, path in paths.items():
            pix = QPixmap(path)
            pm[key] = None if pix.isNull() else pix
        return pm

    # ─────────────────────────────────────────────────────────────────────
    # Init
    # ─────────────────────────────────────────────────────────────────────

    def _init_labels(self):
        for label, key in [
            (self._ui.forward,  "forward"),
            (self._ui.backward, "backward"),
            (self._ui.left,     "left"),
            (self._ui.right,    "right"),
            (self._ui.up,       "up"),
            (self._ui.down,     "down"),
            (self._ui.yawing,   "yaw_neutral"),
        ]:
            self._set(label, key)

        self._refresh_grippers()
        self._refresh_gain()
        self._refresh_mode()

    # ─────────────────────────────────────────────────────────────────────
    # Main refresh (called every _POLL_MS)
    # ─────────────────────────────────────────────────────────────────────

    def _refresh(self):
        self._refresh_axes()
        self._refresh_grippers()
        self._refresh_gain()
        self._refresh_mode()
        self._refresh_arm()

    # ─────────────────────────────────────────────────────────────────────
    # Axes
    # ─────────────────────────────────────────────────────────────────────

    def _axis(self, joy, index) -> float:
        try:
            v = joy.get_axis(index)
            return v if abs(v) > _DEADZONE else 0.0
        except Exception:
            return 0.0

    def _refresh_axes(self):
        if pygame.joystick.get_count() == 0:
            return
        try:
            joy = pygame.joystick.Joystick(0)
        except Exception:
            return

        DZ = _DEADZONE

        if self._is_win:
            left_v  = self._axis(joy, 1)
            left_h  = self._axis(joy, 0)
            right_v = self._axis(joy, 3)
            right_h = self._axis(joy, 2)
        else:
            left_v  = self._axis(joy, 1)
            left_h  = self._axis(joy, 0)
            right_v = self._axis(joy, 4)
            right_h = self._axis(joy, 3)

        self._set(self._ui.forward,  "forward_on"  if left_v  < -DZ else "forward")
        self._set(self._ui.backward, "backward_on" if left_v  >  DZ else "backward")
        self._set(self._ui.right,    "right_on"    if left_h  >  DZ else "right")
        self._set(self._ui.left,     "left_on"     if left_h  < -DZ else "left")
        self._set(self._ui.up,       "up_on"       if right_v < -DZ else "up")
        self._set(self._ui.down,     "down_on"     if right_v >  DZ else "down")

        if right_h > DZ:
            self._set(self._ui.yawing, "yaw_right")
        elif right_h < -DZ:
            self._set(self._ui.yawing, "yaw_left")
        else:
            self._set(self._ui.yawing, "yaw_neutral")

    # ─────────────────────────────────────────────────────────────────────
    # Grippers
    # ─────────────────────────────────────────────────────────────────────

    def _refresh_grippers(self):
        try:
            states = self._pcb.get_gripper_states()
        except AttributeError:
            states = {"a": False, "b": False, "c": False, "d": False}

        self._set(self._ui.firstgripper,
                  "g1_closed" if states["a"] else "g1_open")
        self._set(self._ui.secondgripper,
                  "g2_closed" if states["b"] else "g2_open")
        self._set(self._ui.thirdgripper,
                  "g3_closed" if states["c"] else "g3_open")
        self._set(self._ui.fourthgripper,
                  "g4_closed" if states["d"] else "g4_open")

    # ─────────────────────────────────────────────────────────────────────
    # Gain
    # ─────────────────────────────────────────────────────────────────────

    def _refresh_gain(self):
        self._ui.labelPercentage_2.setText(f"{self._pixhawk.get_gain()}%")

    # ─────────────────────────────────────────────────────────────────────
    # ROV mode  —  update label AND announce on change
    # ─────────────────────────────────────────────────────────────────────

    def _refresh_mode(self):
        mode = getattr(self._pixhawk, "mode", "")

        if mode == "STABILIZE":
            key = "mode_stabilize"
        elif mode == "ALT_HOLD":
            key = "mode_depth"
        else:
            key = "mode_manual"

        self._set(self._ui.rovmodes, key)

        # Announce only when the mode actually changes
        if mode and mode != self._last_mode:
            self._last_mode = mode
            if mode == "STABILIZE":
                self._voice.say("Stabilize mode activated.")
            elif mode == "ALT_HOLD":
                self._voice.say("Depth hold mode activated.")
            elif mode == "MANUAL":
                self._voice.say("Manual mode activated.")

    # ─────────────────────────────────────────────────────────────────────
    # Arm / Disarm  —  announce on change
    # ─────────────────────────────────────────────────────────────────────

    def _refresh_arm(self):
        # sent_armed is updated by pixhawk_class whenever the state changes
        armed = getattr(self._pixhawk, "sent_armed", None)

        # None means pixhawk not yet connected — skip
        if armed is None:
            return

        # Only announce when the value actually flips
        if armed == self._last_armed:
            return

        self._last_armed = armed

        if armed:
            self._voice.say("Armed.")
        else:
            self._voice.say("Disarmed.")

    # ─────────────────────────────────────────────────────────────────────
    # Timer
    # ─────────────────────────────────────────────────────────────────────

    def _wire_timer_buttons(self):
        self._ui.startButton_2.clicked.connect(self._start)
        self._ui.pauseButton.clicked.connect(self._pause)
        self._ui.restartButton.clicked.connect(self._restart)
        self._ui.pauseButton.setEnabled(False)
        self._show_time()

    def _start(self):
        if not self._timer_running and self._remaining > 0:
            self._timer_running = True
            self._countdown.start()
            self._ui.startButton_2.setEnabled(False)
            self._ui.pauseButton.setEnabled(True)

    def _pause(self):
        if self._timer_running:
            self._timer_running = False
            self._countdown.stop()
            self._ui.startButton_2.setEnabled(True)
            self._ui.pauseButton.setEnabled(False)

    def _restart(self):
        self._countdown.stop()
        self._timer_running = False
        self._remaining = _DEFAULT_SEC
        self._show_time()
        self._ui.startButton_2.setEnabled(True)
        self._ui.pauseButton.setEnabled(False)

    def _tick(self):
        if self._remaining > 0:
            self._remaining -= 1
            self._show_time()
        else:
            self._countdown.stop()
            self._timer_running = False
            self._ui.timerlabel.setText("00:00")
            self._ui.startButton_2.setEnabled(False)
            self._ui.pauseButton.setEnabled(False)

    def _show_time(self):
        m, s = divmod(self._remaining, 60)
        self._ui.timerlabel.setText(f"{m:02d}:{s:02d}")

    # ─────────────────────────────────────────────────────────────────────
    # Helper
    # ─────────────────────────────────────────────────────────────────────

    def _set(self, label, key: str):
        pix = self._pm.get(key)
        if pix is not None:
            label.setPixmap(pix)