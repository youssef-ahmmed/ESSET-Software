from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from controllers.sniffing_controller.buttons_controller.start_sniffing_button_controller import \
    StartSniffingButtonController
from controllers.sniffing_controller.buttons_controller.synthesis_button_controller import SynthesisButtonController
from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController
from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class ConfigurationButtons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.synthesis_button = QPushButton('Synthesis')
        self.start_sniffing = QPushButton('Start Sniffing')
        self.sniffing_timer_dialog = SniffingTimer(self.start_sniffing)

        SynthesisButtonController.get_instance(self.synthesis_button)
        StartSniffingButtonController.get_instance(self.start_sniffing)
        SniffingTimerDialogController.get_instance(self.sniffing_timer_dialog)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.synthesis_button)
        self.layout().addWidget(self.start_sniffing)
