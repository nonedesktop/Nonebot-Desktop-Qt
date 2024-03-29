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
from model import PluginMetadata
from view.component import InterfaceTitleBar, FlowLayout, DisplayLabel, ExtensionCard


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
        self.extension_card_view.load_plugin_card()
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
        self.plugin_card_view = PluginCardView(self)
        self.adapter_card_view = PluginCardView(self)
        self.driver_card_view = DriverCardview(self)
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
        self.stacked_container.currentChanged.connect(self.onCurrentIndexChanged)

    def __init_layout(self) -> None:
        # Place layout widgets
        self.layout_manager.addWidget(self.pivot)
        self.layout_manager.addWidget(self.command_bar)
        self.layout_manager.addWidget(self.stacked_container)

    def onCurrentIndexChanged(self, index) -> None:
        widget: QWidget = self.stacked_container.widget(index)
        self.pivot.setCurrentItem(widget.objectName())

    def load_plugin_card(self) -> None:
        # Just for mocking and test
        # should remove this later
        _ = []
        a = PluginMetadata(
            "nonebot_plugin_status",
            "nonebot-plugin-status",
            "服务器状态查看",
            "通过戳一戳获取服务器状态",
            "yanyongyu",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            _,
            True,
            None,
            _,
            True,
            "2023-06-26T21:53:28.908452+08:00",  # type: ignore
        )
        for _ in range(10):
            self.plugin_card_view.add_card(a)


class PluginCardView(SmoothScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_content = QWidget()
        # Instantiating layouts
        self.view_content_layout_manager = FlowLayout(self.view_content, True)
        # Initialize self widget & layout
        self.__init_widget()

    def __init_widget(self) -> None:
        self.setWidget(self.view_content)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 5, 0, 5)

    def add_card(self, metadata: PluginMetadata) -> None:
        card = ExtensionCard(metadata, self)
        self.view_content_layout_manager.addWidget(card)


class AdapterCardView(SmoothScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        # Instantiating layouts
        self.view_container_main_layout = FlowLayout(self.view_container, True, True)
        # Initialize self widget & layout
        self.__init_widget()

    def __init_widget(self) -> None:
        self.setWidget(self.view_container)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


class DriverCardview(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.text_label = DisplayLabel("🚧 施工中...", self)
        # Instantiating Layout Objects
        self.main_layout = QVBoxLayout(self)
        # Initializing Widget & Layout
        self.__init_layout()

    def __init_layout(self):
        # Setting Layout Options
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # Arranging Widgets
        self.main_layout.addWidget(self.text_label)


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
        self.main_layout = QHBoxLayout(self)
        # Initialize Widgets & Layouts
        self.__init_sub_widget__()
        self.__init_layou__()

    def __init_sub_widget__(self) -> None:
        self.search_line_edit.setPlaceholderText("搜索")
        self.search_line_edit.textChanged.connect(self.search_line_edit.search)  # type: ignore

    def __init_layou__(self) -> None:
        # Setting Layout Options
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Place Widgets To Layout
        self.main_layout.addWidget(self.search_line_edit, 3)
        self.main_layout.addWidget(self.plugin_label_button)
        self.main_layout.addWidget(self.adapter_label_button)
        self.main_layout.addWidget(self.certified_extensions_label_button)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.sort_filter_button)

    def set_search_line_edit_place_holder_text(self, text: str) -> None:
        """设置工具栏搜索框的搜索提示文字"""

        self.search_line_edit.setPlaceholderText(text)
