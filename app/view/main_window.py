from qfluentwidgets import SplitFluentWindow, NavigationItemPosition

from view.interface import InterfaceTemplates, MarketInterface, SettingInterface


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.__createSubInterface()
        self.__initNavigation()
        self.__initWindow()

    def __createSubInterface(self):
        self.home_interface = InterfaceTemplates("HomeInterface", "看板子界面", self)
        self.instance_interface = InterfaceTemplates("InstanceInterface", "实例管理子界面", self)
        self.market_interface = MarketInterface(self)
        self.global_instance_interface = InterfaceTemplates("GlobalInstanceSelection", "选择全局实例子界面", self)
        self.setting_interface = SettingInterface(self)

    def __initNavigation(self):
        # set top menu
        self.addSubInterface(self.home_interface, None, "DashBoard")
        # set menu separator
        self.navigationInterface.addSeparator()
        # set scroll menu
        self.addSubInterface(self.instance_interface, None, "Instance Management", NavigationItemPosition.SCROLL)
        self.addSubInterface(self.market_interface, None, "Extension Market", NavigationItemPosition.SCROLL)
        # set bottom menu
        self.addSubInterface(self.global_instance_interface, None, "Global Instance Selection", NavigationItemPosition.BOTTOM,)
        self.addSubInterface(self.setting_interface, None, "Settings", NavigationItemPosition.BOTTOM)

    def __initWindow(self):
        self.setWindowTitle("Nonebot-Desktop-Qt")
