from qfluentwidgets import CardWidget


class ExtensionCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


class PluginCard(ExtensionCard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


class AdapterCard(ExtensionCard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
