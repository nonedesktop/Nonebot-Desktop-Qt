from typing import Optional

from qfluentwidgets import ScrollArea
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from core import StyleSheet
from view.component import InterfaceTitleBar


class DashBoardInterface(ScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar("看板", "Overview All Instance Status Once At All.")
        # Instantiating Layout Objects
        self.view_container_layout_manager = QVBoxLayout(self)
        # Initialize Widgets & Layouts
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set Object Name
        self.setObjectName("DashBoardInterface")
        # Set Widget & Geometry
        self.setWidget(self.view_container)
        # Set Widget Options
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # Apply stylesheet
        StyleSheet.DASHBOARD_INTERFACE.apply(self)

    def __init_sub_widget(self):
        self.view_container.setObjectName("DashBoardInterfaceViewContainer")

    def __init_layout(self) -> None:
        # Set Layout Options
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.view_container_layout_manager.addWidget(self.title_bar)
