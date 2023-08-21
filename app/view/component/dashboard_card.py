from typing import Optional, TYPE_CHECKING

from qfluentwidgets import SimpleCardWidget
from PySide6.QtCore import Signal, QTimer, Property

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class DashBoardCardBase(SimpleCardWidget):
    dataUpdated = Signal()

    def __init__(self, update_interval_mesc: int = 1000, parent: Optional["QWidget"] = None) -> None:
        super().__init__(parent=parent)
        self.update_interval: int = update_interval_mesc
        self.timer = QTimer(self)
        self._setup_timer()

    def _setup_timer(self) -> None:
        self.timer.setInterval(self.update_interval)
        self.timer.timeout.connect(self.render_data)

    def set_update_interval(self, update_interval_mesc: int) -> None:
        self.update_interval = update_interval_mesc

    def get_update_interval(self) -> int:
        return self.update_interval

    def render_data(self) -> None:
        raise NotImplementedError()

    def fetch_data(self) -> None:
        raise NotImplementedError()

    def update_data(self) -> None:
        # 派生类调用 self.dataUpdated.emit() 进行通知
        raise NotImplementedError()

    update_interval_mesc = Property(type=int, fget=get_update_interval, fset=set_update_interval)
