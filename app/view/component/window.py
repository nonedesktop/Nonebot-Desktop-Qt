from typing import Optional, Union, NoReturn

from qfluentwidgets import (
    qrouter,
    isDarkTheme,
    FluentStyleSheet,
    NavigationItemPosition,
    FluentIconBase,
    NavigationInterface,
    NavigationTreeWidget,
)
from qframelesswindow import TitleBar as TitleBarBase
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPainter, QColor, QPixmap, QImage
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout

from .frameless_window import FramelessWindow
from .stacked_widget import StackedWidget


class WindowBase(FramelessWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.stacked_widget = StackedWidget(self)
        self.navigation_interface: Optional[NavigationInterface] = None
        # Instantiating Layout Objects
        self.layout_manager = QHBoxLayout(self)
        # Initialize Widgets & Layouts
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        FluentStyleSheet.FLUENT_WINDOW.apply(self.stacked_widget)

    def __init_layout(self) -> None:
        self.layout_manager.setContentsMargins(0, 0, 0, 0)
        self.layout_manager.setSpacing(0)

    def _onCurrentInterfaceChanged(self, index: int) -> None:
        if not self.navigation_interface:
            raise TypeError
        widget = self.stacked_widget.widget(index)
        self.navigation_interface.setCurrentItem(widget.objectName())
        qrouter.push(self.stacked_widget, widget.objectName())  # type: ignore

    def addSubInterface(
        self,
        interface: QWidget,
        icon: Union[FluentIconBase, QIcon, str],
        text: str,
        position=NavigationItemPosition.TOP,
    ) -> NoReturn:
        raise NotImplementedError

    def switchTo(self, interface: QWidget) -> None:
        self.stacked_widget.setCurrentWidget(
            w=interface,
            enableEasingAnimation=False,
            animationDurationMsec=250,
        )

    def paintEvent(self, e) -> None:
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)

        if isDarkTheme():
            painter.setBrush(QColor(32, 32, 32))
        else:
            painter.setBrush(QColor(243, 243, 243))

        painter.drawRect(self.rect())


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

    def setIcon(self, icon: Union[QPixmap, QImage, str]) -> None:
        self.icon_label.setPixmap(QIcon(icon).pixmap(18, 18))


class Window(WindowBase):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.navigation_interface = NavigationInterface(self, showReturnButton=True)

        self.setTitleBar(TitleBar(self))

        self.widgetLayout = QHBoxLayout()

        # initialize layout
        self.layout_manager.addWidget(self.navigation_interface)
        self.layout_manager.addLayout(self.widgetLayout)
        self.layout_manager.setStretchFactor(self.widgetLayout, 1)

        self.widgetLayout.addWidget(self.stacked_widget)
        self.widgetLayout.setContentsMargins(0, 48, 0, 0)

        self.navigation_interface.displayModeChanged.connect(self.titleBar.raise_)
        self.titleBar.raise_()

    def addSubInterface(
        self,
        interface: QWidget,
        icon: Union[FluentIconBase, QIcon, str],
        text: str,
        position=NavigationItemPosition.TOP,
        parent: Optional[QWidget] = None,
    ) -> NavigationTreeWidget:
        """add sub interface, the object name of `interface` should be set already
        before calling this method

        Parameters
        ----------
        interface: QWidget
            the subinterface to be added

        icon: FluentIconBase | QIcon | str
            the icon of navigation item

        text: str
            the text of navigation item

        position: NavigationItemPosition
            the position of navigation item

        parent: QWidget
            the parent of navigation item
        """
        if not self.navigation_interface:
            raise TypeError
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")
        if parent and not parent.objectName():
            raise ValueError("The object name of `parent` can't be empty string.")

        self.stacked_widget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
        item = self.navigation_interface.addItem(
            routeKey=routeKey,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None,
        )

        # initialize selected item
        if self.stacked_widget.count() == 1:
            self.stacked_widget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigation_interface.setCurrentItem(routeKey)
            qrouter.setDefaultRouteKey(self.stacked_widget, routeKey)  # type: ignore

        return item

    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width() - 46, self.titleBar.height())
