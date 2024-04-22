from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton


class GenerateButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_generate_button()
        self.create_layout()

    def create_generate_button(self):
        self.generate_button = PrimaryPushButton(FIF.ACCEPT, "Generate")

    def create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.generate_button)

        self.setLayout(main_layout)
