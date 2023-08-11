from typing import Optional, Union, TYPE_CHECKING

from qfluentwidgets import FluentStyleSheet
from qframelesswindow import TitleBar as TitleBarBase
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout


if TYPE_CHECKING:
    from PySide6.QtGui import QImage, QPixmap


class TitleBar(TitleBarBase):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.icon_label = QLabel(self)
        self.title_label = QLabel(self)
        # Instantiating Layout Objects
        self.button_layout_manager = QHBoxLayout()
        self.sub_layout_manager = QVBoxLayout()
        # Initialize Widgets & Layouts
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        self.setFixedHeight(48)
        self.window().windowIconChanged.connect(self.setIcon)
        self.window().windowTitleChanged.connect(self.setTitle)
        FluentStyleSheet.FLUENT_WINDOW.apply(self)

    def __init_sub_widget(self) -> None:
        self.title_label.setObjectName("titleLabel")
        self.icon_label.setFixedSize(18, 18)

    def __init_layout(self) -> None:
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)
        self.hBoxLayout.insertWidget(0, self.icon_label, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.hBoxLayout.insertWidget(1, self.title_label, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.hBoxLayout.addLayout(self.sub_layout_manager, 0)

    def __init_sub_layout(self) -> None:
        self.button_layout_manager.setContentsMargins(0, 0, 0, 0)
        self.button_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.button_layout_manager.setSpacing(0)
        self.button_layout_manager.addWidget(self.minBtn)
        self.button_layout_manager.addWidget(self.maxBtn)
        self.button_layout_manager.addWidget(self.closeBtn)
        self.sub_layout_manager.addLayout(self.button_layout_manager)
        self.sub_layout_manager.addStretch(1)

    def setTitle(self, title: str) -> None:
        self.title_label.setText(title)
        self.title_label.adjustSize()

    def setIcon(self, icon: Union["QPixmap", "QImage", str]) -> None:
        self.icon_label.setPixmap(QIcon(icon).pixmap(18, 18))
