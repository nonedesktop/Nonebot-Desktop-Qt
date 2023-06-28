from enum import Enum
from pathlib import Path

from qfluentwidgets import getIconColor, Theme, FluentIconBase


class MyFluentIcon(FluentIconBase, Enum):
    ADD = "Add"
    CUT = "Cut"
    COPY = "Copy"
    BOT = "Bot"

    def path(self, theme=Theme.AUTO):
        return f"./app/res/icons/{self.value}_{getIconColor(theme)}.svg"


print(Path.cwd())