from qfluentwidgets import FluentLabelBase
from PySide6.QtGui import QFont


def getFont(fontSize: int = 14, fontWeight: QFont.Weight = QFont.Weight.Normal) -> QFont:
    font = QFont()
    font.setFamilies(["Segoe UI", "Microsoft YaHei", "PingFang SC"])
    font.setPixelSize(fontSize)
    font.setWeight(fontWeight)
    return font


class CaptionLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=12, fontWeight=QFont.Weight.Normal)


class BodyLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=14, fontWeight=QFont.Weight.Normal)


class BodyStrongLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=14, fontWeight=QFont.Weight.DemiBold)


class BodyLargeLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=18, fontWeight=QFont.Weight.Normal)


class SubtitleLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=20, fontWeight=QFont.Weight.Bold)


class TitleLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=28, fontWeight=QFont.Weight.Bold)


class TitleLargeLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=40, fontWeight=QFont.Weight.Bold)


class DisplayLabel(FluentLabelBase):
    def getFont(self) -> QFont:
        return getFont(fontSize=68, fontWeight=QFont.Weight.Bold)
