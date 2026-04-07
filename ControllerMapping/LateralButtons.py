import math
from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPolygonF, QPainter, QColor, QPen
from PySide6.QtWidgets import QLabel
from ControllerMapping.ControllerButtons import ControllerButton, DEFAULT_COLORS


def _chaikin_smooth(points: list[QPointF], iterations: int = 3) -> list[QPointF]:
    """Smooth a polygon using Chaikin's corner-cutting algorithm."""
    pts = points
    for _ in range(iterations):
        new_pts = []
        n = len(pts)
        for i in range(n):
            p0 = pts[i]
            p1 = pts[(i + 1) % n]
            q = QPointF(0.75 * p0.x() + 0.25 * p1.x(),
                        0.75 * p0.y() + 0.25 * p1.y())
            r = QPointF(0.25 * p0.x() + 0.75 * p1.x(),
                        0.25 * p0.y() + 0.75 * p1.y())
            new_pts.append(q)
            new_pts.append(r)
        pts = new_pts
    return pts


# ── Raw Points ────────────────────────────────────────────────────────────────

_RB_RAW = [
     QPointF(987, 359),
    QPointF(987, 382),
    QPointF(986, 400),
    QPointF(987, 408),
    QPointF(993, 410),
    QPointF(1005, 411),
    QPointF(1024, 411),
    QPointF(1062, 412),
    QPointF(1094, 412),
    QPointF(1120, 413),
    QPointF(1142, 415),
    QPointF(1158, 415),
    QPointF(1177, 415),
    QPointF(1181, 413),
    QPointF(1181, 392),
    QPointF(1179, 385),
    QPointF(1171, 372),
    QPointF(1164, 367),
    QPointF(1154, 362),
    QPointF(1142, 358),
    QPointF(1129, 355),
    QPointF(1115, 352),
    QPointF(1099, 349),
    QPointF(1078, 348),
    QPointF(1064, 347),
    QPointF(1046, 346),
    QPointF(1032, 346),
    QPointF(1019, 345),
    QPointF(1004, 346),
    QPointF(996, 346),
    QPointF(990, 350),
    QPointF(988, 353),
]

_LB_RAW = [
    QPointF(547, 344),
    QPointF(560, 346),
    QPointF(564, 352),
    QPointF(564, 363),
    QPointF(565, 397),
    QPointF(563, 404),
    QPointF(549, 409),
    QPointF(529, 409),
    QPointF(493, 409),
    QPointF(442, 409),
    QPointF(378, 408),
    QPointF(369, 405),
    QPointF(369, 382),
    QPointF(377, 369),
    QPointF(394, 354),
    QPointF(414, 347),
    QPointF(443, 345),
    QPointF(465, 344),
    QPointF(485, 343),
    QPointF(508, 343),
    QPointF(534, 343),
]

_LT_RAW = [
    QPointF(447, 452),
    QPointF(450, 448),
    QPointF(483, 448),
    QPointF(506, 451),
    QPointF(513, 452),
    QPointF(512, 464),
    QPointF(512, 478),
    QPointF(512, 510),
    QPointF(512, 533),
    QPointF(511, 560),
    QPointF(512, 574),
    QPointF(512, 584),
    QPointF(507, 593),
    QPointF(498, 596),
    QPointF(479, 596),
    QPointF(462, 595),
    QPointF(453, 588),
    QPointF(452, 581),
    QPointF(452, 561),
    QPointF(450, 550),
    QPointF(449, 527),
    QPointF(448, 515),
    QPointF(447, 497),
]

