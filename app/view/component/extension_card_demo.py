import os


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QWidget
from qfluentwidgets import CardWidget, PushButton, BodyLabel, CaptionLabel, IconWidget


class ExtensionCard(CardWidget):
    def __init__(
        self,
        module_name: str,
        project_link: str,
        name: str,
        icon: str,
        desc: str,
        author: str,
        homepage: str,
        tags: list[dict[{"label": str, "color": str}]],
        is_official: bool,
        parent=None,
    ):
        super().__init__(parent=parent)
        self.module_name = module_name
        """Name for importing"""
        self.project_link = project_link
        """Name for downloading from PyPI"""
        self.name = name
        """Human-readable name"""
        self.icon = icon
        self.desc = desc
        """Description"""
        self.author = author
        """Author"""
        self.homepage = homepage
        """Project homepage"""
        self.tags = tags
        """Tags"""
        self.is_official = is_official
        """Whether an extension is official"""

        self.init_widget()
        self.init_inner_widgets()
        self.init_layout()

    def init_inner_widgets(self):
        self.icon_widget = IconWidget(self.icon)
        self.name_lable = BodyLabel(self.name, self)
        self.desc_lable = CaptionLabel(self.desc, self)
        self.author_lable = CaptionLabel(self.author, self)
        self.install_button = PushButton("安装", self)
        self.uninstall_button = PushButton("卸载", self)

        self.icon_widget.setFixedSize(50, 50)
        self.desc_lable.setTextColor("#606060", "#d2d2d2")
        self.install_button.setFixedWidth(100)
        self.uninstall_button.setFixedWidth(100)

    def init_layout(self):
        self.card_text_layout = QVBoxLayout()
        self.card_text_layout.setContentsMargins(0, 0, 0, 0)
        self.card_text_layout.setSpacing(0)
        self.card_text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.card_layout = QHBoxLayout(self)
        self.card_layout.setContentsMargins(20, 11, 11, 11)
        self.card_layout.setSpacing(15)
        self.card_layout.addWidget(self.icon_widget)
        
        self.card_text_layout.addWidget(self.name_lable, 0, Qt.AlignmentFlag.AlignVCenter)
        self.card_text_layout.addWidget(self.desc_lable, 0, Qt.AlignmentFlag.AlignVCenter)
        self.card_text_layout.addWidget(self.author_lable, 0, Qt.AlignmentFlag.AlignVCenter)

        self.card_layout.addLayout(self.card_text_layout)
        self.card_layout.addStretch(1)
        self.card_layout.addWidget(self.install_button, 0, Qt.AlignmentFlag.AlignRight)
        self.card_layout.addWidget(self.uninstall_button, 0, Qt.AlignmentFlag.AlignRight)

    def init_widget(self):
        self.setFixedHeight(90)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 600)
        self.layout_mananger = QVBoxLayout(self)
        self.layout_mananger.setSpacing(6)
        self.layout_mananger.setContentsMargins(30, 30, 30, 30)
        self.layout_mananger.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")
        self.addCard("通用数据库连接", "连接至各种数据库,为其他插件导出连接对象")
        self.addCard("Sentry日志监控", "使用Sentry监控机器人日志并处理报错")
        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")
        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")
        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")
        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")
        self.addCard("服务器状态查看", "通过戳一戳获取服务器状态")

    def addCard(self, name, desc):
        card = ExtensionCard("", "", name, "logo.png", desc, "👨 NCBM", "", [], False, self)
        self.layout_mananger.addWidget(card, alignment=Qt.AlignmentFlag.AlignTop)


if __name__ == "__main__":
    current_file = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file)
    os.chdir(current_directory)
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
