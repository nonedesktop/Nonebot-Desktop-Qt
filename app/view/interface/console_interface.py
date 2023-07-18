from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import TextEdit

from view.component import InterfaceTitleBar


class ConsoleLogView(TextEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Initialize self widget & layout
        self.__init_widget()
        # TODO 添加日志的实际方法和设计日志的样式

    def __init_widget(self):
        self.setReadOnly(True)


class ConsoleInterface(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_bar = InterfaceTitleBar("Console Log", "Check the log output of all instances", self)
        self.console_log_view = ConsoleLogView(self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setObjectName("ConsoleInterface")

    def __init_layout(self):
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.setContentsMargins(36, 20, 36, 12)
        self.layout_manager.addWidget(self.title_bar)
        self.layout_manager.setSpacing(4)
        self.layout_manager.addWidget(self.console_log_view)
