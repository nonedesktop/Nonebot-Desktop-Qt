from qfluentwidgets import SmoothScrollArea

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication

from view.component import FlowLayout, ExtensionCard, InstanceCard


class MainWindow(SmoothScrollArea):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.card_view_content = QWidget()
        self.setWidgetResizable(True)
        self.setViewportMargins(0, 5, 0, 5)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.card_view_content)
        self.layout_manager = FlowLayout(self.card_view_content, needAni=True, isTight=False)
        self.layout_manager.setVerticalSpacing(10)
        self.layout_manager.setHorizontalSpacing(10)
        self.layout_manager.setContentsMargins(8, 3, 8, 8)

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

        card4 = InstanceCard("Untitled Instance", "Yue89", "FastAPI", "GitHub")

        for _ in range(400):
            card = ExtensionCard(
                "example_id",
                "Example Name",
                "Example Title",
                "Example Description",
                "Example Author",
                "https://github.com/example",
                [{"label": "example_label", "color": "#f12020"}],
                True,
                "application",
                None,
                True,
                "2023-08-11T00:00:00.000000+08:00",
                self,
            )
            self.layout_manager.addWidget(card)

        self.layout_manager.addWidget(card1)
        self.layout_manager.addWidget(card2)
        self.layout_manager.addWidget(card3)
        self.layout_manager.addWidget(card4)


if __name__ == "__main__":
    # 试验性地启用GPU渲染来优化性能
    # app = QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL)
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
