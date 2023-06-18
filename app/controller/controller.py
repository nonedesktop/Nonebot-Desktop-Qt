from view.main_window import MainWindow


class Controller:
    def __init__(self) -> None:
        self.ui_main_window = MainWindow()
        self.ui_main_window.show()
