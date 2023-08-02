from PySide6.QtCore import QObject

from .singleton import SingletonMeta


class SingleBus(QObject, metaclass=SingletonMeta):
    pass
