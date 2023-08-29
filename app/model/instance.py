from msgspec import Struct


class InstanceMetadata(Struct):
    id: str
    """实例的唯一ID，由数据库生成"""

    name: str
    """实例的名称，由用户自由命名"""

    path: str
    """实例在本地的路径"""

    driver: str
    """实例所使用的驱动器"""

    adapter: str
    """实例所使用的适配器"""

    plugin_list: list[str]
    """实例安装的插件列表"""
