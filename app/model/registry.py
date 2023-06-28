from pydantic import BaseModel


class ColoredTag(BaseModel):
    label: str
    color: str


class CommonInfo(BaseModel):
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

    tags: list[ColoredTag]
    """Tags"""

    is_official: bool
    """Whether an extension is official"""


class PluginInfo(CommonInfo):
    type: str
    """Plugin category"""

    supported_adapters: list[str]
    """Supported adapters"""