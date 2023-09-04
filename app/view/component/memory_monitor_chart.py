import random
from typing import Optional, TYPE_CHECKING

from PySide6.QtCore import Qt, QTimer, Slot, QDateTime
from PySide6.QtGui import QPen
from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QDateTimeAxis


if TYPE_CHECKING:
    from PySide6.QtWidgets import QGraphicsItem


class MemoryMonitorChart(QChart):
    def __init__(self, parent: Optional["QGraphicsItem"] = None) -> None:
        super().__init__(type=QChart.ChartType.ChartTypeCartesian, parent=parent, wFlags=Qt.WindowType.Widget)
        # Initializing Data Bindings and Objects
        self.timer = QTimer(self)
        self.data_series = QSplineSeries()
        # Instantiating Widget Objects
        self.axis_brush = QPen()
        self.axis_x = QDateTimeAxis()
        self.axis_y = QValueAxis()
        # Initializing Widget & Layout
        self.__init_sub_widget()
        self.__init_widget()

    def __init_widget(self) -> None:
        self.addSeries(self.data_series)
        self.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.timer.start()

    def __init_sub_widget(self) -> None:
        # Init Timer
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout_handler)
        # Init Brush
        self.axis_brush.setColor(Qt.GlobalColor.black)
        self.axis_brush.setWidthF(2.8)
        # Init X Axis
        self.axis_x.setFormat("hh:mm:ss")
        self.axis_x.setRange(QDateTime.currentDateTime().addSecs(-60), QDateTime.currentDateTime())
        self.axis_x.setTickCount(5)
        # Init Y Axis
        self.axis_y.setTitleText("Memory Usage (%)")
        self.axis_y.setRange(0, 100)
        self.axis_y.setTickCount(5)
        # Init Series
        self.data_series.setPen(self.axis_brush)
        self.data_series.attachAxis(self.axis_x)
        self.data_series.attachAxis(self.axis_y)

        # self._step = 0
        # self._x = 5
        # self._y = 1

        # self.data_series.append(self._x, self._y)


    # @Slot()
    # def handleTimeout(self):
    #     x = self.plotArea().width() / self.axis_x.tickCount()
    #     y = (self.axis_x.max() - self.axis_x.min()) / self.axis_x.tickCount()
    #     self._x += y
    #     self._y = random.uniform(0, 5) - 2.5
    #     self.data_series.append(self._x, self._y)
    #     self.scroll(x, 0)
    #     if self._x == 100:
    #         self.timer.stop()

    @Slot()
    def timeout_handler(self):
        x = self.plotArea().width() / self.axis_x.tickCount()
        now = QDateTime.currentDateTime()
        timestamp = float(now.toMSecsSinceEpoch())
        val = random.randint(12, 20)
        self.data_series.append(timestamp, val)
        self.scroll(x, 0)
