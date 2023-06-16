import time

from PySide6.QtWidgets import QApplication

from view.main_window import MainWindow

if __name__ == "__main__":
    time_start = time.perf_counter()
    app = QApplication()
    gui = MainWindow()
    gui.show()
    time_end = time.perf_counter()
    print(f"系统渲染UI耗时{((time_end - time_start) * 1000):.1f}毫秒")
    app.exec()
