from qfluentwidgets import CardWidget, InfoBadge, DotInfoBadge, TransparentToolButton
from qfluentwidgets import FluentIcon as FI
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from .label import CaptionLabel, BodyLabel


class InstanceCard(CardWidget):
    def __init__(self, instance_name: str, instance_id: str, driver_name: str, adapter_name: str, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating Data Structures
        # Instantiating Widget Objects
        self.instance_name_label = BodyLabel(instance_name, self)
        self.instance_status_label = CaptionLabel("运行中", self)
        self.instance_status_icon = DotInfoBadge.success(self)
        self.instance_id_label = CaptionLabel(instance_id, self)
        self.instance_id_icon = InfoBadge.info("实例ID")
        self.driver_name_label = CaptionLabel(driver_name, self)
        self.driver_icon = InfoBadge.info("驱动器")
        self.adapter_name_label = CaptionLabel(adapter_name, self)
        self.adapter_icon = InfoBadge.info("适配器")
        self.more_action_button = TransparentToolButton(FI.MORE, self)
        # Instantiating Layout Objects
        self.layout_manager = QVBoxLayout(self)
        self.header_bar_layout_manager = QHBoxLayout()
        self.info_bar_layout_manager = QHBoxLayout()
        # Initialize Widgets & Layouts
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set Object Name
        self.setObjectName("InstanceCard")
        # Set Widget Option & Policy
        self.setFixedHeight(80)
        # Set Geometry

        pass

    def __init_sub_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        # Set Geometry
        self.instance_status_icon.setFixedSize(6, 6)

    def __init_layout(self) -> None:
        # Set Layout Options
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.layout_manager.addLayout(self.header_bar_layout_manager)
        self.layout_manager.addStretch(1)
        self.layout_manager.addLayout(self.info_bar_layout_manager)

    def __init_sub_widget_layout(self) -> None:
        # Set Layout Options
        # self.info_bar_layout_manager.setSizeConstraint(QHBoxLayout.SizeConstraint.SetMinimumSize)
        # Place header bar layout widgets
        self.header_bar_layout_manager.addWidget(self.instance_name_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_bar_layout_manager.addStretch(1)
        self.header_bar_layout_manager.addWidget(self.instance_status_icon, alignment=Qt.AlignmentFlag.AlignRight)
        self.header_bar_layout_manager.addWidget(self.instance_status_label, alignment=Qt.AlignmentFlag.AlignRight)
        # Place info bar layout widgets
        self.info_bar_layout_manager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.info_bar_layout_manager.addWidget(self.instance_id_icon)
        self.info_bar_layout_manager.addWidget(self.instance_id_label)
        self.info_bar_layout_manager.addSpacing(5)
        self.info_bar_layout_manager.addWidget(self.driver_icon)
        self.info_bar_layout_manager.addWidget(self.driver_name_label)
        self.info_bar_layout_manager.addSpacing(5)
        self.info_bar_layout_manager.addWidget(self.adapter_icon)
        self.info_bar_layout_manager.addWidget(self.adapter_name_label)
        self.info_bar_layout_manager.addStretch(1)
        self.info_bar_layout_manager.addWidget(self.more_action_button)
