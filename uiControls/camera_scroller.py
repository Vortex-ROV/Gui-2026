"""Scrolls through camera pages on middlewidget using controller buttons."""

CAMERA_PAGES = [
    ("ZED Stereo",        0),
    ("Rear Cameras",      1),
    ("Down Camera",       2),
    ("Rear + Down",       3),
    ("ZED + Down",        4),
    ("3 IP Cameras",      5),
]


class CameraScroller:

    def __init__(self, stacked_widget):
        self._widget = stacked_widget

    @property
    def _current(self):
        return self._widget.currentIndex()

    def scroll_forward(self):
        self._set_page((self._current + 1) % len(CAMERA_PAGES))

    def scroll_backward(self):
        self._set_page((self._current - 1) % len(CAMERA_PAGES))

    def flip_zed_rear(self):
        self._set_page(1 if self._current == 0 else 0)

    def _set_page(self, index: int):
        self._widget.setCurrentIndex(index)
        name, _ = CAMERA_PAGES[index]
        print(f"[CameraScroller] → {name} (page {index})")