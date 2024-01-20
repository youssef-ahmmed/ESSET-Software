from PyQt5.QtWidgets import QWidget

from views.sniffing.base_mode_widget import BaseModeWidget


class SimpleModeWidget(BaseModeWidget):
    def __init__(self):
        super().__init__(QWidget())
