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
    "forward":  "192.168.33.69",
    "grippers": "192.168.33.65",
    "downward": "192.168.33.68",
}

TARGET_SIZES = {
    "forward":  (945,  422),
    "grippers": (1896, 422),
    "downward": (945,  422),
}


# ── Backend selection ──────────────────────────────────────────────────────────
def _has_gstreamer() -> bool:
    info = cv2.getBuildInformation()
    for line in info.splitlines():
        if "GStreamer" in line and "YES" in line:
            return True
    return False

USE_GSTREAMER = _has_gstreamer()
print(f"[IPStream] Backend: {'GStreamer' if USE_GSTREAMER else 'FFMPEG'}")
# USE_GSTREAMER = False


# ── Pipeline / URL builders ────────────────────────────────────────────────────
def make_gstreamer_pipeline(ip: str) -> str:
    # Lowest-latency GStreamer pipeline:
    # - rtspsrc latency=0          : zero jitter buffer
    # - do-timestamp=true          : stable decoder timing even with UDP drops
    # - rtph264depay + h264parse   : explicit depay/parse avoids decodebin probing delay
    # - avdec_h264 max-threads=2   : direct decoder, no format negotiation
    # - queue leaky=downstream     : always drops old frames, never stalls
    # - appsink drop=true sync=false emit-signals=false : grab newest, never block
    # return (
    #     f"rtspsrc do-timestamp=true latency=0 "
    #     f"location=rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL} ! "
    #     f"rtph264depay ! "
    #     f"h264parse ! "
    #     f"avdec_h264 max-threads=2 ! "
    #     f"queue max-size-buffers=1 max-size-bytes=0 max-size-time=0 leaky=downstream ! "
    #     f"videoconvert ! "
    #     f"video/x-raw,format=BGR ! "
    #     f"appsink max-buffers=1 drop=true sync=false emit-signals=false"
    # )
    return "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@{}:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! appsink max-buffers=1 drop=true".format(ip)


def make_ffmpeg_url(ip: str) -> str:
    return f"rtsp://{USERNAME}:{PASSWORD}@{ip}:{PORT}/Streaming/Channels/{CHANNEL}"


def set_ffmpeg_options():
    # CAP_PROP_BUFFERSIZE is silently ignored by CAP_FFMPEG — these env options
    # are the real way to eliminate FFMPEG's internal buffering.
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = (
        "rtsp_transport;udp|"
        "fflags;nobuffer|"
        "flags;low_delay|"
        "framedrop;1|"
        "max_delay;0"
    )


# ── Frame → QPixmap ───────────────────────────────────────────────────────────
def frame_to_pixmap(frame: np.ndarray, target_w: int, target_h: int) -> QPixmap:
    # Resize first so the QImage step works on a smaller buffer
    if frame.shape[1] != target_w or frame.shape[0] != target_h:
        frame = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
    h, w, ch = frame.shape
    # Format_BGR888 skips the cv2.cvtColor(BGR->RGB) call and the .tobytes() copy
    qimg = QImage(frame.data, w, h, ch * w, QImage.Format.Format_BGR888)
    return QPixmap.fromImage(qimg)


