from qfluentwidgets import ScrollArea
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from view.component import InterfaceTitleBar


class InstanceInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar("实例管理", "Manage all you instances right on one place", self)
        # Instantiating layouts
        self.view_container_layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setObjectName("InstanceInterface")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

    def __init_layout(self):
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.addWidget(self.title_bar)
