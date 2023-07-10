from qfluentwidgets import ScrollArea, ExpandLayout, SettingCardGroup, PrimaryPushSettingCard
from qfluentwidgets import FluentIcon as FI
from PySide6.QtWidgets import QLabel, QWidget


class SettingInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        # TODO Add Title Lable
        self.about_setting_group = SettingCardGroup("关于", self)
        self.about_setting_card = PrimaryPushSettingCard("关于", FI.INFO, "关于", "关于NoneBot Desktop Qt", self.about_setting_group)
        # Instantiating layouts
        self.view_container_layout_mannager = ExpandLayout(self.view_container)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_widget()
        self.__init_layout()
        self.__init_sub_widget_layout()

    def __init_widget(self):
        self.setObjectName("SettingInterface")
        self.setWidget(self.view_container)
        self.setWidgetResizable(True)

    def __init_sub_widget(self):
        pass

    def __init_layout(self):
        self.view_container_layout_mannager.setContentsMargins(36, 10, 36, 0)
        self.view_container_layout_mannager.setSpacing(28)
        self.view_container_layout_mannager.addWidget(self.about_setting_group)

    def __init_sub_widget_layout(self):
        self.about_setting_group.addSettingCard(self.about_setting_card)
