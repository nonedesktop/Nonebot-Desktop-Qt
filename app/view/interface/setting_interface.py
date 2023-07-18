from qfluentwidgets import (
    ScrollArea,
    ExpandLayout,
    SettingCardGroup,
    PrimaryPushSettingCard,
    OptionsSettingCard,
    ComboBoxSettingCard,
    SwitchSettingCard,
)
from qfluentwidgets import FluentIcon as FI
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox

from core import StyleSheet
from config import Config


class SettingInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Instantiating widgets
        self.view_container = QWidget()
        self.appearance_setting_group = SettingCardGroup("外观和行为", self)
        self.theme_setting_card = OptionsSettingCard(
            Config.themeMode, FI.BRUSH, "主题模式", "选择你的主题模式", ["浅色", "深色", "跟随系统"], self.appearance_setting_group
        )
        self.language_setting_card = ComboBoxSettingCard(
            Config.language,
            FI.LANGUAGE,
            "语言",
            "选择你的语言",
            ["简体中文", "繁体中文", "English", "跟随系统"],
            self.appearance_setting_group,
        )
        self.auto_update_setting_card = SwitchSettingCard(
            FI.UPDATE, "自动检查更新", "在启动时自动检查更新", Config.is_auto_update, self.appearance_setting_group
        )
        self.about_setting_group = SettingCardGroup("关于", self)
        self.feedback_card = PrimaryPushSettingCard(
            "反馈", FI.FEEDBACK, "反馈", "发现了BUG？想添加新功能？请告诉我们！", self.about_setting_group
        )
        self.about_card = PrimaryPushSettingCard("关于", FI.INFO, "关于", "关于本程序", self.about_setting_group)
        self.about_qt_card = PrimaryPushSettingCard("关于 Qt", FI.INFO, "关于 Qt", "Qt 的许可证和授权自述", self.about_setting_group)
        # Instantiating layouts
        self.view_container_layout_mannager = ExpandLayout(self.view_container)
        # Initialize self widget & layout
        self.__init_widget()
        self.__init_sub_widget()
        self.__init_layout()
        self.__init_sub_widget_layout()
        # Initialize slot connection
        self.__init_signal_connection()

    def __init_widget(self):
        self.setObjectName("SettingInterface")
        self.view_container.setObjectName("SettingInterfaceViewContainer")
        self.setWidget(self.view_container)
        self.setWidgetResizable(True)
        StyleSheet.SETTING_INTERFACE.apply(self)

    def __init_sub_widget(self):
        pass

    def __init_layout(self):
        self.view_container_layout_mannager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view_container_layout_mannager.setContentsMargins(36, 20, 36, 12)
        self.view_container_layout_mannager.addWidget(self.appearance_setting_group)
        self.view_container_layout_mannager.addWidget(self.about_setting_group)

    def __init_sub_widget_layout(self):
        self.appearance_setting_group.addSettingCards(
            [self.theme_setting_card, self.language_setting_card, self.auto_update_setting_card]
        )
        self.about_setting_group.addSettingCards([self.feedback_card, self.about_card, self.about_qt_card])

    def __init_signal_connection(self):
        self.feedback_card.clicked.connect(lambda: QMessageBox.information(self, "QDesktopService", "这里打开浏览器ISSUE"))
        self.about_qt_card.clicked.connect(lambda: QMessageBox.aboutQt(self, "关于 Qt"))
