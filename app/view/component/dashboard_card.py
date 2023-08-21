from typing import Optional, TYPE_CHECKING

from qfluentwidgets import SimpleCardWidget
from PySide6.QtCore import Signal, QTimer

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class DashBoardCardBase(SimpleCardWidget):
    dataUpdated = Signal()

    def __init__(self, update_interval_mesc: int = 1000, parent: Optional["QWidget"] = None) -> None:
        super().__init__(parent=parent)
        self.timer = QTimer(self)
        self.timer.setInterval(update_interval_mesc)
        self.timer.timeout.connect(self.render_data)

    def render_data(self) -> None:
        raise NotImplementedError()

    def fetch_data(self) -> None:
        raise NotImplementedError()
