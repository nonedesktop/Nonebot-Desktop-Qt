from PySide6.QtWidgets import QHBoxLayout
from qframelesswindow import FramelessWindow
from qfluentwidgets import NavigationInterface


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self._init_windows_size()
        self._init_navigation_interface()
        self._init_layout()

    def _init_windows_size(self):
        self.resize(900, 700)
        # self.setMaximumSize()
        # self.setMinimumSize()
        ## Error raised as no arguments, fill args before uncommenting.

    def _init_layout(self):
        self.h_box_layout = QHBoxLayout(self)
        self.h_box_layout.setSpacing(0)
        self.h_box_layout.setContentsMargins(0, 0, 0, 0)
        # TODO add addWidget
        self.h_box_layout.addWidget(self.navigationInterface)

    def _init_navigation_interface(self):
        self.navigationInterface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True
        )

        # TODO add subinterface
        # TODO add custom widget to bottom

        # TODO add separator for design needs
        # self.navigationInterface.addSeparator()

        # TODO set the default route key a.k.a index or home page : )
        # qrouter.setDefaultRouteKey()
