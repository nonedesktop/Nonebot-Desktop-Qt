from qfluentwidgets import SplitFluentWindow, NavigationItemPosition

from view.interface import InterfaceTemplates


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
        self.setting_interface = InterfaceTemplates("SettingInterface", "设置子界面", self)

    def __initNavigation(self):
        # set top menu
        self.addSubInterface(self.home_interface, None, "DashBoard")
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.market_interface, None, "Extension Market")
        # set bottom menu
        self.addSubInterface(self.setting_interface, None, "Settings", NavigationItemPosition.BOTTOM)

    def __initWindow(self):
        self.setWindowTitle('Nonebot-Desktop-Qt')