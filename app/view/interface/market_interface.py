from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout
from qfluentwidgets import (
    ScrollArea,
    SmoothScrollArea,
    FlowLayout,
    SearchLineEdit,
    PillPushButton,
    FluentIcon,
)

from core import StyleSheet
from view.component import InterfaceTitleBar, ExtensionCard


class ExtensionCardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.search_line_edit = SearchLineEdit(self)
        self.plugin_label_button = PillPushButton("插件", self, FluentIcon.TAG)
        self.adapter_label_button = PillPushButton("适配器", self, FluentIcon.TAG)
        self.certified_extensions_label_button = PillPushButton(
            "官方认证", self, FluentIcon.TAG
        )
        self.card_view_container = SmoothScrollArea(self)
        self.card_view_content = QWidget(self.card_view_container)
        self.command_bar_container = QFrame(self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.card_view_content_layout_manager = FlowLayout(
            self.card_view_content, True, True
        )
        self.command_bar_container_layout_manager = QHBoxLayout(self.command_bar_container)
        # Instantiating data and data structures
        self.extension_cards: list[ExtensionCard] = []
        # TODO 实现一个前缀搜索树 Trie Tree
        self.__init_sub_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_sub_widget(self):
        # init search_line_edit widget
        self.search_line_edit.setPlaceholderText("搜索插件或适配器")
        self.search_line_edit.textChanged.connect(self.search_line_edit.search)
        # init card_view_container widget
        self.card_view_container.setWidget(self.card_view_content)
        self.card_view_container.setWidgetResizable(True)
        self.card_view_container.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

    def __init_layout(self):
        self.layout_manager.setContentsMargins(0, 0, 0, 0)
        self.layout_manager.addWidget(self.command_bar_container)
        self.layout_manager.setSpacing(10)
        self.layout_manager.addWidget(self.card_view_container)

    def __init_sub_widget_layout(self):
        # init command_bar_container widget layout
        # TODO Adjustting the layout and subwidgets size
        # self.command_bar_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.search_line_edit.setMaximumWidth(260)
        # self.plugin_label_button.setMaximumWidth(80)
        # self.adapter_label_button.setMaximumWidth(120)
        # self.certified_extensions_label_button.setMaximumWidth(120)
        self.command_bar_container_layout_manager.addWidget(self.search_line_edit)
        self.command_bar_container_layout_manager.addWidget(self.plugin_label_button)
        self.command_bar_container_layout_manager.addWidget(self.adapter_label_button)
        self.command_bar_container_layout_manager.addWidget(
            self.certified_extensions_label_button
        )
        # init card_view_container widget layout
        self.card_view_container.setViewportMargins(2, 5, 2, 5)
        # init card_view_content widget layout
        self.card_view_content_layout_manager.setVerticalSpacing
        self.card_view_content_layout_manager.setHorizontalSpacing
        self.card_view_content_layout_manager.setContentsMargins


class MarketInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar(
            "扩展商店",
            "Enjoy all the extensions from the community, with our rich ecosystem of plugins",  # noqa: E501
            self,
        )
        self.extension_card_view = ExtensionCardView(self)
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
        self.view_container.setObjectName("MarketInterfaceViewContainer")

    def __init_layout(self):
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.addWidget(self.title_bar)
        self.view_container_layout_manager.setSpacing(4)
        self.view_container_layout_manager.addWidget(self.extension_card_view)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.title_bar.resize(self.width(), self.title_bar.height())
