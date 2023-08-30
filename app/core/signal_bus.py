from PySide6.QtCore import QObject, Signal

from model import InstanceMetadata


class _SignalBus(QObject):
    InstanceCardClicked = Signal(InstanceMetadata)


signal_bus = _SignalBus()
