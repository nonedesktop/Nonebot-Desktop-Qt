from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from qfluentwidgets import CardWidget, IconWidget
from qfluentwidgets import FluentIcon as FI

from core import StyleSheet
from core import MyFluentIcon as MFI


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
        supported_adapters: list[str] | None,
        valid: bool,
        time: str,
        parent=None,
    ):
        super().__init__(parent=parent)
        # Binding data
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
        self.valid = valid
        """Plugin load test result"""
        self.time = time
        """Plugin load test time"""
        # TODO: use pydantic model instead of bunches of params

        # Instantiating widgets
        self.title_label = QLabel(name, self)
        self.content_label = QLabel(self.desc, self)
        self.pypi_label = QLabel(project_link, self)
        self.author_label = QLabel(author, self)
        self.author_icon = IconWidget(FI.PEOPLE, self)
        self.pypi_icon = IconWidget(FI.FINGERPRINT, self)
        self.github_icon = IconWidget(FI.GITHUB, self)
        # self.mannage_button = PrimaryPushButton("MANNAGE", self)
        self.offical_mark_icon = IconWidget(MFI.NOTOFFICALMARK, self)
        self.check_mark_icon = IconWidget(MFI.CHECKNOTPASS, self)
        # TODO MORE WIDGETS
        # Instantiating layouts
        self.layout_mannager = QVBoxLayout(self)
        self.header_bar_layout_manager = QHBoxLayout()
        self.pypi_info_bar_layout_mannager = QHBoxLayout()
        self.author_info_bar_layout_mannager = QHBoxLayout()
        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_widget(self):
        # Set widgets object name
        self.setObjectName("ExtensionCard")
        # Apply stylesheet
        StyleSheet.EXTENSION_CARD.apply(self)

    def __init_sub_widget(self):
        # Set widgets object name
        self.title_label.setObjectName("ExtensionCardTitleLabel")
        self.content_label.setObjectName("ExtensionCardContentLabel")
        self.author_label.setObjectName("ExtensionCardAuthorLabel")
        self.pypi_label.setObjectName("ExtensionCardPypiLabel")
        # Set widgets options
        self.content_label.setWordWrap(True)
        # Set tooltips
        self.offical_mark_icon.setToolTip("非官方认证")
        self.check_mark_icon.setToolTip("测试未通过")
        # Update status badges
        if self.is_official:
            self.offical_mark_icon.setIcon(MFI.OFFICALMARK)
            self.offical_mark_icon.setToolTip("官方认证")
        if self.valid:
            self.check_mark_icon.setIcon(MFI.CHECKPASS)
            self.check_mark_icon.setToolTip("测试通过")
        # Set urlopen
        self.github_icon.mouseReleaseEvent = (
            lambda event:
            (None, QDesktopServices.openUrl(self.homepage))[0]
        )
        self.github_icon.setToolTip("前往项目主页")
        self.github_icon.setCursor(Qt.CursorShape.PointingHandCursor)

    def __init_layout(self):
        # Set layout options
        self.setFixedSize(360, 168)
        self.layout_mannager.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout_mannager.setContentsMargins(16, 12, 12, 12)
        # Place layout widgets
        self.layout_mannager.addLayout(self.header_bar_layout_manager)
        self.layout_mannager.addWidget(self.content_label)
        self.layout_mannager.addLayout(self.pypi_info_bar_layout_mannager)
        self.layout_mannager.addLayout(self.author_info_bar_layout_mannager)
        self.github_icon.move(320, 128)
        # self.mannage_button.move(220, 128)  # 临时放在这里

    def __init_sub_widget_layout(self):
        self.offical_mark_icon.setFixedSize(22, 22)
        self.check_mark_icon.setFixedSize(22, 22)
        self.content_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.pypi_icon.setFixedSize(14, 14)
        self.author_icon.setFixedSize(14, 14)
        self.github_icon.setFixedSize(28, 28)
        # Place header bar layout widgets
        self.header_bar_layout_manager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.header_bar_layout_manager.addWidget(self.title_label)
        self.header_bar_layout_manager.addWidget(self.offical_mark_icon)
        self.header_bar_layout_manager.addWidget(self.check_mark_icon)
        # Place pypi bar layout widgets
        self.pypi_info_bar_layout_mannager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_icon)
        self.pypi_info_bar_layout_mannager.addSpacing(2)
        self.pypi_info_bar_layout_mannager.addWidget(self.pypi_label)
        # Place author bar layout widgets
        self.author_info_bar_layout_mannager.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.author_info_bar_layout_mannager.addWidget(self.author_icon)
        self.author_info_bar_layout_mannager.addSpacing(2)
        self.author_info_bar_layout_mannager.addWidget(self.author_label)
