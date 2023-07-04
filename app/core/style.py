from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    MARKET_INTERFACE = "MARKET_INTERFACE"

    def path(self, theme=Theme.AUTO):
        if theme == Theme.AUTO:
            theme = qconfig.theme
        else:
            theme = theme

        path_prefix: str = "./app/res/style"
        return f"{path_prefix}/{theme.value.lower()}/{self.value.lower()}.qss"
