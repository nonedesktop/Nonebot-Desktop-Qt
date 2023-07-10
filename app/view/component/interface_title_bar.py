from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from .label import InterfaceTitle, InterfaceDesc


class InterfaceTitleBar(QWidget):
    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_lable = InterfaceTitle(title, self)
        self.subtitle_lable = InterfaceDesc(subtitle, self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setFixedHeight(120)

    def __init_layout(self):
        self.setContentsMargins(36, 28, 36, 12)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.addWidget(self.title_lable)
        self.layout_manager.addWidget(self.subtitle_lable)
