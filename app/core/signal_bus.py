from PySide6.QtCore import QObject


class _SignalBus(QObject):
    pass


signal_bus = _SignalBus()
