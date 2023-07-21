# Nonebot-Desktop-Qt

Finally, a GUI program for Nonebot2

## :compass: Development Roadmap

* [ ] Instances management
  * [ ] Create instances
  * [ ] Open existing instances
  * [ ] Run instances
  * [ ] Remote Instance Management
* [ ] Log console
* [ ] Components management
  * [ ] Drivers install/uninstall/enable/disable
  * [ ] Adapters install/uninstall/enable/disable
  * [ ] Plugins install/uninstall/enable/disable
  * [ ] Built-in plugins enable/disable
* [ ] Configuration editing
  * [ ] Visualized config editor
    * [ ] DotEnv
    * [ ] JSON
    * [ ] YAML
    * [ ] TOML
  * [ ] Bind with config model from components
* [ ] Advanced
  * [ ] Import/export "botpack"
* [ ] Performance
  * [ ] Monitor startup performance and try to optimize
  * [ ] If the startup or initialization takes too long, create a startup screen


## :wave: Contributing

Code structure to be followed

```
from typing import Optional, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QObject


class Interface(Protocol):
    def __init__(self, parent: Optional["QObject"] = None) -> None:
        # super().__init__(parent)
        # Instantiating Data Structures
        # Instantiating Widget Objects
        # Instantiating Layout Objects
        # Initialize Widgets & Layouts
        ...

    def __init_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        # Set Geometry
        ...

    def __init_sub_widget(self) -> None:
        # Set Object Name
        # Set Widget Option & Policy
        # Set Geometry
        ...

    def __init_layout(self) -> None:
        # Set Layout Options
        # Place layout widgets
        ...

    def __init_sub_widget(self) -> None:
        # Set Layout Options
        # Place layout widgets
        ...

```