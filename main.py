import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSizePolicy, QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from ui import Ui_MainWindow
from uiControls.window_controls import WindowControls
from camerasStreaming.streaming_receiver import ZEDStreamThread
from camerasStreaming.ip_streaming import IPCameraStreamThread
from ControllerMapping.ControllerButtons import ControllerOverlayLabel
from ControllerMapping.LateralButtons import LateralOverlayLabel
from Control.joystick_class import Joystick
# from Control.motor_sliders import MotorSliders


class MainWindow(QMainWindow, WindowControls):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_window_controls(self.ui)

        # ── Fix layouts BEFORE anything else ─────────────────────────────────
        self._inject_layouts()

        # ── Controller overlays ───────────────────────────────────────────────
        self._setup_controller_overlay()
        self._setup_lateral_overlay()

        # ── Joystick ──────────────────────────────────────────────────────────
        self.joystick = Joystick()
        self.joystick.start()

        # self.motor_sliders = MotorSliders(self.ui, self.joystick.pixhawk)

        # ── ZED stereo camera stream ───────────────────────────────────────────
        self.zed_thread = ZEDStreamThread('192.168.33.1:30000')

        # ZED mode page (firstcamerasmodewidget)
        self.zed_thread.left_frame_ready.connect(self.ui.zedleftlabel.setPixmap)
        self.zed_thread.right_frame_ready.connect(self.ui.zedrightlabel.setPixmap)

        # ZED + Down page (zedanddown)
        self.zed_thread.left_frame_ready.connect(self.ui.leftzed.setPixmap)
        self.zed_thread.right_frame_ready.connect(self.ui.rightzed.setPixmap)

        self.zed_thread.error_occurred.connect(lambda msg: print(msg))
        self.zed_thread.start()

        # ── IP camera streams ──────────────────────────────────────────────────
        self.ip_thread = IPCameraStreamThread()

        # Forward camera → rear labels
        self.ip_thread.forward_frame_ready.connect(self.ui.rightrear.setPixmap)
        self.ip_thread.forward_frame_ready.connect(self.ui.rightrearcamera.setPixmap)

        # # Grippers camera → down camera labels
        self.ip_thread.downward_frame_ready.connect(self.ui.downcameralabel.setPixmap)
        self.ip_thread.downward_frame_ready.connect(self.ui.downcameralabel_2.setPixmap)
        self.ip_thread.downward_frame_ready.connect(self.ui.downcamera_2.setPixmap)

        # # Grippers camera → left rear
        self.ip_thread.grippers_frame_ready.connect(self.ui.leftrear.setPixmap)
        self.ip_thread.grippers_frame_ready.connect(self.ui.leftrearcamera.setPixmap)
        

        self.ip_thread.error_occurred.connect(lambda msg: print(msg))
        self.ip_thread.start()

    # ── Layout injection ──────────────────────────────────────────────────────

    def _inject_layouts(self):
        """
        The .ui file uses absolute geometry for some child labels inside frames.
        We replace that with proper QHBoxLayout/QVBoxLayout so the labels
        actually fill their parent frames and the stacked pages show correctly.
        """
        expand = QSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        # ── twoback page: rightrear + leftrear ────────────────────────────────
        self.ui.rightrear.setSizePolicy(expand)
        self.ui.rightrear.setScaledContents(True)
        self.ui.leftrear.setSizePolicy(expand)
        self.ui.leftrear.setScaledContents(True)

        # ── Rear + Down page (twocamerasanddown / verticalLayout_4) ───────────

        # Top row: leftrearcamera + rightrearcamera
        self.ui.leftrearcamera.setSizePolicy(expand)
        self.ui.leftrearcamera.setScaledContents(True)
        self.ui.rightrearcamera.setSizePolicy(expand)
        self.ui.rightrearcamera.setScaledContents(True)

        # Bottom row: downcamera_2 — inject a layout into downwardcamera frame
        # because the .ui has no layout on this frame (uses absolute geometry)
        if self.ui.downwardcamera.layout() is None:
            lay = QHBoxLayout(self.ui.downwardcamera)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.setSpacing(0)
            self.ui.downwardcamera.setLayout(lay)
        else:
            lay = self.ui.downwardcamera.layout()

        # Re-parent downcamera_2 into the layout
        self.ui.downcamera_2.setParent(self.ui.downwardcamera)
        lay.addWidget(self.ui.downcamera_2)
        self.ui.downcamera_2.setSizePolicy(expand)
        self.ui.downcamera_2.setScaledContents(True)

        # Give equal stretch to top and bottom rows
        self.ui.downwardcamera.setSizePolicy(expand)
        self.ui.twocameras.setSizePolicy(expand)
        self.ui.verticalLayout_4.setStretch(0, 1)   # twocameras  (top)
        self.ui.verticalLayout_4.setStretch(1, 1)   # downwardcamera (bottom)

        # ── ZED + Down page (zedanddown / verticalLayout_5) ───────────────────

        # Top row: leftzed + rightzed
        self.ui.leftzed.setSizePolicy(expand)
        self.ui.leftzed.setScaledContents(True)
        self.ui.rightzed.setSizePolicy(expand)
        self.ui.rightzed.setScaledContents(True)

        # Bottom row: downcameralabel_2 — inject layout into downcamera_3 frame
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

        # Give equal stretch to top and bottom rows
        self.ui.downcamera_3.setSizePolicy(expand)
        self.ui.zedvariants.setSizePolicy(expand)
        self.ui.verticalLayout_5.setStretch(0, 1)   # zedvariants  (top)
        self.ui.verticalLayout_5.setStretch(1, 1)   # downcamera_3 (bottom)

        # ── downcamera page: single label fills frame ─────────────────────────
        if self.ui.downcameraframe.layout() is None:
            laydc = QHBoxLayout(self.ui.downcameraframe)
            laydc.setContentsMargins(0, 0, 0, 0)
            laydc.setSpacing(0)
            self.ui.downcameraframe.setLayout(laydc)
        else:
            laydc = self.ui.downcameraframe.layout()

        self.ui.downcameralabel.setParent(self.ui.downcameraframe)
        laydc.addWidget(self.ui.downcameralabel)
        self.ui.downcameralabel.setSizePolicy(expand)
        self.ui.downcameralabel.setScaledContents(True)

    # ── Controller overlays ───────────────────────────────────────────────────

    def _setup_lateral_overlay(self):
        old_label = self.ui.controllerlateral
        parent    = old_label.parent()
        geometry  = old_label.geometry()
        pixmap    = old_label.pixmap()

        callbacks = {
            "RB": lambda: print("RB clicked"),
            "LB": lambda: print("LB clicked"),
            "LT": lambda: print("LT clicked"),
            "RT": lambda: print("RT clicked"),
        }
        self.lateral_overlay = LateralOverlayLabel(parent=parent, callbacks=callbacks)
        self.lateral_overlay.setGeometry(geometry)
        self.lateral_overlay.setPixmap(pixmap)
        self.lateral_overlay.setScaledContents(old_label.hasScaledContents())
        self.lateral_overlay.setAlignment(old_label.alignment())
        self.lateral_overlay.show()
        old_label.hide()

    def _setup_controller_overlay(self):
        old_label = self.ui.controllernormal
        parent    = old_label.parent()
        geometry  = old_label.geometry()
        pixmap    = old_label.pixmap()

        callbacks = {
            "A":          lambda: print("A clicked"),
            "B":          lambda: print("B clicked"),
            "X":          lambda: print("X clicked"),
            "Y":          lambda: print("Y clicked"),
            "Start":      lambda: print("Start clicked"),
            "Back":       lambda: print("Back clicked"),
            "DPad":       lambda: print("DPad clicked"),
            "DPad_Up":    lambda: print("DPad Up clicked"),
            "DPad_Down":  lambda: print("DPad Down clicked"),
            "DPad_Right": lambda: print("DPad Right clicked"),
            "DPad_Left":  lambda: print("DPad Left clicked"),
            "LS":         lambda: print("Left Stick clicked (LS3)"),
            "LS_Up":      lambda: print("Left Stick Up"),
            "LS_Down":    lambda: print("Left Stick Down"),
            "LS_Left":    lambda: print("Left Stick Left"),
            "LS_Right":   lambda: print("Left Stick Right"),
            "RS":         lambda: print("Right Stick clicked (RS3)"),
            "RS_Up":      lambda: print("Right Stick Up"),
            "RS_Down":    lambda: print("Right Stick Down"),
            "RS_Left":    lambda: print("Right Stick Left"),
            "RS_Right":   lambda: print("Right Stick Right"),
        }

        self.controller_overlay = ControllerOverlayLabel(parent=parent, callbacks=callbacks)
        self.controller_overlay.setGeometry(geometry)
        self.controller_overlay.setPixmap(pixmap)
        self.controller_overlay.setScaledContents(old_label.hasScaledContents())
        self.controller_overlay.setAlignment(old_label.alignment())
        self.controller_overlay.show()
        old_label.hide()

    # ── Misc ──────────────────────────────────────────────────────────────────

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())