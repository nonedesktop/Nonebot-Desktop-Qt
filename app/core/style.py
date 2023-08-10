from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    DASHBOARD_INTERFACE = "DASHBOARD_INTERFACE"
    MARKET_INTERFACE = "MARKET_INTERFACE"
    INSTANCE_INTERFACE = "INSTANCE_INTERFACE"
    SETTING_INTERFACE = "SETTING_INTERFACE"
    EXTENSION_CARD = "EXTENSION_CARD"

    def path(self, theme=Theme.AUTO):
        if theme == Theme.AUTO:
            theme = qconfig.theme
        else:
            theme = theme

        path_prefix: str = "./app/res/style"
        return f"{path_prefix}/{theme.value.lower()}/{self.value.lower()}.qss"
