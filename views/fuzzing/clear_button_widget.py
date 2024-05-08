from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton

from controllers.fuzzing_controller.clear_button_controller import ClearButtonController


class ClearButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_clear_button()
        self.create_layout()

    def create_clear_button(self):
        self.clear_button = PrimaryPushButton(FIF.DELETE, "Clear")

        ClearButtonController.get_instance(self.clear_button)

    def create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.clear_button)

        self.setLayout(main_layout)
