from typing import Optional, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QObject


class Interface(Protocol):
    def __init__(self, parent: Optional["QObject"] = None) -> None:
        # super().__init__(parent)
        # Instantiating Data Structures
        # Instantiating Widget Objects
        # Instantiating Layout Objects
        # Initialize Widgets & Layouts
        ...

    def __init_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        # Set Geometry
        ...

    def __init_sub_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        # Set Geometry
        ...

    def __init_layout(self) -> None:
        # Set Layout Options
        # Place layout widgets
        ...
