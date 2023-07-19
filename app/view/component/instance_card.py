from qfluentwidgets import CardWidget, IconWidget
from qfluentwidgets import FluentIcon as FI
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout


class InstanceCard(CardWidget):
    def __init__(self, instance_name: str, instance_id: str, driver_name: str, adapter_name: str, parent=None) -> None:
        super().__init__(parent=parent)
        # Instantiating Data Structures
        # Instantiating Widget Objects
        self.instance_name_label = QLabel(instance_name, self)
        self.instance_status_icon = IconWidget(FI.FLAG, self)  # 挑选一个简单的圆点图标用不同颜色来表示实例的运行状态
        self.instance_id_label = QLabel(instance_id, self)
        self.instance_id_icon = IconWidget(FI.FINGERPRINT, self)
        self.driver_name_label = QLabel(driver_name, self)
        self.driver_icon = IconWidget(FI.CALORIES, self)
        self.adapter_name_label = QLabel(adapter_name, self)
        self.adapter_icon = IconWidget(FI.AIRPLANE, self)
        # TODO Add Butoon Or Other Widgets
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
        pass

    def __init_sub_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        pass

    def __init_layout(self) -> None:
        # Set Layout Options
        self.setFixedHeight(100)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Place layout widgets
        self.layout_manager.addLayout(self.header_bar_layout_manager)
        self.layout_manager.addLayout(self.info_bar_layout_manager)

    def __init_sub_widget_layout(self) -> None:
        # Place header bar layout widgets
        self.header_bar_layout_manager.addWidget(self.instance_name_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_bar_layout_manager.addWidget(self.instance_status_icon, alignment=Qt.AlignmentFlag.AlignRight)
        self.header_bar_layout_manager.addWidget(self.instance_name_label, alignment=Qt.AlignmentFlag.AlignRight)
        # Place info bar layout widgets
        self.info_bar_layout_manager.addWidget(self.instance_id_icon)
        self.info_bar_layout_manager.addWidget(self.instance_id_label)
        # TODO Add Space Here
        self.info_bar_layout_manager.addWidget(self.driver_icon)
        self.info_bar_layout_manager.addWidget(self.driver_name_label)
        # TODO Add Space Here
        self.info_bar_layout_manager.addWidget(self.adapter_icon)
        self.info_bar_layout_manager.addWidget(self.adapter_name_label)
        pass
