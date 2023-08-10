from typing import Optional

from qfluentwidgets import PopUpAniStackedWidget
from PySide6.QtCore import Qt, Signal, QEasingCurve
from PySide6.QtWidgets import QFrame, QHBoxLayout, QAbstractScrollArea, QWidget


class StackedWidget(QFrame):
    currentChanged = Signal(int)

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.view = PopUpAniStackedWidget(self)
        # Instantiating Layout Objects
        self.layout_manager = QHBoxLayout(self)
        # Initialize Widgets & Layouts
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.view.currentChanged.connect(self.currentChanged)

    def __init_layout(self) -> None:
        self.layout_manager.setContentsMargins(0, 0, 0, 0)
        self.layout_manager.addWidget(self.view)

    def addWidget(self, w: QWidget) -> None:
        self.view.addWidget(w)

    def widget(self, index: int) -> QWidget:
        return self.view.widget(index)

    def setCurrentWidget(
        self,
        w: QWidget,
        enableEasingAnimation: bool = True,
        easingCurveType: QEasingCurve.Type = QEasingCurve.Type.InBack,
        animationDurationMsec: int = 300,
    ) -> None:
        if isinstance(w, QAbstractScrollArea):
            w.verticalScrollBar().setValue(0)

        if not enableEasingAnimation:
            self.view.setCurrentWidget(w, duration=animationDurationMsec)
            return

        self.view.setCurrentWidget(w, True, False, animationDurationMsec, easingCurveType)

    def setCurrentIndex(
        self,
        index: int,
        enableEasingAnimation: bool = True,
        easingCurveType: QEasingCurve.Type = QEasingCurve.Type.InBack,
        animationDurationMsec: int = 300,
    ) -> None:
        self.setCurrentWidget(self.view.widget(index), enableEasingAnimation, easingCurveType, animationDurationMsec)

    def currentIndex(self) -> int:
        return self.view.currentIndex()

    def indexOf(self, w: QWidget) -> int:
        return self.view.indexOf(w)

    def count(self) -> int:
        return self.view.count()
