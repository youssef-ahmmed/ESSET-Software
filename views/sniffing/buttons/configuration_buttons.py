from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton

from controllers.sniffing_controller.buttons_controller.start_config_button_controller import \
    StartConfigButtonController
from controllers.sniffing_controller.buttons_controller.synthesis_button_controller import SynthesisButtonController


class ConfigurationButtons(QWidget):

    def __init__(self):
        super().__init__()
        self.start_config_button = PrimaryPushButton(FIF.IOT, 'Start Configuration')
        self.synthesis_button = PrimaryPushButton(FIF.ROBOT, 'Synthesis')

        SynthesisButtonController.get_instance(self.synthesis_button)
        StartConfigButtonController.get_instance(self.start_config_button)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.synthesis_button)
        self.layout().addWidget(self.start_config_button)
