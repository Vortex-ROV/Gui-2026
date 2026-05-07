import pyzed.sl as sl
import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, QPixmap


class ZEDStreamThread(QThread):
    left_frame_ready = Signal(QPixmap)
    right_frame_ready = Signal(QPixmap)
    error_occurred = Signal(str)

    RECONNECT_DELAY_S    = 2.0   # seconds to wait between reconnection attempts
    GRAB_FAIL_TOLERANCE  = 5     # consecutive grab failures before reconnecting

    def __init__(self, ip_address='192.168.33.1:30000'):
        super().__init__()
        self.ip_address = ip_address
        self.running = False

    def run(self):
        self.running = True  # ← was missing: outer loop never ran without this

        while self.running:
            cam = sl.Camera()

            # ── open ──────────────────────────────────────────────────────
            init_parameters = sl.InitParameters()
            init_parameters.depth_mode = sl.DEPTH_MODE.NONE
            init_parameters.sdk_verbose = 1
            init_parameters.set_from_stream(
                self.ip_address.split(':')[0],
                int(self.ip_address.split(':')[1])
            )
            status = cam.open(init_parameters)
            if status != sl.ERROR_CODE.SUCCESS:
                self.error_occurred.emit(f"Camera Open failed: {repr(status)} — retrying in {self.RECONNECT_DELAY_S}s")
                self._sleep_interruptible(self.RECONNECT_DELAY_S)
                continue                             # retry the whole open sequence

            # ── stream ────────────────────────────────────────────────────
            runtime = sl.RuntimeParameters()
            mat_left = sl.Mat()
            mat_right = sl.Mat()
            consecutive_failures = 0

            while self.running:
                err = cam.grab(runtime)
                if err <= sl.ERROR_CODE.SUCCESS:
                    consecutive_failures = 0         # reset on success

                    cam.retrieve_image(mat_left, sl.VIEW.LEFT)
                    cam.retrieve_image(mat_right, sl.VIEW.RIGHT)

                    left_pixmap = self._mat_to_pixmap(mat_left)
                    right_pixmap = self._mat_to_pixmap(mat_right)

                    if left_pixmap:
                        self.left_frame_ready.emit(right_pixmap)
                    if right_pixmap:
                        self.right_frame_ready.emit(left_pixmap)
                else:
                    consecutive_failures += 1
                    self.error_occurred.emit(f"Capture error: {repr(err)} ({consecutive_failures}/{self.GRAB_FAIL_TOLERANCE})")

                    if consecutive_failures >= self.GRAB_FAIL_TOLERANCE:
                        self.error_occurred.emit("Too many grab failures — reconnecting…")
                        break                        # exit inner loop → reconnect

            cam.close()

            if self.running:                         # don't sleep if stop() was called
                self._sleep_interruptible(self.RECONNECT_DELAY_S)

    def _mat_to_pixmap(self, mat):
        try:
            img = mat.get_data()
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
            h, w, ch = img.shape
            qimg = QImage(img.data, w, h, ch * w, QImage.Format.Format_RGB888)
            return QPixmap.fromImage(qimg)
        except Exception:
            return None

    def _sleep_interruptible(self, seconds):
        """Sleep in small chunks so stop() is respected quickly."""
        chunk = 0.1
        elapsed = 0.0
        while self.running and elapsed < seconds:
            self.msleep(int(chunk * 1000))
            elapsed += chunk

    def stop(self):
        self.running = False
        self.wait()