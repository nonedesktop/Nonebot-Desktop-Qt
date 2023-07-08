from qfluentwidgets import Theme, setTheme, setThemeColor

from view.main_window import MainWindow


class Controller:
    def __init__(self) -> None:
        self.ui_main_window = MainWindow()
        self.set_window_theme(Theme.DARK)

    def init_window_geometry(self, w: int, h: int):
        main = self.ui_main_window
        desktop_pixel_ratio: float = main.devicePixelRatioF()
        main.resize(int(w * 0.8), int(h * 0.8))
        main.setMinimumSize(
            int(w * desktop_pixel_ratio * 1030 / 1920),
            int(h * desktop_pixel_ratio * 780 / 1080),
        )
        main.setMaximumSize(int(w * 1.2), int(h * 1.2))
        main.move(w // 2 - main.width() // 2, h // 2 - main.height() // 2)

    def set_window_theme(self, theme: Theme):
        setTheme(theme)
        setThemeColor("#ea5252")

    def show(self, w: int, h: int):
        self.init_window_geometry(w, h)
        main = self.ui_main_window
        main.show()
