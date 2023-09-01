from typing import Optional
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout
from qfluentwidgets import SubtitleLabel, setFont


class InterfaceTemplates(QFrame):
    def __init__(self, obj_name: str, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(obj_name)
        self.sub_title = SubtitleLabel(text, self)
        self.layout_manager = QHBoxLayout(self)
        setFont(self.sub_title, 24)
        self.sub_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.addWidget(self.sub_title, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout_manager.setContentsMargins(0, 32, 0, 0)


class Templates(QObject):
    """Widget Doc"""

    someSignal: Signal = Signal()
    """Signal Doc"""

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent=parent)
        # Initializing Data Bindings and Objects
        # Instantiating Widget Objects
        # Instantiating Layout Objects
        # Initializing Widget & Layout
        self.__init_sub_widget__()
        self.__init_widget__()
        self.__init_sub_layout__()
        self.__init_layout__()

    def __init_widget__(self) -> None:
        # Setting Objects Name
        # Setting Widget Sub Widget
        # Setting Widget Options
        # Setting Widget Geometry
        # Initialize Signal Connections
        # Setting Widget StyleSheet
        pass

    def __init_sub_widget__(self) -> None:
        # Setting Objects Name
        # Setting Widget Sub Widget
        # Setting Widget Options
        # Setting Widget Geometry
        # Initialize Signal Connections
        # Setting Widget StyleSheet
        pass

    def __init_layout__(self) -> None:
        # Setting Layout Options
        # Arranging Widgets & Layouts
        pass

    def __init_sub_layout__(self) -> None:
        # Setting Layout Options
        # Arranging Widgets & Layouts
        pass

    def event_rewrite(self) -> None:
        pass

    def public_api(self) -> None:
        """API Doc"""
        pass
