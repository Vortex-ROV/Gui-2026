
import cv2
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

class CameraThread(QThread):
    frame_ready = Signal(QImage)  # Signal to send frames to the main GUI

    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Cannot open video file")
            return

        while self.running:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            # Convert BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Emit frame to main thread
            self.frame_ready.emit(qt_image)

            self.msleep(30)  # ~30 FPS

        cap.release()

    def stop(self):
        self.running = False
        self.wait()