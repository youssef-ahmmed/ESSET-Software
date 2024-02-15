from PyQt5.QtWidgets import QWidget, QVBoxLayout

from controllers.sniffing_controller.buttons_controller.channel_pins_button_controller import \
    ChannelPinsButtonController
from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.dialogs_controller.bits_input_dialog_controller import BitsInputDialogController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController
from controllers.sniffing_controller.terminal_controller import TerminalController
from views.custom_component.output_terminal import OutputTerminal
from views.sniffing.buttons.configuration_buttons import ConfigurationButtons
from views.sniffing.buttons.select_channel_pins_button import SelectChannelPinsButton
from views.sniffing.comm_protocol_select import CommunicationProtocolSelect
from views.sniffing.dialogs.bits_input_dialog import BitsInputDialog
from views.sniffing.number_bits_select import NumberBitsSelect


class HardwareConfigurations(QWidget):

    def __init__(self, parent):
        super().__init__()

        bits_input_dialog = BitsInputDialog()
        BitsInputDialogController.get_instance(parent, bits_input_dialog)

        self.comm_protocol = CommunicationProtocolSelect(parent)
        CommProtocolSelectController.get_instance(self.comm_protocol)

        self.no_bits = NumberBitsSelect()
        NumberBitsSelectController.get_instance(self.no_bits, bits_input_dialog)

        self.channel_button = SelectChannelPinsButton(parent)
        ChannelPinsButtonController.get_instance(self.channel_button, parent)

        self.terminal = OutputTerminal()
        self.configuration_buttons = ConfigurationButtons(parent)

        TerminalController.get_instance(self.terminal.terminal)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.comm_protocol)
        self.layout().addWidget(self.no_bits)
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.terminal)
        self.layout().addWidget(self.configuration_buttons)
