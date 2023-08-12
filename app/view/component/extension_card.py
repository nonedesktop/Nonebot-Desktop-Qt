from typing import Optional, TYPE_CHECKING

from qfluentwidgets import CardWidget, IconWidget, PrimaryPushButton, FluentIcon as FI
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy

from core import StyleSheet, MyFluentIcon as MFI
from model import PluginMetadata


if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class ExtensionCard(CardWidget):
    clicked: Signal = Signal(PluginMetadata)

    def __init__(
        self,
        metadata: PluginMetadata,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent=parent)
        # Binding data
        self.metadata = metadata
        # Instantiating widgets
        self.title_label = QLabel(metadata.name, self)
        self.content_label = QLabel(self.metadata.desc, self)
        self.pypi_label = QLabel(metadata.project_link, self)
        self.author_label = QLabel(metadata.author, self)
        self.author_icon = IconWidget(FI.PEOPLE, self)
        self.pypi_icon = IconWidget(FI.FINGERPRINT, self)
        self.offical_mark_icon = IconWidget(MFI.NOTOFFICALMARK, self)
        self.check_mark_icon = IconWidget(MFI.CHECKNOTPASS, self)
        self.mannage_button = PrimaryPushButton("安装", self)
        self.github_icon = IconWidget(FI.GITHUB, self)
        # Instantiating layouts
        self.layout_manager = QVBoxLayout(self)
        self.header_bar_layout_manager = QHBoxLayout()
        self.pypi_info_bar_layout_mannager = QHBoxLayout()
        self.author_info_bar_layout_mannager = QHBoxLayout()
        # Initialize self widget & layout
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_widget_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set widgets object name
        self.setObjectName("ExtensionCard")
        # Apply stylesheet
        StyleSheet.EXTENSION_CARD.apply(self)

    def __init_sub_widget(self) -> None:
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
        if self.metadata.is_official:
            self.offical_mark_icon.setIcon(MFI.OFFICALMARK)
            self.offical_mark_icon.setToolTip("官方认证")
        if self.metadata.valid:
            self.check_mark_icon.setIcon(MFI.CHECKPASS)
            self.check_mark_icon.setToolTip("测试通过")
        # Set urlopen
        self.github_icon.mouseReleaseEvent = lambda event: (
            None,
            QDesktopServices.openUrl(self.metadata.homepage),
        )[0]
        self.github_icon.setToolTip("前往项目主页")
        self.github_icon.setCursor(Qt.CursorShape.PointingHandCursor)

    def __init_layout(self) -> None:
        # Set layout options
        self.setFixedSize(360, 168)
        self.layout_manager.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout_manager.setContentsMargins(16, 12, 12, 12)
        # Place layout widgets
        self.layout_manager.addLayout(self.header_bar_layout_manager)
        self.layout_manager.addWidget(self.content_label)
        self.layout_manager.addLayout(self.pypi_info_bar_layout_mannager)
        self.layout_manager.addLayout(self.author_info_bar_layout_mannager)
        self.mannage_button.move(240, 128)
        self.github_icon.move(320, 128)

    def __init_sub_widget_layout(self) -> None:
        self.offical_mark_icon.setFixedSize(22, 22)
        self.check_mark_icon.setFixedSize(22, 22)
        self.content_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.pypi_icon.setFixedSize(14, 14)
        self.author_icon.setFixedSize(14, 14)
        self.mannage_button.setFixedSize(64, 28)
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
