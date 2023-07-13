from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
from extension_card import ExtensionCard


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        card = ExtensionCard(
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
            self
        )

        self.layout_mannager = QVBoxLayout(self)
        self.layout_mannager.addWidget(card)


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
