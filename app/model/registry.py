from pydantic import BaseModel


class ColoredTag(BaseModel):
    """Tag with color"""

    label: str
    color: str


class CommonInfo(BaseModel):
    """Common info for drivers, adapters and plugins"""

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
    """Plugin info model"""
    # Some plugins are still not prepared for these metadata, so `None` is still needed
    # for now, until the registry is ready for all plugins.

    type: str | None
    """Plugin category"""

    supported_adapters: list[str] | None
    """Supported adapters"""