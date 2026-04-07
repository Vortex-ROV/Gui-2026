import math

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPolygonF, QPainter, QColor, QPen
from PySide6.QtWidgets import QLabel
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ControllerButton:
    name: str
    polygon: QPolygonF
    color_normal: QColor = field(default_factory=lambda: QColor(255, 255, 255, 0))
    color_hover: QColor = field(default_factory=lambda: QColor(255, 255, 255, 60))
    color_pressed: QColor = field(default_factory=lambda: QColor(255, 255, 255, 120))
    on_click: Callable = None
    is_hovered: bool = field(default=False, init=False)
    is_pressed: bool = field(default=False, init=False)

    def contains(self, point: QPointF) -> bool:
        return self.polygon.containsPoint(point, Qt.FillRule.OddEvenFill)

    def current_color(self) -> QColor:
        if self.is_pressed:
            return self.color_pressed
        elif self.is_hovered:
            return self.color_hover
        return self.color_normal


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_circle(cx: float, cy: float, r: float, n: int = 24) -> list[QPointF]:
    """Return n evenly-spaced points approximating a circle."""
    return [
        QPointF(cx + r * math.cos(2 * math.pi * i / n),
                cy + r * math.sin(2 * math.pi * i / n))
        for i in range(n)
    ]

def _make_ellipse(cx: float, cy: float, rx: float, ry: float, n: int = 16) -> list[QPointF]:
    """Return n evenly-spaced points approximating an ellipse."""
    return [
        QPointF(cx + rx * math.cos(2 * math.pi * i / n),
                cy + ry * math.sin(2 * math.pi * i / n))
        for i in range(n)
    ]


# ── Button Definitions ────────────────────────────────────────────────────────

