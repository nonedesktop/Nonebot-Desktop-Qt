from PySide6.QtCore import QObject, Signal


class _SignalBus(QObject):
    FOO = Signal()


signal_bus = _SignalBus()
