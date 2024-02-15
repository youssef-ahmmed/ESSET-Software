from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF, RoundMenu, Action, PrimarySplitPushButton
from qfluentwidgets import PrimaryPushButton

from controllers.sniffing_controller.buttons_controller.receive_button_controller import ReceiveButtonController
from controllers.sniffing_controller.buttons_controller.start_sniffing_button_controller import \
    StartSniffingButtonController
from controllers.sniffing_controller.buttons_controller.synthesis_button_controller import SynthesisButtonController
from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController
from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class ConfigurationButtons(QWidget):

    def __init__(self):
        super().__init__()
        self.start_sniffing = PrimarySplitPushButton(FIF.IOT, 'Start Sniffing')
        self.synthesis_button = PrimaryPushButton(FIF.ROBOT, 'Synthesis')
        self.sniffing_timer_dialog = SniffingTimer(self.start_sniffing)

        SynthesisButtonController.get_instance(self.synthesis_button)
        StartSniffingButtonController.get_instance(self.start_sniffing)
        SniffingTimerDialogController.get_instance(self.sniffing_timer_dialog)

        self.init_ui()
        self.create_sniffing_options()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.synthesis_button)
        self.layout().addWidget(self.start_sniffing)

    def create_sniffing_options(self):
        sniffing_button_option = RoundMenu()
        receive_data_button = Action(FIF.LINK, 'Receive Data')
        sniffing_button_option.addAction(receive_data_button)
        self.start_sniffing.setFlyout(sniffing_button_option)

        ReceiveButtonController.get_instance(receive_data_button)
