from qfluentwidgets import CardWidget


class ExtensionCard(CardWidget):
    module_name: str
    """Name for importing"""

    project_link: str
    """Name for downloading from PyPI"""

    name: str
    """Human-readable name"""

    desc: str
    """Description"""

    author: str
    """Author"""

    homepage: str
    """Project homepage"""

    tags: list[dict[{"label": str, "color": str}]]
    """Tags"""

    is_official: bool
    """Whether an extension is official"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)


class PluginCard(ExtensionCard):
    type: str
    """Plugin category"""

    supported_adapters: list[str]
    """Supported adapters"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)


class AdapterCard(ExtensionCard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
