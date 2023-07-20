from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
from view.component import ExtensionCard, InstanceCard


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
            True,
            "2023-06-26T21:53:28.908452+08:00",
            self,
        )

        card2 = ExtensionCard(
            "nonebot_plugin_docs",
            "nonebot-plugin-docs",
            "NoneBot离线文档",
            "在本地浏览NoneBot文档",
            "nonebot",
            "https://github.com/nonebot/nonebot2/tree/master/packages/nonebot-plugin-docs",
            [{"label": "t:server", "color": "#f12020"}],
            True,
            "application",
            None,
            False,
            "2023-06-26T21:54:14.646379+08:00",
            self,
        )

        card3 = ExtensionCard(
            "nonebot_plugin_fortune",
            "nonebot-plugin-fortune",
            "今日运势",
            "抽签！抽取你的今日运势🙏",
            "KafCoppelia",
            "https://github.com/MinatoAquaCrews/nonebot_plugin_fortune",
            [{"label": "t:server", "color": "#f12020"}],
            False,
            "application",
            None,
            True,
            "2023-07-16T00:01:41.186448+08:00",
            self,
        )

        card4 = InstanceCard("未命名实例1", "Yue89", "FastAPI", "GitHub")

        self.layout_mannager = QVBoxLayout(self)
        self.layout_mannager.addWidget(card1)
        self.layout_mannager.addWidget(card2)
        self.layout_mannager.addWidget(card3)
        self.layout_mannager.addWidget(card4)


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
