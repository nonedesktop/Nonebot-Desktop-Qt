from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
from view.component import ExtensionCard


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        card1 = ExtensionCard(
            "nonebot_plugin_status",
            "nonebot-plugin-status",
            "服务器状态查看",
            "通过戳一戳获取服务器状态",
            "yanyongyu",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            [{"label": "t:server", "color": "#f12020"}],
            True,
            "application",
            None,
            self,
        )

        card2 = ExtensionCard(
            "nonebot-plugin-docs",
            "nonebot-plugin-docs",
            "NoneBot离线文档",
            "在本地浏览NoneBot文档",
            "nonebot",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            [{"label": "t:server", "color": "#f12020"}],
            True,
            "application",
            None,
            self,
        )

        card3 = ExtensionCard(
            "nonebot-plugin-fortune",
            "nonebot-plugin-fortune",
            "今日运势",
            "抽签！抽取你的今日运势🙏",
            "KafCoppelia",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            [{"label": "t:server", "color": "#f12020"}],
            True,
            "application",
            None,
            self,
        )

        self.layout_mannager = QVBoxLayout(self)
        self.layout_mannager.addWidget(card1)
        self.layout_mannager.addWidget(card2)
        self.layout_mannager.addWidget(card3)


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
