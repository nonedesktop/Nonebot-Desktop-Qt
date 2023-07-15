from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QTextBrowser,
    QVBoxLayout,
)
from PySide6.QtCore import Qt
from qfluentwidgets import CardWidget, IconWidget, PrimaryPushButton
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

        self.module_name = module_name
        """Name for importing"""
        self.project_link = project_link
        """Name for downloading from PyPI"""
        self.name = name
        """Human-readable name"""
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
        self.type = type
        """Plugin category"""
        self.supported_adapters = supported_adapters
        """Supported adapters"""

        # Instantiating widgets
        self.title_label = QLabel(name, self)
        self.content_label = QTextBrowser(self)
        self.pypi_label = QLabel(project_link, self)
        self.author_label = QLabel(author, self)
        self.author_icon = IconWidget(FI.PEOPLE, self)
        self.pypi_icon = IconWidget(FI.FINGERPRINT, self)
        self.github_icon = IconWidget(FI.GITHUB, self)
        self.mannage_button = PrimaryPushButton("MANNAGE", self)
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
        title_font = self.title_label.font()
        title_font.setPointSize(12)
        self.title_label.setFont(title_font)
        self.title_label.setToolTip("非官方插件")
        if self.is_official:
            self.title_label.setText(
                "<html><head/><body><p><span style=\" color:#0cd50c;\">"
                f"{self.name}</span></p></body></html>"
            )
            self.title_label.setToolTip("官方插件")

        self.content_label.setText(self.desc)
        self.content_label.setFrameStyle(0)
        # The annotation says that it accepts an int parameter,
        # but besides this there is no more information.
        # Maybe I should find and read Qt's documents.

        self.pypi_label.setToolTip(self.module_name)


        # Here we depens on the status to modfiy the button's text:
        # if installed set uninstall
        # if uninstalled set install
        # we get the status from instance globe status object
        
        # self.mannage_button.setText()

    def __init_layout(self):
        self.setFixedSize(360, 168)
        self.layout_mannager.setContentsMargins(16, 12, 12, 12)
        self.layout_mannager.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_icon)
        self.pypi_info_bar_layout_mannager.addSpacing(2)
        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_label)

        self.author_info_bar_layout_mannager.addWidget(self.author_icon)
        self.author_info_bar_layout_mannager.addSpacing(2)
        self.author_info_bar_layout_mannager.addWidget(self.author_label)

        self.layout_mannager.addWidget(self.title_label)
        self.layout_mannager.addWidget(self.content_label)
        self.layout_mannager.addLayout(self.pypi_info_bar_layout_mannager)
        self.layout_mannager.addLayout(self.author_info_bar_layout_mannager)
        self.github_icon.move(320, 128)
        self.mannage_button.move(220, 128) # 临时放在这里

        # vbox layout:
        #     label title
        #     textbrowser content
        #     hbox pypi_info:
        #         icon pypi_icon
        #         label pypi_name
        #     hbox author_info:
        #         icon author_icon
        #         label author_name
        # icon gh_icon

    def __init_sub_widget_layout(self):
        self.pypi_icon.setFixedSize(16, 16)
        self.author_icon.setFixedSize(16, 16)
        self.github_icon.setFixedSize(28, 28)

    # TODO: Click vbox to perform installation (ask users)
