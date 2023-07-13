from qfluentwidgets import FluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FI

from view.interface import (
    InterfaceTemplates,
    MarketInterface,
    ConsoleInterface,
    SettingInterface,
)
from core.icon import MyFluentIcon as MFI


class MainWindow(FluentWindow):
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
        self.console_interface = ConsoleInterface(self)
        self.setting_interface = SettingInterface(self)

    def __initNavigation(self):
        # set top menu
        self.addSubInterface(self.home_interface, FI.HOME, "DashBoard")
        self.addSubInterface(self.market_interface, FI.APPLICATION, "Extension Market")
        # set menu separator
        self.navigationInterface.addSeparator()
        # set scroll menu
        self.addSubInterface(
            self.instance_interface,
            MFI.BOT,
            "Instance Management",
            NavigationItemPosition.SCROLL,
        )

        # set bottom menu
        self.addSubInterface(
            self.global_instance_interface,
            MFI.BOTSPARKLE,
            "Global Instance Selection",
            NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(self.console_interface, FI.PRINT, "Console", NavigationItemPosition.BOTTOM)
        self.addSubInterface(
            self.setting_interface,
            FI.SETTING,
            "Settings",
            NavigationItemPosition.BOTTOM,
        )

    def __initWindow(self):
        self.setWindowTitle("Nonebot-Desktop-Qt")
