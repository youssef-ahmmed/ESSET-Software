from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton


class ResponseTableButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.send_button = PrimaryPushButton(FIF.SEND_FILL, "Send")
        self.cancel_button = PrimaryPushButton(FIF.CANCEL_MEDIUM, "Cancel")

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.send_button)
        self.layout().addWidget(self.cancel_button)
