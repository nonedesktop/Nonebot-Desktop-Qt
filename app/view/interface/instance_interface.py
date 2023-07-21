from qfluentwidgets import ScrollArea, PrimaryPushButton
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel

from core.style import StyleSheet
from view.component import InterfaceTitleBar, InstanceCard


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
        # 

    def __init_layout(self):
        # Set layout options
        # Place layout widgets
        # self.setFixedHeight(100)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.addLayout(self.header_bar_layout_mannager)

    def __init_sub_widget_layout(self):
        self.header_bar_layout_mannager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.header_bar_layout_mannager.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_bar_layout_mannager.addWidget(self.new_instance_button, alignment=Qt.AlignmentFlag.AlignRight)

    def add_instance_card(self, instance_name: str, instance_id: str, driver_name: str, adapter_name: str) -> None:
        """将实例卡片添加到实例布局中
        参数:
            instance_name: 实例的名称
            instance_id: 实例的唯一标识ID
            driver_name: 实例所使用的驱动名称
            adapter_name: 实例所使用的适配器名称
        用法:
            实例的唯一ID应当是自动生成的,后续用作导航等,
            最佳实践应当是在非GUI线程内进行调用,否则可能会造成GUI线程绘制阻塞,
            因此需要将此函数注册到控制器中,再交由线程管理器移交到工作线程处理.
        """
        # TODO Use Emun with driver and adapter
        card = InstanceCard(instance_name, instance_id, driver_name, adapter_name, self)
        self.layout_manager.addWidget(card)


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
        # Temporary
        self.load_instance_card()

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

    def __init_layout(self):
        self.setWidget(self.view_container)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.addWidget(self.title_bar)
        self.view_container_layout_manager.addSpacing(4)
        self.view_container_layout_manager.addWidget(self.instance_card_view)

    def load_instance_card(self):
        """Attention!!!
        Here this is a temporary method for design and layout purposes,
        we should never do this kind of thing inside the UI thread,
        it can have serious consequences.
        """
        self.instance_card_view.add_instance_card("Untitled Instance", "0XA", "FastAPI", "OneBot V11")
        self.instance_card_view.add_instance_card("Github Bot", "0XB", "FastAPI", "Github")
        self.instance_card_view.layout_manager.addStretch(1)
