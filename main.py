from logger import log
import os
import sys
# ── GStreamer environment fix for PyInstaller ──────────────────────────────
import traceback
import ctypes

if getattr(sys, 'frozen', False):
    base = sys._MEIPASS
    gst_plugin_path = os.path.join(base, 'gstreamer-1.0')
    os.environ['GST_PLUGIN_PATH'] = gst_plugin_path
    os.environ['GST_PLUGIN_SYSTEM_PATH'] = gst_plugin_path
    os.environ['PATH'] = base + os.pathsep + os.environ.get('PATH', '')

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Titans.ROV.Control.2026")

import traceback
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSizePolicy, QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QIcon
from ui import Ui_MainWindow
from uiControls.window_controls import WindowControls
from camerasStreaming.streaming_receiver import ZEDStreamThread
from camerasStreaming.ip_streaming import IPCameraStreamThread
from Control.joystick_class import Joystick
from Control.gui_mappings import GUIControllerButtonActions
from voice.voice_announcer import VoiceAnnouncer
from uiControls.camera_scroller import CameraScroller
from uiControls.gui_updater import GUIUpdater


class MainWindow(QMainWindow, WindowControls):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Icons/iCONS/titnaslogo.png"))
        self.setup_window_controls(self.ui)

        self.voice = VoiceAnnouncer()
        self.voice.welcome()

        self.scroller = CameraScroller(self.ui.middlewidget)

        self._inject_layouts()

        self.scroller = CameraScroller(self.ui.middlewidget)

        self.joystick = Joystick()

        self.joystick.wrap_action(
            GUIControllerButtonActions.GAIN_INCREASE,
            lambda: self.voice.say_gain(self.joystick.pixhawk.get_gain())
        )
        self.joystick.wrap_action(
            GUIControllerButtonActions.GAIN_DECREASE,
            lambda: self.voice.say_gain(self.joystick.pixhawk.get_gain())
        )

        self.joystick.set_button_mapping("XBOX",   self.scroller.scroll_forward)
        self.joystick.set_button_mapping("LSTICK", self.scroller.scroll_backward)

        self.joystick.start()

        self.gui_updater = GUIUpdater(self.ui, self.joystick)

        # ── ZED stream ────────────────────────────────────────────────────────
        self.zed_thread = ZEDStreamThread('192.168.33.1:30000')
        self.zed_thread.left_frame_ready.connect(self.ui.zedleftlabel.setPixmap)
        self.zed_thread.left_frame_ready.connect(self.ui.leftzed.setPixmap)
        self.zed_thread.error_occurred.connect(lambda msg: print(msg))
        self.zed_thread.start()

        # ── IP streams ────────────────────────────────────────────────────────
        self.ip_thread = IPCameraStreamThread()

        # Forward → rear labels + threeipcameras top-left
        self.ip_thread.forward_frame_ready.connect(self.ui.rightrear.setPixmap)
        self.ip_thread.forward_frame_ready.connect(self.ui.rightrearcamera.setPixmap)
        self.ip_thread.forward_frame_ready.connect(self.ui.leftone.setPixmap)

        # Grippers → left rear + threeipcameras top-right
        self.ip_thread.grippers_frame_ready.connect(self.ui.leftrear.setPixmap)
        self.ip_thread.grippers_frame_ready.connect(self.ui.leftrearcamera.setPixmap)
        self.ip_thread.grippers_frame_ready.connect(self.ui.rightone.setPixmap)

        # Downward → down labels + threeipcameras bottom (square)
        self.ip_thread.downward_frame_ready.connect(self.ui.downcameralabel.setPixmap)
        self.ip_thread.downward_frame_ready.connect(self.ui.downcameralabel_2.setPixmap)
        self.ip_thread.downward_frame_ready.connect(self.ui.downcamera_2.setPixmap)

        # Third (.68) → threeipcameras bottom label (downcamera_4)
        self.ip_thread.third_frame_ready.connect(self.ui.downcamera_4.setPixmap)

        self.ip_thread.error_occurred.connect(lambda msg: print(msg))
        self.ip_thread.start()

    def _inject_layouts(self):
        expand = QSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        # ── twoback ───────────────────────────────────────────────────────────
        self.ui.rightrear.setSizePolicy(expand)
        self.ui.rightrear.setScaledContents(True)
        self.ui.leftrear.setSizePolicy(expand)
        self.ui.leftrear.setScaledContents(True)

        # ── Rear + Down ───────────────────────────────────────────────────────
        self.ui.leftrearcamera.setSizePolicy(expand)
        self.ui.leftrearcamera.setScaledContents(True)
        self.ui.rightrearcamera.setSizePolicy(expand)
        self.ui.rightrearcamera.setScaledContents(True)

        if self.ui.downwardcamera.layout() is None:
            lay = QHBoxLayout(self.ui.downwardcamera)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.setSpacing(0)
            self.ui.downwardcamera.setLayout(lay)
        else:
            lay = self.ui.downwardcamera.layout()
        self.ui.downcamera_2.setParent(self.ui.downwardcamera)
        lay.addWidget(self.ui.downcamera_2)
        self.ui.downcamera_2.setSizePolicy(expand)
        self.ui.downcamera_2.setScaledContents(True)
        self.ui.downwardcamera.setSizePolicy(expand)
        self.ui.twocameras.setSizePolicy(expand)
        self.ui.verticalLayout_4.setStretch(0, 1)
        self.ui.verticalLayout_4.setStretch(1, 1)

        # ── ZED + Down ────────────────────────────────────────────────────────
        self.ui.leftzed.setSizePolicy(expand)
        self.ui.leftzed.setScaledContents(True)

        if self.ui.downcamera_3.layout() is None:
            lay3 = QHBoxLayout(self.ui.downcamera_3)
            lay3.setContentsMargins(0, 0, 0, 0)
            lay3.setSpacing(0)
            self.ui.downcamera_3.setLayout(lay3)
        else:
            lay3 = self.ui.downcamera_3.layout()
        self.ui.downcameralabel_2.setParent(self.ui.downcamera_3)
        lay3.addWidget(self.ui.downcameralabel_2)
        self.ui.downcameralabel_2.setSizePolicy(expand)
        self.ui.downcameralabel_2.setScaledContents(True)
        self.ui.downcamera_3.setSizePolicy(expand)
        self.ui.zedvariants.setSizePolicy(expand)
        self.ui.verticalLayout_5.setStretch(0, 1)
        self.ui.verticalLayout_5.setStretch(1, 1)

        # # ── Down only ─────────────────────────────────────────────────────────
        # if self.ui.downcameraframe.layout() is None:
        #     laydc = QHBoxLayout(self.ui.downcameraframe)
        #     laydc.setContentsMargins(0, 0, 0, 0)
        #     laydc.setSpacing(0)
        #     self.ui.downcameraframe.setLayout(laydc)
        # else:
        #     laydc = self.ui.downcameraframe.layout()
        # self.ui.downcameralabel.setParent(self.ui.downcameraframe)
        # laydc.addWidget(self.ui.downcameralabel)
        # self.ui.downcameralabel.setSizePolicy(expand)
        # self.ui.downcameralabel.setScaledContents(True)

        # ── 3 IP cameras page ─────────────────────────────────────────────────
        # Top row: leftone + rightone already in horizontalLayout_12 — just expand
        self.ui.leftone.setSizePolicy(expand)
        self.ui.leftone.setScaledContents(True)
        self.ui.rightone.setSizePolicy(expand)
        self.ui.rightone.setScaledContents(True)
        self.ui.twocamerasframe.setSizePolicy(expand)

        # Bottom: downcamera_4 needs a layout injected into thirdcameraframe
        if self.ui.thirdcameraframe.layout() is None:
            lay4 = QHBoxLayout(self.ui.thirdcameraframe)
            lay4.setContentsMargins(0, 0, 0, 0)
            lay4.setSpacing(0)
            self.ui.thirdcameraframe.setLayout(lay4)
        else:
            lay4 = self.ui.thirdcameraframe.layout()
        self.ui.downcamera_4.setParent(self.ui.thirdcameraframe)
        lay4.addWidget(self.ui.downcamera_4)
        self.ui.downcamera_4.setSizePolicy(expand)
        self.ui.downcamera_4.setScaledContents(True)
        self.ui.thirdcameraframe.setSizePolicy(expand)

        # Top row 1 stretch : bottom row 1 stretch — equal halves
        self.ui.verticalLayout_6.setStretch(0, 1)   # twocamerasframe
        self.ui.verticalLayout_6.setStretch(1, 1)   # thirdcameraframe

    def update_label(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        pixmap = pixmap.scaled(
            self.ui.zedlabel.width(),
            self.ui.zedlabel.height(),
            Qt.KeepAspectRatio
        )
        self.ui.zedlabel.setPixmap(pixmap)

    def closeEvent(self, event):
        self.zed_thread.stop()
        self.ip_thread.stop()
        self.joystick.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    old_hook = sys.excepthook
    def exception_hook(exctype, value, tb):
        traceback.print_exception(exctype, value, tb)
        old_hook(exctype, value, tb)
    sys.excepthook = exception_hook
    window = MainWindow()
    window.show()
    sys.exit(app.exec())