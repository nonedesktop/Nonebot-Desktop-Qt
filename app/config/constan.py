from enum import Enum

from PySide6.QtCore import QLocale


class Language(Enum):
    AUTO = QLocale()
    ENGLISH = QLocale(QLocale.Language.English)
    CHINESE_SIMPLIFIED = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Language.Chinese, QLocale.Country.HongKong)
