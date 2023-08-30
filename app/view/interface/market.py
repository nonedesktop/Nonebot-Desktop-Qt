from typing import Optional

from qfluentwidgets import (
    ScrollArea,
    SegmentedWidget,
    SmoothScrollArea,
    SearchLineEdit,
    PillPushButton,
    TransparentDropDownPushButton,
    FluentIcon as FI,
)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QStackedWidget

from core import StyleSheet
from view.component import InterfaceTitleBar, ExtensionCard, FlowLayout


class MarketInterface(ScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar(
            title="🛒 扩展商店",
            subtitle="Enjoy all the extensions from the community, with our rich ecosystem",
            parent=self,
        )
        self.extension_card_view = SegmentedNavigationView(self)
        # Instantiating layouts
        self.view_container_layout_manager = QVBoxLayout(self.view_container)
        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        self.setObjectName("MarketInterface")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        StyleSheet.MARKET_INTERFACE.apply(self)

    def __init_sub_widget(self):
        self.view_container.setObjectName("MarketInterfaceViewContainer")

    def __init_layout(self):
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.addWidget(self.title_bar)
        self.view_container_layout_manager.setSpacing(4)
        self.view_container_layout_manager.addWidget(self.extension_card_view)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.title_bar.resize(self.width(), self.title_bar.height())


class ExtensionCardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.command_bar = CommandBar(self)
        self.card_view_container = SmoothScrollArea(self)
        self.card_view_content = QWidget()
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.card_view_content_layout_manager = FlowLayout(self.card_view_content, True, True)
        # Instantiating data and data structures
        self.extension_cards: list[ExtensionCard] = []
        # TODO 实现一个前缀搜索树 Trie Tree
        self.__init_sub_widget()
        self.__init_layout()

    def __init_sub_widget(self):
        # init search_line_edit widget
        # init card_view_container widget
        self.card_view_container.setWidget(self.card_view_content)
        self.card_view_container.setWidgetResizable(True)
        self.card_view_container.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def __init_layout(self):
        self.layout_manager.addWidget(self.command_bar)
        self.layout_manager.addWidget(self.card_view_container)


class SegmentedNavigationView(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.pivot = SegmentedWidget(self)
        self.command_bar = CommandBar(self)
        self.stacked_container = QStackedWidget(self)
        self.driver_card_view = PluginCardView(self)
        self.adapter_card_view = PluginCardView(self)
        self.plugin_card_view = PluginCardView(self)
        self.robot_card_view = PluginCardView(self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        self.__add_sub_interface(self.driver_card_view, "DriverCardView", "驱动器")
        self.__add_sub_interface(self.adapter_card_view, "AdapterCardView", "适配器")
        self.__add_sub_interface(self.plugin_card_view, "PluginCardView", "插件")
        self.__add_sub_interface(self.robot_card_view, "RobotCardView", "机器人")
        self.stacked_container.currentChanged.connect(self.onCurrentIndexChanged)  # type: ignore
        self.stacked_container.setCurrentWidget(self.adapter_card_view)
        self.pivot.setCurrentItem(self.adapter_card_view.objectName())

    def __init_layout(self) -> None:
        # Place layout widgets
        self.layout_manager.addWidget(self.pivot)
        self.layout_manager.addWidget(self.command_bar)
        self.layout_manager.addWidget(self.stacked_container)

    def __add_sub_interface(self, widget: QWidget, objectName: str, text: str) -> None:
        widget.setObjectName(objectName)
        self.stacked_container.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stacked_container.setCurrentWidget(widget),
        )

    def onCurrentIndexChanged(self, index) -> None:
        widget: QWidget = self.stacked_container.widget(index)
        self.pivot.setCurrentItem(widget.objectName())


class PluginCardView(SmoothScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_content = QWidget()
        # Instantiating layouts
        self.view_content_layout_manager = FlowLayout(self.view_content, True, True)
        # Initialize self widget & layout
        self.__init_widget()

    def __init_widget(self) -> None:
        self.setWidget(self.view_content)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


class CommandBar(QFrame):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.search_line_edit = SearchLineEdit(self)
        self.plugin_label_button = PillPushButton("插件", self, FI.TAG)
        self.adapter_label_button = PillPushButton("适配器", self, FI.TAG)
        self.certified_extensions_label_button = PillPushButton("官方认证", self, FI.TAG)
        self.sort_filter_button = TransparentDropDownPushButton("排序和筛选", self, FI.SCROLL)
        # Instantiating Layout Objects
        self.layout_manager = QHBoxLayout(self)
        # Initialize Widgets & Layouts
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        self.search_line_edit.setFixedWidth(280)
        self.search_line_edit.setPlaceholderText("搜索插件或适配器")
        self.search_line_edit.textChanged.connect(self.search_line_edit.search)  # type: ignore

    def __init_layout(self) -> None:
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Place Widgets To Layout
        self.layout_manager.addWidget(self.search_line_edit)
        self.layout_manager.addWidget(self.plugin_label_button)
        self.layout_manager.addWidget(self.adapter_label_button)
        self.layout_manager.addWidget(self.certified_extensions_label_button)
        self.layout_manager.addStretch(1)
        self.layout_manager.addWidget(self.sort_filter_button)
