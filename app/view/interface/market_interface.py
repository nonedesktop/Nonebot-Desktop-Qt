from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import ScrollArea

from core import StyleSheet
from view.component import InterfaceTitleBar


class MarketInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets\
        # TODO 需要微调位置来适配Title Bar
        self.title_bar = InterfaceTitleBar(
            "Extension Store",
            "Enjoy all the extensions from the community, with our rich ecosystem of plugins",
            self,
        )
        self.view_container = QWidget(self)
        # Instantiating layouts
        self.view_container_layout_manager = QVBoxLayout(self.view_container)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setObjectName("MarketInterface")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        StyleSheet.MARKET_INTERFACE.apply(self)

    def __init_sub_widget(self):
        self.view_container.setObjectName("MarketInterfaceContainerView")

    def __init_layout(self):
        # 需要微调位置来适配
        self.setViewportMargins(0, self.title_bar.height(), 0, 0)
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setSpacing(30)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.setContentsMargins(0, 0, 0, 0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.title_bar.resize(self.width(), self.title_bar.height())
