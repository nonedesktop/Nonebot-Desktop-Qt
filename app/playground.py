import random
from time import perf_counter
from datetime import datetime, timedelta

from qfluentwidgets import SmoothScrollArea
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication

from model import ColoredTag, PluginMetadata
from view.component import FlowLayout, ExtensionCard


class MainWindow(SmoothScrollArea):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.init_ui()
        start_time = perf_counter()
        self.load_card(500)
        end_time = perf_counter()
        print(f"加载500个卡片共耗时{end_time - start_time:.2f}秒")

    def init_ui(self) -> None:
        start_time = perf_counter()
        self.card_view_content = QWidget()
        self.layout_manager = FlowLayout(self.card_view_content, needAni=True)
        self.setWidget(self.card_view_content)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 5, 0, 5)
        self.layout_manager.setContentsMargins(8, 3, 8, 8)
        self.layout_manager.setVerticalSpacing(10)
        self.layout_manager.setHorizontalSpacing(10)
        end_time = perf_counter()
        print(f"初始化UI共耗时{end_time - start_time:.2f}秒")

    def generate_colored_tag(self) -> ColoredTag:
        colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
        return ColoredTag(label=f"Tag-{random.randint(1, 100)}", color=random.choice(colors))

    def generate_plugin_metadata(self) -> PluginMetadata:
        tags = [self.generate_colored_tag() for _ in range(3)]  # Generating 3 tags for each plugin
        return PluginMetadata(
            module_name=f"module_{random.randint(1, 100)}",
            project_link=f"pypi.org/project/module_{random.randint(1, 100)}",
            name=f"Module {random.randint(1, 100)}",
            desc=f"Description for Module {random.randint(1, 100)}",
            author=f"Author-{random.randint(1, 100)}",
            homepage=f"homepage-{random.randint(1, 100)}.com",
            tags=tags,
            is_official=random.choice([True, False]),
            type=f"Type-{random.choice(['A', 'B', 'C'])}",
            supported_adapters=[f"adapter-{random.randint(1, 10)}" for _ in range(random.randint(1, 5))],
            valid=random.choice([True, False]),
            time=datetime.now() - timedelta(days=random.randint(1, 365)),
        )

    def add_card(self, matadate: PluginMetadata) -> None:
        self.layout_manager.addWidget(ExtensionCard(matadate, self))

    def load_card(self, num: int) -> None:
        for _ in range(num):
            self.add_card(self.generate_plugin_metadata())


if __name__ == "__main__":
    total_start_time = perf_counter()
    # 试验性地启用GPU渲染来优化性能
    # app = QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL)
    app = QApplication([])
    init_qapp_time = perf_counter()
    print(f"初始化QApplication对象耗时{init_qapp_time - total_start_time:.2f}秒")
    w = MainWindow()
    init_mainwindows_time = perf_counter()
    print(f"初始化MainWindow对象耗时{init_mainwindows_time - total_start_time:.2f}秒")
    w.show()
    total_end_time = perf_counter()
    print(f"完成渲染绘制到事件循环启动共耗时{total_end_time - total_start_time:.2f}秒")
    app.exec()