# ── Single-camera capture (runs in its own daemon thread) ──────────────────────
class _CaptureWorker:
    # ── ADDED: how many seconds of no new frames before forcing a reconnect ──
    _HUNG_TIMEOUT = 8.0

    def __init__(self, name: str, ip: str):
        self.name     = name
        self.ip       = ip
        self._cap     = None
        self._frame   = None
        self._lock    = threading.Lock()
        self._running = False
        self._thread  = None
        self._new     = False  # True only when a fresh frame is available
        # ── ADDED: timestamp of the last successfully decoded frame ──────────
        self._last_frame_time = time.monotonic()

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop, daemon=True, name=f"cam-{self.name}"
        )
        self._thread.start()
        # ── ADDED: watchdog runs in its own thread — calls cap.release() from
        # outside to unblock a hung cap.read() in _loop. This is the only safe
        # way to interrupt a blocking read without touching the main thread. ──
        threading.Thread(
            target=self._watchdog, daemon=True, name=f"cam-{self.name}-wd"
        ).start()

    def read(self):
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
        # pipeline = make_gstreamer_pipeline(self.ip)
        # self._cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        # return True
        if self._cap:
            self._cap.release()
        # USE_GSTREAMER = False

        if USE_GSTREAMER:
            pipeline = make_gstreamer_pipeline(self.ip)
            self._cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        else:
            set_ffmpeg_options()
            self._cap = cv2.VideoCapture(make_ffmpeg_url(self.ip), cv2.CAP_FFMPEG)

        if self._cap.isOpened():
            print(f"[IPStream] {self.name} connected ({self.ip})")
            # ── ADDED: reset watchdog on every successful open ───────────────
            self._last_frame_time = time.monotonic()
            return True
        print(f"[IPStream] {self.name} failed to open, retrying…")
        return False
    
    def frame_to_pixmap(self, target_w: int, target_h: int) -> QPixmap:
        # Resize first so the QImage step works on a smaller buffer
        frame = self._frame
        # if frame.shape[1] != target_w or frame.shape[0] != target_h:
        #     frame = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
        h, w, ch = frame.shape
        # Format_BGR888 skips the cv2.cvtColor(BGR->RGB) call and the .tobytes() copy
        qimg = QImage(frame.data, w, h, ch * w, QImage.Format.Format_BGR888)
        return QPixmap.fromImage(qimg)

    def _watchdog(self):
        # ── ADDED: polls every second; if no frame has arrived in _HUNG_TIMEOUT
        # seconds, calls cap.release() which unblocks cap.read() in _loop,
        # causing it to return (False, None) and trigger the reconnect path. ──
        while self._running:
            time.sleep(1.0)
            if time.monotonic() - self._last_frame_time > self._HUNG_TIMEOUT:
                print(f"[IPStream] {self.name} hung — forcing reconnect…")
                cap = self._cap
                if cap:
                    cap.release()   # unblocks cap.read() in _loop
                self._last_frame_time = time.monotonic()  # reset to avoid re-triggering immediately

    def _loop(self):
        # self._open()
        while self._running:
            # time.sleep(1/30)
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

            # ── ADDED: update watchdog timestamp on every good frame ─────────
            with self._lock:
                self._frame = frame   # replace reference, old frame GC'd
                self._new   = True
                self._last_frame_time = time.monotonic()


# ── Qt thread that polls workers and emits QPixmap signals ────────────────────
class IPCameraStreamThread(QThread):
    """
    Automatically picks GStreamer (lowest latency) if available,
    falls back to FFMPEG with low-latency flags otherwise.

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

    POLL_INTERVAL_MS = int(1000/24)   # ~60 fps poll; workers gate output to actual camera FPS

    def __init__(self, parent=None):
        super().__init__(parent)
        self._workers: dict[str, _CaptureWorker] = {}
        self._timer: QTimer | None = None

    def run(self):
        for name, ip in CAMERA_IPS.items():
            worker = _CaptureWorker(name, ip)
            worker.start()
            self._workers[name] = worker
            # time.sleep(0.1)

        # self._timer = QTimer()
        # self._timer.setInterval(self.POLL_INTERVAL_MS)
        # self._timer.timeout.connect(self._emit_frames)
        # self._timer.start()

        # self.exec()

        # self._timer.stop()
        # for w in self._workers.values():
        #     w.stop()
        while True:
            time.sleep(1/30)
            # print("here")
            signal_map = {
                "forward":  self.forward_frame_ready,
                "grippers": self.grippers_frame_ready,
                "downward": self.downward_frame_ready,
            }
            for name, signal in signal_map.items():
                # print(signal_map.items())
                # time.sleep(1/30)
                is_new, frame = self._workers[name].read()
                if not is_new:
                    continue   # no new frame — skip pixmap work entirely
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
                signal.emit(self._workers[name].frame_to_pixmap(w, h))
            except Exception as exc:
                self.error_occurred.emit(f"[IPStream] {name} error: {exc}")
                import traceback
                traceback.print_exc()