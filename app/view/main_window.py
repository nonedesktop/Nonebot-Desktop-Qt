from qfluentwidgets import SplitFluentWindow

from view.interface.interface_templates import InterfaceTemplates


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.__createSubInterface()
        self.__initNavigation()
        self.__initWindow()

    def __createSubInterface(self):
        self.home_interface = InterfaceTemplates("HomeInterface", "看板子界面", self)
        self.market_interface = InterfaceTemplates("MarketInterface", "扩展商店子界面", self)

    def __initNavigation(self):
        self.addSubInterface(self.home_interface, None, "DashBoard")
        self.addSubInterface(self.market_interface, None, "Extension Market")

    def __initWindow(self):
        pass
