from qframelesswindow import FramelessWindow


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self._init_windows_size()

    def _init_windows_size(self):
        self.resize(900, 700)
        # self.setMaximumSize()
        # self.setMinimumSize()
        ## Error raised as no arguments, fill args before uncommenting.