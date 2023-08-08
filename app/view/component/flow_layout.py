# coding:utf-8
from typing import List, TYPE_CHECKING

from PySide6.QtCore import (
    Qt,
    QRect,
    QSize,
    QPoint,
    QEasingCurve,
    QPropertyAnimation,
    QParallelAnimationGroup,
)
from PySide6.QtWidgets import QLayout


if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidgetItem


class FlowLayout(QLayout):
    """Flow layout"""

    def __init__(self, parent=None, needAni=False, isTight=False, durationMsec: int = 120):
        """
        Parameters
        ----------
        parent:
            parent window or layout

        needAni: bool
            whether to add moving animation

        isTight: bool
            whether to use the tight layout when widgets are hidden

        durationMsec: int
            the duration of animation in milliseconds
        """
        super().__init__(parent)
        self._items: List[QWidgetItem] = []
        self._anis: List[QPropertyAnimation] = []
        self._aniGroup = QParallelAnimationGroup(self)
        self._verticalSpacing = 10
        self._horizontalSpacing = 10
        self.needAni = needAni
        self.isTight = isTight
        self.DurationMsec = durationMsec

    def addItem(self, item):
        self._items.append(item)

    def addWidget(self, w):
        super().addWidget(w)
        if not self.needAni:
            return

        ani = QPropertyAnimation(w, b"geometry")
        ani.setEndValue(QRect(QPoint(0, 0), w.size()))
        ani.setDuration(self.DurationMsec)
        w.setProperty("flowAni", ani)
        self._anis.append(ani)
        self._aniGroup.addAnimation(ani)

    def setAnimation(self, duration, ease=QEasingCurve.Type.Linear):
        """set the moving animation

        Parameters
        ----------
        duration: int
            the duration of animation in milliseconds

        ease: QEasingCurve
            the easing curve of animation
        """
        if not self.needAni:
            return

        print(duration, ease)
        for ani in self._anis:
            ani.setDuration(duration)
            ani.setEasingCurve(ease)

    def count(self):
        return len(self._items)

    def itemAt(self, index: int):
        if 0 <= index < len(self._items):
            return self._items[index]

        return None

    def takeAt(self, index: int):
        if 0 <= index < len(self._items):
            item: QWidgetItem = self._items[index]
            ani = item.widget().property("flowAni")
            if ani:
                self._anis.remove(ani)
                self._aniGroup.removeAnimation(ani)
                ani.deleteLater()

            return self._items.pop(index).widget()

        return None

    def removeWidget(self, widget):
        for i, item in enumerate(self._items):
            if item.widget() is widget:
                return self.takeAt(i)

    def removeAllWidgets(self):
        """remove all widgets from layout"""
        while self._items:
            self.takeAt(0)

    def takeAllWidgets(self):
        """remove all widgets from layout and delete them"""
        while self._items:
            w = self.takeAt(0)
            if w:
                w.deleteLater()

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width: int):
        """get the minimal height according to width"""
        return self._doLayout(QRect(0, 0, width, 0), False)

    def setGeometry(self, rect: QRect):
        super().setGeometry(rect)
        self._doLayout(rect, True)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self._items:
            size = size.expandedTo(item.minimumSize())

        m = self.contentsMargins()
        size += QSize(m.left() + m.right(), m.top() + m.bottom())

        return size

    def setVerticalSpacing(self, spacing: int):
        """set vertical spacing between widgets"""
        self._verticalSpacing = spacing

    def verticalSpacing(self):
        """get vertical spacing between widgets"""
        return self._verticalSpacing

    def setHorizontalSpacing(self, spacing: int):
        """set horizontal spacing between widgets"""
        self._horizontalSpacing = spacing

    def horizontalSpacing(self):
        """get horizontal spacing between widgets"""
        return self._horizontalSpacing

    def _doLayout(self, rect: QRect, move: bool):
        """adjust widgets position according to the window size"""
        margin = self.contentsMargins()
        x = rect.x() + margin.left()
        y = rect.y() + margin.top()
        rowHeight = 0
        spaceX = self.horizontalSpacing()
        spaceY = self.verticalSpacing()

        for i, item in enumerate(self._items):
            if item.widget() and not item.widget().isVisible() and self.isTight:
                continue

            nextX = x + item.sizeHint().width() + spaceX

            if nextX - spaceX > rect.right() and rowHeight > 0:
                x = rect.x() + margin.left()
                y = y + rowHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                rowHeight = 0

            if move:
                if not self.needAni:
                    item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
                else:
                    self._anis[i].stop()
                    self._anis[i].setEndValue(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            rowHeight = max(rowHeight, item.sizeHint().height())

        if self.needAni:
            self._aniGroup.stop()
            self._aniGroup.start()

        return y + rowHeight - rect.y()