CONTROLLER_BUTTONS: dict[str, list[QPointF]] = {
    # A: centroid ≈ (1054, 388), radius ≈ 34
    "A": _make_circle(1054, 388, 34),

    # B: centroid ≈ (1130, 313), radius ≈ 33
    "B": _make_circle(1130, 313, 33),

    # X: centroid ≈ (976, 308), radius ≈ 30
    "X": _make_circle(976, 308, 30),

    # Y: centroid ≈ (1054, 237), radius ≈ 33
    "Y": _make_circle(1054, 237, 33),

    # Start: centroid ≈ (868, 318), oval wider than tall
    "Start": _make_ellipse(868, 318, 24, 16),

    # Back: centroid ≈ (656, 315), oval wider than tall
    "Back": _make_ellipse(656, 315, 23, 17),

    # ── D-Pad ─────────────────────────────────────────────────────────────────
    "DPad": [
        QPointF(541, 454),
        QPointF(554, 451),
        QPointF(566, 445),
        QPointF(574, 440),
        QPointF(580, 431),
        QPointF(581, 417),
        QPointF(583, 409),
        QPointF(589, 404),
        QPointF(597, 403),
        QPointF(606, 403),
        QPointF(615, 404),
        QPointF(625, 406),
        QPointF(629, 414),
        QPointF(630, 423),
        QPointF(632, 432),
        QPointF(637, 440),
        QPointF(644, 445),
        QPointF(651, 449),
        QPointF(660, 451),
        QPointF(668, 452),
        QPointF(676, 454),
        QPointF(678, 460),
        QPointF(680, 467),
        QPointF(681, 476),
        QPointF(682, 483),
        QPointF(682, 492),
        QPointF(679, 498),
        QPointF(672, 500),
        QPointF(665, 501),
        QPointF(658, 503),
        QPointF(651, 504),
        QPointF(644, 506),
        QPointF(639, 511),
        QPointF(636, 519),
        QPointF(635, 525),
        QPointF(635, 534),
        QPointF(634, 542),
        QPointF(630, 547),
        QPointF(621, 549),
        QPointF(614, 551),
        QPointF(603, 551),
        QPointF(596, 551),
        QPointF(589, 550),
        QPointF(581, 547),
        QPointF(582, 538),
        QPointF(582, 532),
        QPointF(582, 526),
        QPointF(580, 518),
        QPointF(576, 513),
        QPointF(574, 508),
        QPointF(568, 505),
        QPointF(565, 504),
        QPointF(559, 502),
        QPointF(552, 501),
        QPointF(547, 500),
        QPointF(541, 497),
        QPointF(534, 492),
        QPointF(532, 484),
        QPointF(532, 476),
        QPointF(531, 469),
        QPointF(531, 461),
    ],

    "DPad_Up": [
        QPointF(618.0, 402.0),
        QPointF(611.0, 402.0),
        QPointF(595.0, 404.0),
        QPointF(586.0, 404.0),
        QPointF(581.0, 411.0),
        QPointF(580.0, 421.0),
        QPointF(576.0, 437.0),
        QPointF(569.0, 446.0),
        QPointF(580.0, 449.0),
        QPointF(586.0, 449.0),
        QPointF(595.0, 448.0),
        QPointF(603.0, 447.0),
        QPointF(609.0, 448.0),
        QPointF(622.0, 448.0),
        QPointF(630.0, 446.0),
        QPointF(639.0, 446.0),
        QPointF(633.0, 438.0),
        QPointF(630.0, 432.0),
        QPointF(628.0, 421.0),
        QPointF(627.0, 412.0),
        QPointF(623.9, 403.7),
    ],

    "DPad_Down": [
        QPointF(581.0, 518.0),
        QPointF(583.0, 529.0),
        QPointF(583.0, 540.0),
        QPointF(587.7, 546.1),
        QPointF(594.0, 548.0),
        QPointF(605.0, 549.0),
        QPointF(617.0, 547.0),
        QPointF(627.0, 544.0),
        QPointF(631.0, 535.0),
        QPointF(633.0, 514.0),
        QPointF(635.5, 511.5),
        QPointF(633.0, 509.0),
        QPointF(628.0, 509.0),
        QPointF(623.0, 508.0),
        QPointF(616.0, 507.0),
        QPointF(609.0, 508.0),
        QPointF(600.0, 509.0),
        QPointF(596.0, 509.0),
        QPointF(592.0, 509.0),
        QPointF(584.0, 508.0),
        QPointF(577.0, 509.0),
    ],

    "DPad_Right": [
        QPointF(673.0, 454.0),
        QPointF(661.0, 453.0),
        QPointF(649.0, 452.0),
        QPointF(638.0, 445.0),
        QPointF(637.0, 460.0),
        QPointF(637.0, 471.0),
        QPointF(637.0, 480.0),
        QPointF(637.0, 484.0),
        QPointF(638.0, 489.0),
        QPointF(638.0, 495.0),
        QPointF(639.0, 501.0),
        QPointF(644.6, 504.5),
        QPointF(651.0, 501.0),
        QPointF(672.0, 498.0),
        QPointF(679.0, 492.0),
        QPointF(678.0, 474.0),
        QPointF(678.0, 458.0),
        QPointF(674.4, 454.8),
    ],

    "DPad_Left": [
        QPointF(559.0, 450.0),
        QPointF(551.0, 451.0),
        QPointF(542.0, 453.0),
        QPointF(535.8, 458.8),
        QPointF(534.0, 467.0),
        QPointF(533.0, 479.0),
        QPointF(534.2, 488.5),
        QPointF(537.0, 493.0),
        QPointF(552.0, 497.0),
        QPointF(567.6, 502.8),
        QPointF(569.0, 503.0),
        QPointF(570.0, 497.0),
        QPointF(570.0, 486.0),
        QPointF(570.0, 474.0),
        QPointF(570.0, 463.0),
        QPointF(570.0, 452.0),
        QPointF(567.0, 447.0),
    ],

    # ── Righ Stick ────────────────────────────────────────────────────────────
    # Full circle generated from fitted center=(906, 490), radius=65
    "RS": _make_circle(906, 480, 65, 24),

    # Arrow triangles placed just outside the circle
    # tip at center ± 100px, base at center ± 75px, half-width 16px
    "RS_Up": [
    QPointF(906, 375),   # tip
    QPointF(922, 402),   # base right
    QPointF(890, 402),   # base left
    ],
    "RS_Down": [
        QPointF(906, 585),   # tip
        QPointF(890, 558),   # base left
        QPointF(922, 558),   # base right
    ],
    "RS_Left": [
        QPointF(801, 480),   # tip
        QPointF(828, 464),   # base top
        QPointF(828, 496),   # base bottom
    ],
    "RS_Right": [
        QPointF(1011, 480),  # tip
        QPointF(984, 496),   # base bottom
        QPointF(984, 464),   # base top
    ],

    # ── Left Stick ───────────────────────────────────────────────────────────
    # Full circle generated from fitted center=(471, 310), radius=60
    "LS": _make_circle(471, 310, 60, 24),

    # Arrow triangles placed just outside the circle
    # tip at center ± 95px, base at center ± 70px, half-width 16px
    "LS_Up": [
        QPointF(471, 215),   # tip
        QPointF(487, 242),   # base right
        QPointF(455, 242),   # base left
    ],
    "LS_Down": [
        QPointF(471, 405),   # tip
        QPointF(455, 378),   # base left
        QPointF(487, 378),   # base right
    ],
    "LS_Left": [
        QPointF(376, 310),   # tip
        QPointF(403, 294),   # base top
        QPointF(403, 326),   # base bottom
    ],
    "LS_Right": [
        QPointF(566, 310),   # tip
        QPointF(539, 326),   # base bottom
        QPointF(539, 294),   # base top
    ],
}

