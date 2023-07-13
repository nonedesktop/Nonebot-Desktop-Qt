from PySide6.QtGui import QFont
from qfluentwidgets import FluentLabelBase


def getFont(fontSize: int = 14, fontWeight: QFont.Weight = QFont.Weight.Normal) -> QFont:
    font = QFont()
    font.setFamilies(["Segoe UI", "Microsoft YaHei", "PingFang SC"])
    font.setPixelSize(fontSize)
    font.setWeight(fontWeight)
    return font


class InterfaceTitle(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=28, fontWeight=QFont.Weight.Bold)


class InterfaceDesc(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=14, fontWeight=QFont.Weight.Normal)
