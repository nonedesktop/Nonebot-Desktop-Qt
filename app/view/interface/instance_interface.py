from typing import Optional

from qfluentwidgets import SmoothScrollArea, PrimaryPushButton, RoundMenu, Action, ElevatedCardWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QSizePolicy,
)

from model import InstanceMetadata
from core import StyleSheet, MyFluentIcon as MFI, signal_bus
from view.component import (
    InterfaceTitleBar,
    InstanceCard,
    BodyLabel,
    BodyStrongLabel,
    BodyStrongLargeLabel,
)


class InstancePerformanceView(ElevatedCardWidget):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_label = BodyStrongLargeLabel("🚀 性能监控", self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        pass

    def __init_layout(self) -> None:
        self.layout_manager.setContentsMargins(18, 16, 18, 12)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_manager.addWidget(self.title_label)

    def __init_sub_layout(self) -> None:
        pass


class InstanceDetailView(ElevatedCardWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_label = BodyStrongLargeLabel("🔍 实例详情", self)
        self.id_label = BodyStrongLabel("INSTANCE ID", self)
        self.id_field_label = BodyLabel("", self)
        self.name_label = BodyStrongLabel("INSTANCE NAME", self)
        self.name_field_label = BodyLabel("", self)
        self.path_label = BodyStrongLabel("INSTANCE PATH")
        self.path_field_label = BodyLabel("", self)
        self.driver_label = BodyStrongLabel("DRIVER", self)
        self.driver_field_label = BodyLabel("DRIVER", self)
        self.adapter_label = BodyStrongLabel("ADAPTER", self)
        self.adapter_field_label = BodyLabel("", self)
        self.plugin_list = BodyStrongLabel("PLUGIN LIST", self)
        self.plugin_field_list = BodyLabel("", self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.form_layout_manager = QFormLayout()
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set Object Name
        self.setObjectName("InstanceDetailView")

    def __init_layout(self) -> None:
        # Set Option & Policy
        self.layout_manager.setContentsMargins(18, 16, 18, 12)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.layout_manager.addWidget(self.title_label)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(self.form_layout_manager)

    def __init_sub_layout(self) -> None:
        # Set Option & Policy
        self.form_layout_manager.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.form_layout_manager.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.form_layout_manager.setHorizontalSpacing(50)
        # Place layout widgets
        # TODO Just for Design should consider all later
        self.form_layout_manager.addRow(self.id_label, self.id_field_label)
        self.form_layout_manager.addRow(self.name_label, self.name_field_label)
        self.form_layout_manager.addRow(self.path_label, self.path_field_label)
        self.form_layout_manager.addRow(self.driver_label, self.driver_field_label)
        self.form_layout_manager.addRow(self.adapter_label, self.adapter_field_label)
        self.form_layout_manager.addRow(self.plugin_list, self.plugin_field_list)

    def show_detail(self, metadata: InstanceMetadata) -> None:
        self.id_field_label.setText(metadata.id)
        self.name_field_label.setText(metadata.name)
        self.path_field_label.setText(metadata.path)
        self.driver_field_label.setText(metadata.driver)
        self.adapter_field_label.setText(metadata.adapter)
        # TODO plugin list


class InstanceCardView(QFrame):
    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.title_label = BodyStrongLargeLabel("👁️ 实例总览", self)
        self.new_instance_button = PrimaryPushButton("新的实例", self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.header_bar_layout_manager = QHBoxLayout()
        self.instance_card_container_layout_manager = QVBoxLayout()
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set Object Name
        self.setObjectName("InstanceCardView")
        # Set Widget Option & Policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        # Set Geometry & Widget
        # Apply stylesheet
        # TODO This is just for design should move this to qss file later
        self.setStyleSheet(
            "#InstanceCardView {background-color: rgb(242, 242, 242);border: 1px solid rgba(0, 0, 0, 0.0578);border-radius: 6px}"
        )  # noqa: E501

    def __init_layout(self) -> None:
        # Set Widget Option & Policy
        # Set layout options
        self.layout_manager.setContentsMargins(18, 12, 18, 12)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.layout_manager.addLayout(self.header_bar_layout_manager)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(self.instance_card_container_layout_manager)

    def __init_sub_widget_layout(self) -> None:
        # Set layout options
        self.instance_card_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.header_bar_layout_manager.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_bar_layout_manager.addWidget(self.new_instance_button, alignment=Qt.AlignmentFlag.AlignRight)

    def add_instance_card(self, instance_metadata: InstanceMetadata) -> None:
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
        card = InstanceCard(instance_metadata, self)
        self.instance_card_container_layout_manager.addWidget(card)


class InstanceInterface(SmoothScrollArea):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar("🔌 实例管理", "Manage all you instances right on one place", self)
        self.card_view = InstanceCardView(self)
        self.detail_view = InstanceDetailView(self)
        self.performance_view = InstancePerformanceView(self)
        # Instantiating layouts
        self.view_container_layout_manager = QVBoxLayout(self.view_container)
        self.detail_layout_manager = QHBoxLayout()
        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_layout()
        self.__init_layout()
        # Initialize signal connection
        self.__init_signal_connection()
        # Temporary
        self.load_instance_card()

    def __init_widget(self) -> None:
        # Set widgets object name
        self.setObjectName("InstanceInterface")
        # Set widgets options
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        # Set Geometry & Widget
        self.setWidget(self.view_container)
        # Apply stylesheet
        StyleSheet.INSTANCE_INTERFACE.apply(self)

    def __init_sub_widget(self) -> None:
        self.view_container.setObjectName("InstanceInterfaceViewContainer")

    def __init_layout(self) -> None:
        # Set Layout Options
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.view_container_layout_manager.addWidget(self.title_bar)
        self.view_container_layout_manager.addSpacing(4)
        self.view_container_layout_manager.addWidget(self.card_view)
        self.view_container_layout_manager.addSpacing(5)
        self.view_container_layout_manager.addLayout(self.detail_layout_manager)
        self.view_container_layout_manager.addStretch(1)

    def __init_sub_layout(self) -> None:
        self.detail_layout_manager.addWidget(self.detail_view)
        self.detail_layout_manager.addWidget(self.performance_view)

    def __init_signal_connection(self) -> None:
        self.card_view.new_instance_button.clicked.connect(self.__show_new_instance_menu)  # type: ignore
        signal_bus.InstanceCardClicked.connect(self.detail_view.show_detail)

    def __show_new_instance_menu(self) -> None:
        menu = RoundMenu(parent=self)
        menu.addAction(Action(MFI.BOT, "新建本地实例", self))
        menu.addAction(Action(MFI.BOT, "托管本地实例", self))
        menu.addAction(Action(MFI.BOT, "新建远程实例", self))
        menu.addAction(Action(MFI.BOT, "托管远程实例", self))
        x: int = (self.card_view.new_instance_button.width() - menu.sizeHint().width()) // 2 + 10
        pos: QPoint = self.card_view.new_instance_button.mapToGlobal(
            QPoint(x, self.card_view.new_instance_button.height())
        )
        menu.exec(pos)

    def load_instance_card(self) -> None:
        """Attention!!!
        Here this is a temporary method for design and layout purposes,
        we should never do this kind of thing inside the UI thread,
        it can have serious consequences.
        """
        _ = [""]
        a = InstanceMetadata("0XA", "Untitled Instance", "", "FastAPI", "Red", _)
        b = InstanceMetadata("0XB", "QQ Bot", "", "FastAPI", "OneBot V11", _)
        c = InstanceMetadata("0XC", "Cai Bot", "", "FastAPI", "Github", _)
        d = InstanceMetadata("0XD", "YunZai Bot", "", "FastAPI", "OneBot V11", _)
        e = InstanceMetadata("0XE", "Telegram Bot", "", "FastAPI", "Telegram", _)
        self.card_view.add_instance_card(a)
        self.card_view.add_instance_card(b)
        self.card_view.add_instance_card(c)
        self.card_view.add_instance_card(d)
        self.card_view.add_instance_card(e)
