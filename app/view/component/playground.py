from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout
from extension_card import ExtensionCard


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        card = ExtensionCard(
            "服务器状态查看",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            "服务器状态查看",
            "通过戳一戳获取服务器状态",
            "yanyongyu",
            "https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status",
            ["t:server"],
            True,
            "Plugin",
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
