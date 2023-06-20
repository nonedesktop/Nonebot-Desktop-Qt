from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QStackedWidget, QFrame, QLabel
from qframelesswindow import FramelessWindow
from qfluentwidgets import NavigationInterface, NavigationItemPosition

from view.title_bar import CustomTitleBar


class PlaceholderComponent(QFrame):
    def __init__(self, text: str, parent):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "-"))
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.setContentsMargins(0, 32, 0, 0)


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(CustomTitleBar(self))
        self.setObjectName("MainWindow")
        self._init_windows_size()
        self._init_stacked_widget()
        self._init_sub_interface()
        self._init_navigation_interface()
        self._init_layout()

    def _init_windows_size(self):
        self.resize(900, 700)
        # self.setMaximumSize()
        # self.setMinimumSize()
        ## Error raised as no arguments, fill args before uncommenting.

    def _init_layout(self):
        self.layout_manager = QHBoxLayout(self)
        self.layout_manager.setSpacing(0)
        self.layout_manager.setContentsMargins(0, 0, 0, 0)
        # TODO add addWidget
        self.layout_manager.addWidget(self.navigation_interface)
        self.layout_manager.addWidget(self.stacked_widget)
        # self.h_box_layout.setStretchFactor(self.stacked_widget, 1)
        # raise title bar
        self.titleBar.raise_()
        self.navigation_interface.displayModeChanged.connect(self.titleBar.raise_)

    def _init_navigation_interface(self):
        self.navigation_interface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True
        )

        self._add_sub_interface(self.interface_1, None, "实例总览")
        self._add_sub_interface(self.interface_2, None, "实例详情")
        self._add_sub_interface(self.interface_3, None, "配置管理")
        self._add_sub_interface(self.interface_4, None, "插件市场")
        self._add_sub_interface(self.interface_5, None, "关于")

        # TODO add custom widget to bottom

        # TODO add separator for design needs
        # self.navigationInterface.addSeparator()

        # TODO set the default route key a.k.a index or home page : )
        # qrouter.setDefaultRouteKey()

    def _init_stacked_widget(self):
        self.stacked_widget = QStackedWidget(self)

    def _init_sub_interface(self):
        self.interface_1 = PlaceholderComponent("实例总览", self)
        self.interface_2 = PlaceholderComponent("实例详情", self)
        self.interface_3 = PlaceholderComponent("配置管理", self)
        self.interface_4 = PlaceholderComponent("插件市场", self)
        self.interface_5 = PlaceholderComponent("关于", self)

    def _add_sub_interface(
        self,
        interface: PlaceholderComponent,
        icon,
        text: str,
        position=NavigationItemPosition.TOP,
    ):
        self.stacked_widget.addWidget(interface)
        self.navigation_interface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=None,
            position=position,
            tooltip=text,
        )
