import cv2
import os
import time
import threading
import numpy as np
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QImage, QPixmap


USERNAME = "admin"
PASSWORD = "VortexROV2025"
PORT     = 554
CHANNEL  = "101"

CAMERA_IPS = {
    "forward":  "192.168.33.69",
    "grippers": "192.168.33.63",
    "downward": "192.168.33.64",
    "third":    "192.168.33.68",   # new camera
}

TARGET_SIZES = {
    "forward":  (945,  422),
    "grippers": (945,  422),
    "downward": (945,  422),
    "third":    (945,  422),       # new camera — same size, square-ish slot
}


def _has_gstreamer() -> bool:
    info = cv2.getBuildInformation()
    for line in info.splitlines():
        if "GStreamer" in line and "YES" in line:
            return True
    return False

USE_GSTREAMER = _has_gstreamer()
print(f"[IPStream] Backend: {'GStreamer' if USE_GSTREAMER else 'FFMPEG'}")


def make_gstreamer_pipeline(ip: str) -> str:
    return (
        "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@{}:554/Streaming/Channels/102 ! "
        "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! "
        "decodebin ! videoconvert ! appsink max-buffers=1 drop=true"
    ).format(ip)


def make_ffmpeg_url(ip: str) -> str:
    return f"rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL}"


def set_ffmpeg_options():
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = (
        "rtsp_transport;udp|"
        "fflags;nobuffer|"
        "flags;low_delay|"
        "framedrop;1|"
        "max_delay;0"
    )


def frame_to_pixmap(frame: np.ndarray, target_w: int, target_h: int) -> QPixmap:
    if frame.shape[1] != target_w or frame.shape[0] != target_h:
        frame = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
    h, w, ch = frame.shape
    qimg = QImage(frame.data, w, h, ch * w, QImage.Format.Format_BGR888)
    return QPixmap.fromImage(qimg)


class _CaptureWorker:
    _HUNG_TIMEOUT = 8.0

    def __init__(self, name: str, ip: str):
        self.name     = name
        self.ip       = ip
        self._cap     = None
        self._frame   = None
        self._lock    = threading.Lock()
        self._running = False
        self._thread  = None
        self._new     = False
        self._last_frame_time = time.monotonic()

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop, daemon=True, name=f"cam-{self.name}"
        )
        self._thread.start()
        threading.Thread(
            target=self._watchdog, daemon=True, name=f"cam-{self.name}-wd"
        ).start()

    def read(self):
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
        if USE_GSTREAMER:
            pipeline = make_gstreamer_pipeline(self.ip)
            self._cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        else:
            set_ffmpeg_options()
            self._cap = cv2.VideoCapture(make_ffmpeg_url(self.ip), cv2.CAP_FFMPEG)

        if self._cap.isOpened():
            print(f"[IPStream] {self.name} connected ({self.ip})")
            self._last_frame_time = time.monotonic()
            return True
        print(f"[IPStream] {self.name} failed to open, retrying…")
        return False

    def frame_to_pixmap(self, target_w: int, target_h: int) -> QPixmap:
        frame = self._frame
        h, w, ch = frame.shape
        qimg = QImage(frame.data, w, h, ch * w, QImage.Format.Format_BGR888)
        return QPixmap.fromImage(qimg)

    def _watchdog(self):
        while self._running:
            time.sleep(1.0)
            if time.monotonic() - self._last_frame_time > self._HUNG_TIMEOUT:
                print(f"[IPStream] {self.name} hung — forcing reconnect…")
                cap = self._cap
                if cap:
                    cap.release()
                self._last_frame_time = time.monotonic()

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
                self._new   = True
                self._last_frame_time = time.monotonic()


class IPCameraStreamThread(QThread):
    forward_frame_ready  = Signal(QPixmap)
    grippers_frame_ready = Signal(QPixmap)
    downward_frame_ready = Signal(QPixmap)
    third_frame_ready    = Signal(QPixmap)    # new signal
    error_occurred       = Signal(str)

    POLL_INTERVAL_MS = int(1000 / 24)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._workers: dict[str, _CaptureWorker] = {}

    def run(self):
        for name, ip in CAMERA_IPS.items():
            worker = _CaptureWorker(name, ip)
            worker.start()
            self._workers[name] = worker

        signal_map = {
            "forward":  self.forward_frame_ready,
            "grippers": self.grippers_frame_ready,
            "downward": self.downward_frame_ready,
            "third":    self.third_frame_ready,
        }

        while True:
            time.sleep(1 / 30)
            for name, signal in signal_map.items():
                is_new, frame = self._workers[name].read()
                if not is_new:
                    continue
                try:
                    w, h = TARGET_SIZES[name]
                    signal.emit(self._workers[name].frame_to_pixmap(w, h))
                except Exception as exc:
                    self.error_occurred.emit(f"[IPStream] {name} error: {exc}")
                    import traceback
                    traceback.print_exc()

    def stop(self):
        self.quit()
        self.wait()