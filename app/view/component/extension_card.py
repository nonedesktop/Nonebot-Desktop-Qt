from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)
from PySide6.QtCore import Qt
from qfluentwidgets import CardWidget, IconWidget
from qfluentwidgets import FluentIcon as FI


class ExtensionCard(CardWidget):
    def __init__(
        self,
        module_name: str,
        project_link: str,
        name: str,
        desc: str,
        author: str,
        homepage: str,
        tags: list[dict[{"label": str, "color": str}]],
        is_official: bool,
        type: str,
        supported_adapters: list[str] | None = None,
        parent=None,
    ):
        super().__init__(parent=parent)
        """Name for importing"""
        self.module_name = module_name
        """Name for downloading from PyPI"""
        self.project_link = project_link
        """Human-readable name"""
        self.name = name
        """Description"""
        self.desc = desc
        """Author"""
        self.author = author
        """Project homepage"""
        self.homepage = homepage
        """Tags"""
        self.tags = tags
        """Whether an extension is official"""
        self.is_official = is_official
        """Plugin category"""
        self.type = type
        """Supported adapters"""
        self.supported_adapters = supported_adapters

        # Instantiating widgets
        self.title_lable = QLabel(name, self)
        self.content_lable = QLabel(desc, self)
        self.pypi_lable = QLabel(module_name, self)
        self.author_lable = QLabel(author, self)
        self.author_icon = IconWidget(FI.PEOPLE, self)
        self.pypi_icon = IconWidget(FI.FINGERPRINT, self)
        self.github_icon = IconWidget(FI.GITHUB, self)
        # TODO MORE WIDGETS

        # Instantiating layouts
        self.layout_mannager = QVBoxLayout(self)
        self.pypi_info_bar_layout_mannager = QHBoxLayout()
        self.author_info_bar_layout_mannager = QHBoxLayout()

        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_widget(self):
        pass

    def __init_sub_widget(self):
        pass

    def __init_layout(self):
        self.setFixedSize(360, 180)
        self.layout_mannager.setContentsMargins(24, 24, 0, 13)
        self.layout_mannager.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_icon)
        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_lable)

        self.author_info_bar_layout_mannager.addWidget(self.author_icon)
        self.author_info_bar_layout_mannager.addWidget(self.author_lable)

        self.layout_mannager.addWidget(self.title_lable)
        self.layout_mannager.addWidget(self.content_lable)
        self.layout_mannager.addLayout(self.pypi_info_bar_layout_mannager)
        self.layout_mannager.addLayout(self.author_info_bar_layout_mannager)
        self.github_icon.move(320, 140)

    def __init_sub_widget_layout(self):
        self.pypi_icon.setFixedSize(16, 16)
        self.author_icon.setFixedSize(16, 16)
        self.github_icon.setFixedSize(28, 28)
