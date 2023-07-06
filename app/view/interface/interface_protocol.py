from typing import Optional, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QObject


class Interface(Protocol):
    def __init__(self, parent: Optional["QObject"] = None) -> None:
        # super().__init__(parent)
        ...

    def __init_widget(self) -> None:
        ...

    def __init_sub_widget(self) -> None:
        ...

    def __init_layout(self) -> None:
        ...
