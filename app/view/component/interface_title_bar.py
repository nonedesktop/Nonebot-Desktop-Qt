from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import TitleLabel, CaptionLabel


class InterfaceTitleBar(QWidget):
    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_lable = TitleLabel(title, self)
        self.subtitle_lable = CaptionLabel(subtitle, self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setFixedHeight(100)

    def __init_layout(self):
        self.layout_manager.setSpacing(0)
        self.setContentsMargins(36, 22, 36, 12)
        self.layout_manager.addWidget(self.title_lable)
        self.layout_manager.addSpacing(4)
        self.layout_manager.addWidget(self.subtitle_lable)
        self.layout_manager.addSpacing(4)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
