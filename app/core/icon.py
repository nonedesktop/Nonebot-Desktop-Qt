from enum import Enum
from qfluentwidgets import getIconColor, Theme, FluentIconBase


class MyFluentIcon(FluentIconBase, Enum):
    ADD = "Add"
    CUT = "Cut"
    COPY = "Copy"
    BOT = "Bot"
    BOTSPARKLE = "BotSparkle"
    OFFICALMARK = "OfficalMark"
    NOTOFFICALMARK = "NotOfficalMark"
    CHECKPASS = "CheckPass"
    CHECKNOTPASS = "CheckNotPass"

    def path(self, theme=Theme.AUTO):
        return f"./app/res/icons/{self.value}_{getIconColor(theme)}.svg"
