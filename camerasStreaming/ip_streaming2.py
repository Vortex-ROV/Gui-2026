import cv2
import time
import threading
import numpy as np
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QImage, QPixmap


# ── Camera credentials ─────────────────────────────────────────────────────────
USERNAME = "admin"
PASSWORD = "VortexROV2025"
PORT     = 554
CHANNEL  = "101"

CAMERA_IPS = {
    "forward":  "192.168.33.66",
    "grippers": "192.168.33.69",
    "downward": "192.168.33.64",
}


def make_pipeline(ip: str) -> str:
    return (
        f"rtspsrc latency=0 "
        f"location=rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL} ! "
        f"queue max-size-buffers=1 max-size-bytes=0 max-size-time=0 leaky=downstream ! "
        f"decodebin ! "
        f"videoconvert ! "
        f"appsink max-buffers=1 drop=true sync=false"
    )


def bgr_to_pixmap(frame: np.ndarray) -> QPixmap:
    """Convert a BGR numpy frame to a QPixmap."""
    rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb.shape
    qimg  = QImage(rgb.data.tobytes(), w, h, ch * w, QImage.Format.Format_RGB888)
    return QPixmap.fromImage(qimg)


# ── Single-camera capture (runs in its own daemon thread) ──────────────────────
class _CaptureWorker:
    """Grab frames from one RTSP source in a background thread."""

    def __init__(self, name: str, ip: str):
        self.name     = name
        self.ip       = ip
        self.pipeline = make_pipeline(ip)
        self._cap     = None
        self._frame   = None
        self._lock    = threading.Lock()
        self._running = False
        self._thread  = None

    # ── public ────────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        self._thread  = threading.Thread(target=self._loop, daemon=True, name=f"cam-{self.name}")
        self._thread.start()

    def read(self) -> np.ndarray | None:
        with self._lock:
            return None if self._frame is None else self._frame.copy()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
        if self._cap:
            self._cap.release()

    # ── internal ──────────────────────────────────────────────────────────────

    def _open(self) -> bool:
        if self._cap:
            self._cap.release()
        self._cap = cv2.VideoCapture(self.pipeline, cv2.CAP_GSTREAMER)
        if self._cap.isOpened():
            print(f"[IPStream] {self.name} connected ({self.ip})")
            return True
        print(f"[IPStream] {self.name} failed to open, retrying…")
        return False

    def _loop(self):
        while self._running:
            if not self._cap or not self._cap.isOpened():
                if not self._open():
                    time.sleep(2.0)
                    continue

            ok, frame = self._cap.read()
            if not ok or frame is None:
                print(f"[IPStream] {self.name} lost — reconnecting…")
                self._cap.release()
                self._cap = None
                time.sleep(2.0)
                continue

            with self._lock:
                self._frame = frame


# ── Qt thread that polls workers and emits QPixmap signals ────────────────────
class IPCameraStreamThread(QThread):
    """
    Manages all three IP cameras and emits a QPixmap signal per camera
    at ~30 fps so you can connect them directly to QLabel.setPixmap.

    Signals
    -------
    forward_frame_ready  : QPixmap  – forward  camera (192.168.33.66)
    grippers_frame_ready : QPixmap  – grippers camera (192.168.33.69)
    downward_frame_ready : QPixmap  – downward camera (192.168.33.64)
    error_occurred       : str      – human-readable error message
    """

    forward_frame_ready  = Signal(QPixmap)
    grippers_frame_ready = Signal(QPixmap)
    downward_frame_ready = Signal(QPixmap)
    error_occurred       = Signal(str)

    # How many milliseconds between UI refreshes (≈30 fps)
    POLL_INTERVAL_MS = 33

    def __init__(self, parent=None):
        super().__init__(parent)
        self._workers: dict[str, _CaptureWorker] = {}
        self._timer: QTimer | None = None

    # ── lifecycle ─────────────────────────────────────────────────────────────

    def run(self):
        """Start capture workers then drive a QTimer on this thread's event loop."""
        for name, ip in CAMERA_IPS.items():
            worker = _CaptureWorker(name, ip)
            worker.start()
            self._workers[name] = worker

        # QTimer must be created inside run() so it lives on this thread
        self._timer = QTimer()
        self._timer.setInterval(self.POLL_INTERVAL_MS)
        self._timer.timeout.connect(self._emit_frames)
        self._timer.start()

        self.exec()          # Qt event loop — keeps thread alive

        # Cleanup after exec() returns
        self._timer.stop()
        for w in self._workers.values():
            w.stop()

    def stop(self):
        """Call this from the main thread to shut everything down."""
        self.quit()          # exits exec()
        self.wait()

    # ── frame dispatch ────────────────────────────────────────────────────────

    def _emit_frames(self):
        signal_map = {
            "forward":  self.forward_frame_ready,
            "grippers": self.grippers_frame_ready,
            "downward": self.downward_frame_ready,
        }
        for name, signal in signal_map.items():
            frame = self._workers[name].read()
            if frame is not None:
                try:
                    signal.emit(bgr_to_pixmap(frame))
                except Exception as exc:
                    self.error_occurred.emit(f"[IPStream] {name} pixmap error: {exc}")