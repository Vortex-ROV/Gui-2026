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
    "forward":  "192.168.33.63",
    "grippers": "192.168.33.65",
    "downward": "192.168.33.68",
}

TARGET_SIZES = {
    "forward":  (945,  422),
    "grippers": (1896, 422),
    "downward": (945,  422),
}


def make_url(ip: str) -> str:
    return f"rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL}"


def frame_to_pixmap(frame: np.ndarray, target_w: int, target_h: int) -> QPixmap:
    # Resize first so the BGR->QImage step works on a smaller buffer
    if frame.shape[1] != target_w or frame.shape[0] != target_h:
        frame = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
    h, w, ch = frame.shape
    # Format_BGR888 skips the cv2.cvtColor(BGR->RGB) call and the .tobytes() copy
    qimg = QImage(frame.data, w, h, ch * w, QImage.Format.Format_BGR888)
    return QPixmap.fromImage(qimg)


# ── Single-camera capture ──────────────────────────────────────────────────────
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
        self._new     = False  # True only when a fresh frame is available

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop, daemon=True, name=f"cam-{self.name}"
        )
        self._thread.start()

    def read(self) -> tuple[bool, np.ndarray | None]:
        """
        Returns (is_new, frame).
        is_new=False → frame unchanged since last call, skip rendering.
        No copy — caller must use the frame immediately (before next _loop iteration).
        """
        with self._lock:
            if not self._new or self._frame is None:
                return False, None
            self._new = False
            return True, self._frame

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
        if self._cap:
            self._cap.release()

    def _open(self) -> bool:
        if self._cap:
            self._cap.release()

        # FFMPEG low-latency flags:
        # - rtsp_transport=udp  : explicit UDP
        # - fflags=nobuffer     : disables FFMPEG's internal read buffer entirely
        # - flags=low_delay     : disables B-frame reordering delay in decoder
        # - framedrop=1         : drop frames to stay live rather than stalling
        # - max_delay=0         : zero mux/demux delay budget
        # Note: CAP_PROP_BUFFERSIZE is silently ignored by CAP_FFMPEG —
        # these env options are the actual way to control buffering.
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = (
            "rtsp_transport;udp|"
            "fflags;nobuffer|"
            "flags;low_delay|"
            "framedrop;1|"
            "max_delay;0"
        )
        self._cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)

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
                self._frame = frame   # replace reference, old frame GC'd
                self._new   = True


# ── Qt thread ─────────────────────────────────────────────────────────────────
class IPCameraStreamThread(QThread):
    """
    Signals
    -------
    forward_frame_ready  : QPixmap  945  x 422
    grippers_frame_ready : QPixmap  1896 x 422
    downward_frame_ready : QPixmap  945  x 422
    error_occurred       : str
    """

    forward_frame_ready  = Signal(QPixmap)
    grippers_frame_ready = Signal(QPixmap)
    downward_frame_ready = Signal(QPixmap)
    error_occurred       = Signal(str)

    POLL_INTERVAL_MS = 16   # ~60 fps poll; workers gate output to actual camera FPS

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
            is_new, frame = self._workers[name].read()
            if not is_new:
                continue   # no new frame — skip pixmap work entirely
            try:
                w, h = TARGET_SIZES[name]
                signal.emit(frame_to_pixmap(frame, w, h))
            except Exception as exc:
                self.error_occurred.emit(f"[IPStream] {name} error: {exc}")
                import traceback
                traceback.print_exc()