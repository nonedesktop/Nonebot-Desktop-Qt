from qfluentwidgets import ScrollArea, PrimaryPushButton
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

from view.component import InterfaceTitleBar
from core.style import StyleSheet


class InstanceCardView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_label = QLabel("实例总览", self)
        self.new_instance_button = PrimaryPushButton("新的实例", self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.header_bar_layout_mannager = QHBoxLayout()
        # Initialize self widget & layout
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_layout(self):
        # Set layout options
        # Place layout widgets
        self.setFixedHeight(100)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.addLayout(self.header_bar_layout_mannager)

    def __init_sub_widget_layout(self):
        self.header_bar_layout_mannager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.header_bar_layout_mannager.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_bar_layout_mannager.addWidget(self.new_instance_button, alignment=Qt.AlignmentFlag.AlignRight)


class InstanceInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar("实例管理", "Manage all you instances right on one place", self)
        self.instance_card_view = InstanceCardView(self)
        # Instantiating layouts
        self.view_container_layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self):
        # Set widgets object name
        self.setObjectName("InstanceInterface")
        # Set widgets options
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # Apply stylesheet
        StyleSheet.INSTANCE_INTERFACE.apply(self)

    def __init_sub_widget(self):
        self.view_container.setObjectName("InstanceInterfaceViewContainer")
        self.title_bar.setObjectName("InstanceInterfaceTitleBar")

    def __init_layout(self):
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.addWidget(self.title_bar)
        self.view_container_layout_manager.addSpacing(4)
        self.view_container_layout_manager.addWidget(self.instance_card_view)
