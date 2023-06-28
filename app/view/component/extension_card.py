from qfluentwidgets import CardWidget


class ExtensionCard(CardWidget):
    def __init__(
        self,
        module_name: str,
        project_link: str,
        name: str,
        desc: str,
        author: str,
        homepage: str,
        tags: list[dict[{"label": str, "color": str}]],
        is_official: bool,
        parent=None,
    ):
        super().__init__(parent=parent)
        self.module_name = module_name
        """Name for importing"""
        self.project_link = project_link
        """Name for downloading from PyPI"""
        self.name = name
        """Human-readable name"""
        self.desc = desc
        """Description"""
        self.author = author
        """Author"""
        self.homepage = homepage
        """Project homepage"""
        self.tags = tags
        """Tags"""
        self.is_official = is_official
        """Whether an extension is official"""


class PluginCard(ExtensionCard):
    def __init__(
        self,
        module_name: str,
        project_link: str,
        name: str,
        desc: str,
        author: str,
        homepage: str,
        tags: list[dict[{"label": str, "color": str}]],
        is_official: bool,
        type: str,
        supported_adapters: list[str],
        parent=None,
    ):
        super().__init__(
            module_name,
            project_link,
            name,
            desc,
            author,
            homepage,
            tags,
            is_official,
            parent=parent,
        )
        self.type = type
        """Plugin category"""
        self.supported_adapters = supported_adapters
        """Supported adapters"""


class AdapterCard(ExtensionCard):
    def __init__(
        self,
        module_name: str,
        project_link: str,
        name: str,
        desc: str,
        author: str,
        homepage: str,
        tags: list[dict[{"label": str, "color": str}]],
        is_official: bool,
        parent=None,
    ):
        super().__init__(
            module_name,
            project_link,
            name,
            desc,
            author,
            homepage,
            tags,
            is_official,
            parent=parent,
        )
