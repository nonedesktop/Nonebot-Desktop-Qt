from PySide6.QtWidgets import QHBoxLayout, QStackedWidget, QWidget
from qframelesswindow import FramelessWindow
from qfluentwidgets import NavigationInterface, NavigationItemPosition


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self._init_windows_size()
        self._init_navigation_interface()
        self._init_stacked_widget()
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

    def _init_navigation_interface(self):
        self.navigation_interface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True
        )

        # TODO add subinterface
        # TODO add custom widget to bottom

        # TODO add separator for design needs
        # self.navigationInterface.addSeparator()

        # TODO set the default route key a.k.a index or home page : )
        # qrouter.setDefaultRouteKey()

    def _init_stacked_widget(self):
        self.stacked_widget = QStackedWidget(self)

    def _add_sub_interface(
        self, interface: QWidget, icon, text: str, position=NavigationItemPosition.TOP
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
