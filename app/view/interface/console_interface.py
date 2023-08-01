from qfluentwidgets import TextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QVBoxLayout

from view.component import InterfaceTitleBar


class ConsoleLogView(TextEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Initialize self widget & layout
        self.__init_widget()
        # TODO 添加日志的实际方法和设计日志的样式

    def __init_widget(self):
        self.setReadOnly(True)
        self.setText("Violet - NoneBot2 Desktop Application\n" "2023 NoneDesktop\n")
        self.setFont(
            [
                "Iosevka Term",
                "Sarasa Term SC",
                "Consolas",
                "Noto Sans Mono CJK SC",
                "Microsoft YaHei UI",
                "Monospace",
            ]
        )
        self.setFontPointSize(10)
        self.setFontWeight(QFont.Weight.Medium)

        # assume after loading
        self.append("就绪")
        # 'append' operation will add a new line automatically

    def contextMenuEvent(self, e):
        pass


class ConsoleInterface(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_bar = InterfaceTitleBar(
            "日志", "Check the log output of all instances", self
        )
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
