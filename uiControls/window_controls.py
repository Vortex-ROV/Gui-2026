from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QRect
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget, QVBoxLayout, QPushButton, QFrame
from PySide6.QtGui import QFont

class CameraMenuPopup(QWidget):
    """Vertical floating camera selection menu that appears under camerasbutton"""

    CAMERA_PAGES = [
        ("🎥  ZED Stereo",          0),
        ("📷  Rear Cameras",         1),
        ("⬇️  Down Camera",          2),
        ("🔀  Rear + Down",          3),
        ("🔭  ZED + Down",           4),
    ]

    def __init__(self, parent, on_select):
        super().__init__(parent, Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.on_select = on_select
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        container = QFrame(self)
        container.setObjectName("cameraMenuContainer")
        container.setStyleSheet("""
            QFrame#cameraMenuContainer {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(4, 10, 30),
                    stop:1 rgb(5, 18, 50)
                );
                border: 1px solid rgb(201, 169, 97);
                border-top: none;
                border-radius: 0px 0px 6px 6px;
            }
        """)
        inner = QVBoxLayout(container)
        inner.setContentsMargins(0, 4, 0, 4)
        inner.setSpacing(0)

        font = QFont("Segoe UI", 10)

        for label, index in self.CAMERA_PAGES:
            btn = QPushButton(label, container)
            btn.setFont(font)
            btn.setFixedHeight(38)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: rgb(210, 210, 230);
                    border: none;
                    border-bottom: 1px solid rgba(201, 169, 97, 40);
                    padding: 0px 16px;
                    text-align: left;
                    font-size: 10pt;
                }
                QPushButton:hover {
                    background-color: rgba(201, 169, 97, 25);
                    color: rgb(201, 169, 97);
                }
                QPushButton:pressed {
                    background-color: rgba(201, 169, 97, 50);
                }
            """)
            btn.clicked.connect(lambda checked=False, i=index: self._select(i))
            inner.addWidget(btn)

        # Remove border from last button
        if inner.count():
            inner.itemAt(inner.count() - 1).widget().setStyleSheet(
                inner.itemAt(inner.count() - 1).widget().styleSheet().replace(
                    "border-bottom: 1px solid rgba(201, 169, 97, 40);", "border-bottom: none;"
                )
            )

        layout.addWidget(container)
        self.setFixedWidth(200)
        self.setFixedHeight(len(self.CAMERA_PAGES) * 38 + 8)

    def _select(self, index):
        print(f"_select called with index={index}")
        try:
            print("calling on_select...")
            self.on_select(index)
            print("on_select done, calling close...")
            self.close()
            print("close done")
        except Exception as e:
            import traceback
            traceback.print_exc()

    def show_under(self, button: QPushButton):
        """Position and show the menu directly below the given button"""
        global_pos = button.mapToGlobal(QPoint(0, button.height()))
        self.move(global_pos)
        self.show()


class WindowControls:
    """Mixin class for custom window controls"""

    def setup_window_controls(self, ui):
        """Setup frameless window with custom controls"""
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Primary buttons
        ui.Exitbutton.clicked.connect(self.close)
        ui.Minimizebutton.clicked.connect(self.showMinimized)
        ui.MaximizeButton.clicked.connect(self.toggle_maximize)

        # Secondary buttons - welcome screen
        if hasattr(ui, 'Exitbutton_2'):
            ui.Exitbutton_2.clicked.connect(self.close)
        if hasattr(ui, 'Minimizebutton_2'):
            ui.Minimizebutton_2.clicked.connect(self.showMinimized)
        if hasattr(ui, 'MaximizeButton_2'):
            ui.MaximizeButton_2.clicked.connect(self.toggle_maximize)

        # Tertiary buttons - settings page
        if hasattr(ui, 'Exitbutton_3'):
            ui.Exitbutton_3.clicked.connect(self.close)
        if hasattr(ui, 'Minimizebutton_3'):
            ui.Minimizebutton_3.clicked.connect(self.showMinimized)
        if hasattr(ui, 'MaximizeButton_3'):
            ui.MaximizeButton_3.clicked.connect(self.toggle_maximize)

        # Screen transition - welcome → control
        if hasattr(ui, 'startButton'):
            ui.startButton.clicked.connect(lambda checked: self.fade_slide_transition(ui))

        # Navigation buttons
        if hasattr(ui, 'Menubutton'):
            ui.Menubutton.clicked.connect(self.go_to_settings)
        if hasattr(ui, 'tocontrolframe'):
            ui.tocontrolframe.clicked.connect(self.go_to_control)
        if hasattr(ui, 'yground'):
            ui.yground.clicked.connect(self.go_to_yester)
        if hasattr(ui, 'zed2iicon'):
            ui.zed2iicon.clicked.connect(self.go_to_camerasettings)
        if hasattr(ui, 'controllericon'):
            ui.controllericon.clicked.connect(self.go_to_settings)

        # ── Camera menu ───────────────────────────────────────────────────────
        if hasattr(ui, 'camerasbutton'):
            self._camera_menu = None
            ui.camerasbutton.clicked.connect(lambda checked: self._toggle_camera_menu())

        self.dragging = False
        self.offset = QPoint()

        # Setup dragging for main screen topBar
        if hasattr(ui, 'topBar'):
            ui.topBar.mousePressEvent = self.topbar_press
            ui.topBar.mouseMoveEvent = self.topbar_move
            ui.topBar.mouseReleaseEvent = self.topbar_release
            ui.topBar.mouseDoubleClickEvent = self.topbar_double_click

        # Setup dragging for welcome screen
        if hasattr(ui, 'welcomeScreen'):
            ui.welcomeScreen.mousePressEvent = self.topbar_press
            ui.welcomeScreen.mouseMoveEvent = self.topbar_move
            ui.welcomeScreen.mouseReleaseEvent = self.topbar_release
            ui.welcomeScreen.mouseDoubleClickEvent = self.topbar_double_click

        # Setup dragging for settings topBar
        if hasattr(ui, 'topBar_2'):
            ui.topBar_2.mousePressEvent = self.topbar_press
            ui.topBar_2.mouseMoveEvent = self.topbar_move
            ui.topBar_2.mouseReleaseEvent = self.topbar_release
            ui.topBar_2.mouseDoubleClickEvent = self.topbar_double_click

        self.ui = ui

    # ── Camera Menu ───────────────────────────────────────────────────────────

    def _toggle_camera_menu(self):
        """Show or hide the camera selection dropdown menu"""
        if self._camera_menu and self._camera_menu.isVisible():
            self._camera_menu.close()
            return

        self._camera_menu = CameraMenuPopup(
            parent=self,
            on_select=self._switch_camera_view
        )
        self._camera_menu.show_under(self.ui.camerasbutton)

    def _switch_camera_view(self, index: int):
        """Switch middlewidget to the selected camera page"""
        if hasattr(self.ui, 'middlewidget'):
            self.ui.middlewidget.setCurrentIndex(index)

    # ── Navigation ────────────────────────────────────────────────────────────

    def go_to_settings(self):
        """Menu button → settings page, controller panel"""
        self.ui.MainWidget.setCurrentIndex(2)
        self.ui.stackedWidget.setCurrentIndex(0)

    def go_to_control(self):
        """Back button → control widget"""
        self.ui.MainWidget.setCurrentIndex(0)

    def go_to_yester(self):
        """Team button → settings page, yester panel"""
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_to_camerasettings(self):
        """ZED icon → settings page, camera settings panel"""
        self.ui.stackedWidget.setCurrentIndex(2)

    # ── Transitions ───────────────────────────────────────────────────────────

    def fade_slide_transition(self, ui):
        """Fade out welcome screen, then slide in control widget"""
        welcome_widget = ui.welcomeWidget
        self.opacity_effect_out = QGraphicsOpacityEffect()
        welcome_widget.setGraphicsEffect(self.opacity_effect_out)

        self.fade_out = QPropertyAnimation(self.opacity_effect_out, b"opacity")
        self.fade_out.setDuration(250)
        self.fade_out.setStartValue(1.0)
        self.fade_out.setEndValue(0.0)
        self.fade_out.setEasingCurve(QEasingCurve.Type.InQuad)
        self.fade_out.finished.connect(lambda: self.slide_in_control(ui))
        self.fade_out.start()

    def slide_in_control(self, ui):
        """Slide in the control widget"""
        ui.MainWidget.setCurrentIndex(0)
        control_widget = ui.ControlWidget

        self.opacity_effect_in = QGraphicsOpacityEffect()
        control_widget.setGraphicsEffect(self.opacity_effect_in)

        original_pos = control_widget.pos()
        control_widget.move(200, 0)

        self.slide_in_anim = QPropertyAnimation(control_widget, b"pos")
        self.slide_in_anim.setDuration(350)
        self.slide_in_anim.setStartValue(QPoint(200, 0))
        self.slide_in_anim.setEndValue(original_pos)
        self.slide_in_anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.fade_in_anim = QPropertyAnimation(self.opacity_effect_in, b"opacity")
        self.fade_in_anim.setDuration(350)
        self.fade_in_anim.setStartValue(0.0)
        self.fade_in_anim.setEndValue(1.0)

        self.slide_fade_group = QParallelAnimationGroup()
        self.slide_fade_group.addAnimation(self.slide_in_anim)
        self.slide_fade_group.addAnimation(self.fade_in_anim)
        self.slide_fade_group.finished.connect(lambda: control_widget.setGraphicsEffect(None))
        self.slide_fade_group.start()

    # ── Window Controls ───────────────────────────────────────────────────────

    def showMinimized(self):
        """Override minimize to show in taskbar properly"""
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
        super().showMinimized()

    def showNormal(self):
        """Restore frameless when unminimizing"""
        self.setWindowFlags(Qt.FramelessWindowHint)
        super().showNormal()
        self.show()

    def toggle_maximize(self):
        """Toggle between fullscreen and normal window"""
        if self.isFullScreen() or self.isMaximized():
            self.showNormal()
        else:
            self.showFullScreen()

    # ── Dragging ──────────────────────────────────────────────────────────────

    def topbar_press(self, event):
        """Start dragging"""
        if event.button() == Qt.LeftButton and not (self.isFullScreen() or self.isMaximized()):
            self.dragging = True
            self.offset = event.pos()

    def topbar_move(self, event):
        """Move window when dragging"""
        if self.dragging:
            if self.isFullScreen() or self.isMaximized():
                self.showNormal()
            self.move(self.mapToGlobal(event.pos()) - self.offset)

    def topbar_release(self, event):
        """Stop dragging"""
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def topbar_double_click(self, event):
        """Double-click to toggle maximize/fullscreen"""
        if event.button() == Qt.LeftButton:
            self.toggle_maximize()