BUTTON_COLORS: dict[str, dict] = {
    "A": {
        "normal":  QColor(0, 200, 0, 0),
        "hover":   QColor(0, 200, 0, 80),
        "pressed": QColor(0, 200, 0, 180),
    },
    "B": {
        "normal":  QColor(200, 0, 0, 0),
        "hover":   QColor(200, 0, 0, 80),
        "pressed": QColor(200, 0, 0, 180),
    },
    "X": {
        "normal":  QColor(0, 100, 200, 0),
        "hover":   QColor(0, 100, 200, 80),
        "pressed": QColor(0, 100, 200, 180),
    },
    "Y": {
        "normal":  QColor(200, 200, 0, 0),
        "hover":   QColor(200, 200, 0, 80),
        "pressed": QColor(200, 200, 0, 180),
    },
    
    "Start": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "Back": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "DPad": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 60),
        "pressed": QColor(255, 255, 255, 150),
    },
    "DPad_Up": {
        "normal":  QColor(0, 220, 220, 0),
        "hover":   QColor(0, 220, 220, 80),
        "pressed": QColor(0, 220, 220, 200),
    },
    "DPad_Down": {
        "normal":  QColor(255, 140, 0, 0),
        "hover":   QColor(255, 140, 0, 80),
        "pressed": QColor(255, 140, 0, 200),
    },
    "DPad_Right": {
        "normal":  QColor(220, 0, 220, 0),
        "hover":   QColor(220, 0, 220, 80),
        "pressed": QColor(220, 0, 220, 200),
    },
    "DPad_Left": {
        "normal":  QColor(100, 220, 0, 0),
        "hover":   QColor(100, 220, 0, 80),
        "pressed": QColor(100, 220, 0, 200),
    },

    # ── Right Stick colors ─────────────────────────────────────────────────────
    "RS": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 50),
        "pressed": QColor(255, 255, 255, 160),
    },
    "RS_Up": {
        "normal":  QColor(80, 180, 255, 0),
        "hover":   QColor(80, 180, 255, 100),
        "pressed": QColor(80, 180, 255, 220),
    },
    "RS_Down": {
        "normal":  QColor(80, 180, 255, 0),
        "hover":   QColor(80, 180, 255, 100),
        "pressed": QColor(80, 180, 255, 220),
    },
    "RS_Left": {
        "normal":  QColor(80, 180, 255, 0),
        "hover":   QColor(80, 180, 255, 100),
        "pressed": QColor(80, 180, 255, 220),
    },
    "RS_Right": {
        "normal":  QColor(80, 180, 255, 0),
        "hover":   QColor(80, 180, 255, 100),
        "pressed": QColor(80, 180, 255, 220),
    },

    # ── Left Stick colors ────────────────────────────────────────────────────
    "LS": {
        "normal":  QColor(255, 255, 255, 0),
        "hover":   QColor(255, 255, 255, 50),
        "pressed": QColor(255, 255, 255, 160),
    },
    "LS_Up": {
        "normal":  QColor(255, 160, 40, 0),
        "hover":   QColor(255, 160, 40, 100),
        "pressed": QColor(255, 160, 40, 220),
    },
    "LS_Down": {
        "normal":  QColor(255, 160, 40, 0),
        "hover":   QColor(255, 160, 40, 100),
        "pressed": QColor(255, 160, 40, 220),
    },
    "LS_Left": {
        "normal":  QColor(255, 160, 40, 0),
        "hover":   QColor(255, 160, 40, 100),
        "pressed": QColor(255, 160, 40, 220),
    },
    "LS_Right": {
        "normal":  QColor(255, 160, 40, 0),
        "hover":   QColor(255, 160, 40, 100),
        "pressed": QColor(255, 160, 40, 220),
    },
}

