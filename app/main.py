import time

from PySide6.QtWidgets import QApplication

from controller.controller import Controller


def get_screen_geometry(app: QApplication) -> tuple[int, int]:
    primary_screen = app.primaryScreen()
    geometry = primary_screen.geometry()
    screen_width: int = geometry.width()
    screen_height: int = geometry.height()
    return screen_width, screen_height


if __name__ == "__main__":
    time_start = time.perf_counter()
    app = QApplication()
    w, h = get_screen_geometry(app)
    ctr = Controller()
    ctr.init_window_geometry(w, h)
    ctr.ui_main_window.show()
    time_end = time.perf_counter()
    print(f"系统渲染UI耗时{((time_end - time_start) * 1000):.1f}毫秒")
    app.exec()
