import cv2
import os
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
    "downward": "192.168.33.68",
}

# ── Target sizes matching the UI label dimensions ─────────────────────────────
TARGET_SIZES = {
    "forward":  (945,  422),
    "grippers": (1896, 422),
    "downward": (945,  422),
}


def make_url(ip: str) -> str:
    return f"rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL}?udp"


def frame_to_pixmap(frame: np.ndarray, target_w: int, target_h: int) -> QPixmap:
    if frame.shape[1] != target_w or frame.shape[0] != target_h:
        frame = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
    rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb.shape
    qimg = QImage(rgb.data.tobytes(), w, h, ch * w, QImage.Format.Format_RGB888)
    return QPixmap.fromImage(qimg)


# ── Single-camera capture (runs in its own daemon thread) ──────────────────────
class _CaptureWorker:
    def __init__(self, name: str, ip: str):
        self.name     = name
        self.ip       = ip
        self.url      = make_url(ip)
        self._cap     = None
        self._frame   = None
        self._lock    = threading.Lock()
        self._running = False
        self._thread  = None

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop, daemon=True, name=f"cam-{self.name}"
        )
        self._thread.start()

    def read(self):
        with self._lock:
            return None if self._frame is None else self._frame.copy()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
        if self._cap:
            self._cap.release()

    def _open(self) -> bool:
        if self._cap:
            self._cap.release()
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
        self._cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)
        self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self._cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 5000)
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
    Signals
    -------
    forward_frame_ready  : QPixmap  945  x 422  – forward  camera
    grippers_frame_ready : QPixmap  1896 x 422  – grippers camera
    downward_frame_ready : QPixmap  945  x 422  – downward camera
    error_occurred       : str
    """

    forward_frame_ready  = Signal(QPixmap)
    grippers_frame_ready = Signal(QPixmap)
    downward_frame_ready = Signal(QPixmap)
    error_occurred       = Signal(str)

    POLL_INTERVAL_MS = 33

    def __init__(self, parent=None):
        super().__init__(parent)
        self._workers = {}
        self._timer   = None

    def run(self):
        for name, ip in CAMERA_IPS.items():
            worker = _CaptureWorker(name, ip)
            worker.start()
            self._workers[name] = worker

        self._timer = QTimer()
        self._timer.setInterval(self.POLL_INTERVAL_MS)
        self._timer.timeout.connect(self._emit_frames)
        self._timer.start()

        self.exec()

        self._timer.stop()
        for w in self._workers.values():
            w.stop()

    def stop(self):
        self.quit()
        self.wait()

    def _emit_frames(self):
        signal_map = {
            "forward":  self.forward_frame_ready,
            "grippers": self.grippers_frame_ready,
            "downward": self.downward_frame_ready,
        }
        for name, signal in signal_map.items():
            try:
                frame = self._workers[name].read()
                if frame is not None:
                    w, h = TARGET_SIZES[name]
                    signal.emit(frame_to_pixmap(frame, w, h))
            except Exception as exc:
                self.error_occurred.emit(f"[IPStream] {name} error: {exc}")
                import traceback
                traceback.print_exc()