_RT_RAW = [
    QPointF(1037, 454),
    QPointF(1051, 448),
    QPointF(1073, 447),
    QPointF(1095, 447),
    QPointF(1103, 449),
    QPointF(1105, 453),
    QPointF(1105, 466),
    QPointF(1105, 481),
    QPointF(1104, 493),
    QPointF(1104, 506),
    QPointF(1103, 524),
    QPointF(1102, 537),
    QPointF(1101, 546),
    QPointF(1100, 557),
    QPointF(1099, 571),
    QPointF(1099, 583),
    QPointF(1098, 586),
    QPointF(1097, 590),
    QPointF(1091, 596),
    QPointF(1078, 598),
    QPointF(1051, 597),
    QPointF(1041, 589),
    QPointF(1038, 577),
    QPointF(1037, 556),
    QPointF(1037, 537),
    QPointF(1037, 525),
    QPointF(1037, 507),
    QPointF(1037, 483),
]


# ── Button Definitions ────────────────────────────────────────────────────────

LATERAL_BUTTONS: dict[str, list[QPointF]] = {
    "RB": _chaikin_smooth(_RB_RAW, iterations=3),
    "LB": _chaikin_smooth(_LB_RAW, iterations=3),
    "LT": _chaikin_smooth(_LT_RAW, iterations=3),
    "RT": _chaikin_smooth(_RT_RAW, iterations=3),
}

LATERAL_COLORS: dict[str, dict] = {
    "RB": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "LB": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "LT": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "RT": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
}


# ── Build ─────────────────────────────────────────────────────────────────────

def build_lateral_buttons(callbacks: dict = None) -> list[ControllerButton]:
    callbacks = callbacks or {}
    buttons = []
    for name, points in LATERAL_BUTTONS.items():
        polygon = QPolygonF(points)
        colors = LATERAL_COLORS.get(name, DEFAULT_COLORS)
        btn = ControllerButton(
            name=name,
            polygon=polygon,
            color_normal=colors["normal"],
            color_hover=colors["hover"],
            color_pressed=colors["pressed"],
            on_click=callbacks.get(name),
        )
        buttons.append(btn)
    return buttons


# ── Overlay Label ─────────────────────────────────────────────────────────────

class LateralOverlayLabel(QLabel):

    def __init__(self, parent=None, callbacks: dict = None):
        super().__init__(parent)
        self.buttons = build_lateral_buttons(callbacks or {})
        self.setMouseTracking(True)

    def _scale_factors(self):
        pixmap = self.pixmap()
        if pixmap is None:
            return 1.0, 1.0
        if self.hasScaledContents():
            return self.width() / pixmap.width(), self.height() / pixmap.height()
        return 1.0, 1.0

    def _scale_point(self, point: QPointF) -> QPointF:
        sx, sy = self._scale_factors()
        return QPointF(point.x() * sx, point.y() * sy)

    def _unscale_point(self, point: QPointF) -> QPointF:
        sx, sy = self._scale_factors()
        if sx == 0 or sy == 0:
            return point
        return QPointF(point.x() / sx, point.y() / sy)

    def _scaled_polygon(self, polygon: QPolygonF) -> QPolygonF:
        return QPolygonF([self._scale_point(p) for p in polygon])

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for btn in self.buttons:
            scaled_poly = self._scaled_polygon(btn.polygon)
            color = btn.current_color()
            painter.setBrush(color)
            pen_color = QColor(color)
            pen_color.setAlpha(min(255, color.alpha() + 80))
            painter.setPen(QPen(pen_color, 1.5))
            painter.drawPolygon(scaled_poly)
        painter.end()

    def mouseMoveEvent(self, event):
        pos = self._unscale_point(QPointF(event.position()))
        changed = False
        for btn in self.buttons:
            was_hovered = btn.is_hovered
            btn.is_hovered = btn.contains(pos)
            if btn.is_hovered != was_hovered:
                changed = True
        if changed:
            self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = self._unscale_point(QPointF(event.position()))
            for btn in self.buttons:
                if btn.contains(pos):
                    btn.is_pressed = True
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = self._unscale_point(QPointF(event.position()))
            for btn in self.buttons:
                if btn.is_pressed and btn.contains(pos):
                    if btn.on_click:
                        btn.on_click()
                btn.is_pressed = False
            self.update()

    def leaveEvent(self, event):
        for btn in self.buttons:
            btn.is_hovered = False
            btn.is_pressed = False
        self.update()