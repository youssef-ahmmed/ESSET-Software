from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import FluentIcon as FIF


class SendButton(QWidget):
    def __init__(self):
        super().__init__()

        self.send_button = PrimaryPushButton(FIF.SEND, "Send")

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.send_button)

