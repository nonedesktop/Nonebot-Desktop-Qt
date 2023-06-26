from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout
from qfluentwidgets import SubtitleLabel, setFont


class InterfaceTemplates(QFrame):
    def __init__(self, obj_name: str, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(obj_name)
        self.sub_title = SubtitleLabel(text, self)
        self.layout_manager = QHBoxLayout(self)
        setFont(self.sub_title, 24)
        self.sub_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.addWidget(self.sub_title, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.setContentsMargins(0, 32, 0, 0)
