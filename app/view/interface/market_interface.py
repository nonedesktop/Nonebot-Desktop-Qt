from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout
from qfluentwidgets import SubtitleLabel, setFont


class MarketInterface(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MarketInterface")
        self.sub_title = SubtitleLabel("扩展商店子界面", self)
        self.layout_manager = QHBoxLayout(self)
        setFont(self.sub_title, 24)
        self.sub_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.addWidget(self.sub_title, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.setContentsMargins(0, 32, 0, 0)
