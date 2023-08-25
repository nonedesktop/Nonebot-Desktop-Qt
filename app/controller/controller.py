from typing import TYPE_CHECKING

from qfluentwidgets import Theme, setTheme, setThemeColor

from view.main_window import MainWindow


if TYPE_CHECKING:
    from PySide6.QtGui import QScreen


class Controller:
    def __init__(self) -> None:
        self.ui_main_window = MainWindow()
        self.set_window_theme(Theme.LIGHT)

    def init_window_geometry(self, screen: "QScreen") -> None:
        scale_factor: float = screen.logicalDotsPerInch() / 96.0
        screen_geometry = screen.geometry()
        screen_width: int = screen_geometry.width()
        screen_height: int = screen_geometry.height()

        min_width = int(screen_width * 0.6 * scale_factor)
        min_height = int(screen_height * 0.6 * scale_factor)
        init_width = int(screen_width * 0.75 * scale_factor)
        init_height = int(screen_height * 0.75 * scale_factor)

        self.ui_main_window.setMinimumSize(min_width, min_height)
        self.ui_main_window.resize(init_width, init_height)

        x: int = (screen_geometry.width() - self.ui_main_window.width()) // 2
        y: int = (screen_geometry.height() - self.ui_main_window.height()) // 2
        self.ui_main_window.move(x, y)

    def set_window_theme(self, theme: Theme):
        setTheme(theme)
        setThemeColor("#ea5252")

    def show(self, screen: "QScreen") -> None:
        self.init_window_geometry(screen)
        self.ui_main_window.show()