DEFAULT_COLORS = {
    "normal":  QColor(255, 255, 255, 0),
    "hover":   QColor(255, 255, 255, 60),
    "pressed": QColor(255, 255, 255, 120),
}

# Buttons that are "sub-buttons" of a parent zone.
# When any member of a group is hit, the parent is suppressed.
_STICK_GROUPS: dict[str, set[str]] = {
    "LS": {"LS_Up", "LS_Down", "LS_Left", "LS_Right"},
    "RS": {"RS_Up", "RS_Down", "RS_Left", "RS_Right"},
    "DPad": {"DPad_Up", "DPad_Down", "DPad_Left", "DPad_Right"},
}
# Reverse map: direction key → parent name
_DIRECTION_PARENT: dict[str, str] = {
    d: parent for parent, dirs in _STICK_GROUPS.items() for d in dirs
}


def build_buttons(callbacks: dict = None) -> list[ControllerButton]:
    callbacks = callbacks or {}
    buttons = []
    for name, points in CONTROLLER_BUTTONS.items():
        polygon = QPolygonF(points)
        colors = BUTTON_COLORS.get(name, DEFAULT_COLORS)
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

class ControllerOverlayLabel(QLabel):

    def __init__(self, parent=None, callbacks: dict = None):
        super().__init__(parent)
        self.buttons = build_buttons(callbacks or {})
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

    def _hit_directions(self, pos: QPointF) -> set[str]:
        """Return the set of all directional sub-buttons (arrows) hit at pos."""
        return {
            btn.name
            for btn in self.buttons
            if btn.name in _DIRECTION_PARENT and btn.contains(pos)
        }

    def _suppressed_parents(self, pos: QPointF) -> set[str]:
        """
        Return parent button names that should be suppressed because a
        directional child is hit at pos.
        """
        hit = self._hit_directions(pos)
        return {_DIRECTION_PARENT[d] for d in hit}

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
        suppressed = self._suppressed_parents(pos)
        changed = False
        for btn in self.buttons:
            was_hovered = btn.is_hovered
            if btn.name in suppressed:
                btn.is_hovered = False
            else:
                btn.is_hovered = btn.contains(pos)
            if btn.is_hovered != was_hovered:
                changed = True
        if changed:
            self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = self._unscale_point(QPointF(event.position()))
            suppressed = self._suppressed_parents(pos)
            for btn in self.buttons:
                if btn.name in suppressed:
                    continue
                if btn.contains(pos):
                    btn.is_pressed = True
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = self._unscale_point(QPointF(event.position()))
            suppressed = self._suppressed_parents(pos)
            for btn in self.buttons:
                if btn.name in suppressed:
                    btn.is_pressed = False
                    continue
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