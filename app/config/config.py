from qfluentwidgets import (
    QConfig,
    ConfigItem,
    OptionsConfigItem,
    BoolValidator,
    OptionsValidator,
    ConfigSerializer,
)
from PySide6.QtCore import QLocale

from .constan import Language


class LanguageSerializer(ConfigSerializer):
    def serialize(self, language: Language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, lanuage: str):
        return Language(QLocale(lanuage)) if lanuage != "Auto" else Language.AUTO


class Config(QConfig):
    is_auto_update = ConfigItem("Version", "isAutoUpdate", True, BoolValidator())
    language = OptionsConfigItem(
        "Appearance",
        "Language",
        Language.AUTO,
        OptionsValidator(Language),
        LanguageSerializer(),
        restart=True,
    )
