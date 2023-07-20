from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from .label import TitleLabel, BodyLabel


class InterfaceTitleBar(QWidget):
    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_label = TitleLabel(title, self)
        self.subtitle_label = BodyLabel(subtitle, self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setFixedHeight(90)
        self.setStyleSheet("background-color: transparent;")

    def __init_layout(self):
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.addWidget(self.title_label)
        self.layout_manager.addWidget(self.subtitle_label)
