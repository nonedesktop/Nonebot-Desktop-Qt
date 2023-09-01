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
from view.component import InterfaceTitleBar, FlowLayout, DisplayLabel


class MarketInterface(ScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar(
            title="🛒 扩展商店",
            subtitle="Enjoy all the extensions from the community, with our rich ecosystem",
            parent=self,
        )
        self.extension_card_view = SegmentedNavigationExtensionCardView(self)
        # Instantiating Layout Objects
        self.view_container_main_layout = QVBoxLayout(self.view_container)
        # Initialize self widget & layout
        self.__init_sub_widget__()
        self.__init_widget__()
        self.__init_layout__()

    def __init_widget__(self) -> None:
        # Setting Objects Name
        self.setObjectName("MarketInterface")
        # Setting Widget Sub Widget
        self.setWidget(self.view_container)
        # Setting Widget Options
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        # Setting Widget StyleSheet
        StyleSheet.MARKET_INTERFACE.apply(self)

    def __init_sub_widget__(self) -> None:
        # Setting Objects Name
        self.view_container.setObjectName("MarketInterfaceViewContainer")

    def __init_layout__(self) -> None:
        # Setting Layout Options
        self.view_container_main_layout.setContentsMargins(36, 20, 36, 12)
        self.view_container_main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Arranging Widgets & Layouts
        self.view_container_main_layout.addWidget(self.title_bar)
        self.view_container_main_layout.setSpacing(4)
        self.view_container_main_layout.addWidget(self.extension_card_view)


class SegmentedNavigationExtensionCardView(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Initializing Data Bindings and Objects
        # Instantiating Widget Objects
        self.pivot = SegmentedWidget(self)
        self.command_bar = CommandBar(self)
        self.stacked_container = QStackedWidget(self)
        self.driver_card_view = PluginCardView(self)
        self.adapter_card_view = PluginCardView(self)
        self.plugin_card_view = PluginCardView(self)
        self.robot_card_view = RobotCardView(self)
        # Instantiating Layout Objects
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_sub_widget__()
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        pass

    def __init_sub_widget__(self) -> None:
        # Setting Objects Name
        self.driver_card_view.setObjectName("DriverCardView")
        self.adapter_card_view.setObjectName("DdapterCardView")
        self.plugin_card_view.setObjectName("PluginCardView")
        self.robot_card_view.setObjectName("RobotCardView")
        # Setting Widget Sub Widget
        self.stacked_container.addWidget(self.plugin_card_view)
        self.pivot.addItem(
            self.plugin_card_view.objectName(),
            "插件",
            lambda: self.stacked_container.setCurrentWidget(self.plugin_card_view),
        )
        self.stacked_container.addWidget(self.adapter_card_view)
        self.pivot.addItem(
            self.adapter_card_view.objectName(),
            "适配器",
            lambda: self.stacked_container.setCurrentWidget(self.adapter_card_view),
        )
        self.stacked_container.addWidget(self.driver_card_view)
        self.pivot.addItem(
            self.driver_card_view.objectName(),
            "驱动器",
            lambda: self.stacked_container.setCurrentWidget(self.driver_card_view),
        )
        self.stacked_container.addWidget(self.robot_card_view)
        self.pivot.addItem(
            self.robot_card_view.objectName(),
            "机器人",
            lambda: self.stacked_container.setCurrentWidget(self.robot_card_view),
        )
        # Setting Widget Options
        self.stacked_container.setCurrentWidget(self.plugin_card_view)
        self.pivot.setCurrentItem(self.plugin_card_view.objectName())
        # Initialize Signal Connections
        self.stacked_container.currentChanged.connect(self.onCurrentIndexChanged)  # type: ignore

    def __init_layout(self) -> None:
        # Place layout widgets
        self.layout_manager.addWidget(self.pivot)
        self.layout_manager.addWidget(self.command_bar)
        self.layout_manager.addWidget(self.stacked_container)

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


class RobotCardView(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.text_label = DisplayLabel("🚧 施工中...", self)
        # Instantiating Layout Objects
        self.main_layout = QVBoxLayout(self)
        # Initializing Widget & Layout
        self.__init_layout__()

    def __init_layout__(self) -> None:
        # Setting Layout Options
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # Arranging Widgets
        self.main_layout.addWidget(self.text_label)


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
        self.search_line_edit.setFixedWidth(320)
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
