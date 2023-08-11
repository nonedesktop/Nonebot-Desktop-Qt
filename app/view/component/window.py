from typing import Optional, Union, TYPE_CHECKING

from qfluentwidgets import qrouter, isDarkTheme, FluentStyleSheet, NavigationItemPosition, NavigationInterface
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout

from .frameless_window import FramelessWindow
from .window_title_bar import TitleBar
from .stacked_widget import StackedWidget


if TYPE_CHECKING:
    from PySide6.QtGui import QPaintEvent, QResizeEvent
    from qfluentwidgets import FluentIconBase, NavigationTreeWidget


class Window(FramelessWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.navigation_interface = NavigationInterface(self, showReturnButton=True)
        self.stacked_widget = StackedWidget(self)
        # Instantiating Layout Objects
        self.layout_manager = QHBoxLayout(self)
        self.widget_layout_manager = QHBoxLayout()
        # Initialize Widgets & Layouts
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_sub_layout()
        self.__init_layout()

    def __init_widget(self) -> None:
        self.setTitleBar(TitleBar(self))
        self.titleBar.raise_()
        FluentStyleSheet.FLUENT_WINDOW.apply(self.stacked_widget)

    def __init_sub_widget(self) -> None:
        self.navigation_interface.displayModeChanged.connect(self.titleBar.raise_)

    def __init_layout(self) -> None:
        self.layout_manager.setContentsMargins(0, 0, 0, 0)
        self.layout_manager.setSpacing(0)
        self.layout_manager.setStretchFactor(self.widget_layout_manager, 1)
        self.layout_manager.addWidget(self.navigation_interface)
        self.layout_manager.addLayout(self.widget_layout_manager)

    def __init_sub_layout(self) -> None:
        self.widget_layout_manager.setContentsMargins(0, 48, 0, 0)
        self.widget_layout_manager.addWidget(self.stacked_widget)

    def _onCurrentInterfaceChanged(self, index: int) -> None:
        if not self.navigation_interface:
            raise TypeError
        widget = self.stacked_widget.widget(index)
        self.navigation_interface.setCurrentItem(widget.objectName())
        qrouter.push(self.stacked_widget, widget.objectName())  # type: ignore

    def switchTo(self, interface: QWidget) -> None:
        self.stacked_widget.setCurrentWidget(
            w=interface,
            enableEasingAnimation=False,
            animationDurationMsec=260,
        )

    def addSubInterface(
        self,
        interface: QWidget,
        icon: Union["FluentIconBase", QIcon, str],
        text: str,
        position=NavigationItemPosition.TOP,
        parent: Optional[QWidget] = None,
    ) -> "NavigationTreeWidget":
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

    def resizeEvent(self, event: "QResizeEvent") -> None:
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width() - 46, self.titleBar.height())

    def paintEvent(self, event: "QPaintEvent") -> None:
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)

        if isDarkTheme():
            painter.setBrush(QColor(32, 32, 32))
        else:
            painter.setBrush(QColor(243, 243, 243))

        painter.drawRect(self.rect())
