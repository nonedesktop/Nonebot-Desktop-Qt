from typing import Optional, Union, TYPE_CHECKING

from qfluentwidgets import drawIcon, FluentIconBase
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QPainter, QDesktopServices
from PySide6.QtWidgets import QWidget


if TYPE_CHECKING:
    from PySide6.QtGui import QPaintEvent, QMouseEvent


class UrlIconWidget(QWidget):
    def __init__(self, icon: Union[str, QIcon, FluentIconBase], url: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        self.url = QUrl(url)
        self.icon = icon
        self.update()
        self.url = QUrl(url)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _onMouseRelease(self):
        if self.url.isValid:
            QDesktopServices.openUrl(self.url)

    def get_icon(self) -> QIcon:
        if isinstance(self._icon, str):
            return QIcon(self._icon)

        if isinstance(self._icon, FluentIconBase):
            return self._icon.icon()

        return self._icon

    def set_icon(self, icon: Union[str, QIcon, FluentIconBase]) -> None:
        self._icon = icon
        self.update()

    def mouseReleaseEvent(self, event: "QMouseEvent") -> None:
        self._onMouseRelease()

    def paintEvent(self, event: "QPaintEvent") -> None:
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        drawIcon(self.icon, painter, self.rect())
