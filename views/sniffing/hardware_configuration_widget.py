from PyQt5.QtWidgets import QWidget, QVBoxLayout

from controllers.sniffing_controller.bits_input_dialog_controller import BitsInputDialogController
from controllers.sniffing_controller.buttons_controller.channel_pins_button_controller import \
    ChannelPinsButtonController
from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController
from controllers.sniffing_controller.terminal_controller import TerminalController
from views.custom_component.output_terminal import OutputTerminal
from views.sniffing.dialogs.bits_input_dialog import BitsInputDialog
from views.sniffing.buttons.configuration_buttons import ConfigurationButtons
from views.sniffing.buttons.select_channel_pins_button import SelectChannelPinsButton
from views.sniffing.comm_protocol_select import CommunicationProtocolSelect
from views.sniffing.number_bits_select import NumberBitsSelect


class HardwareConfigurations(QWidget):

    def __init__(self):
        super().__init__()

        self.bits_input_dialog = BitsInputDialog("test")
        BitsInputDialogController.get_instance(self.bits_input_dialog)

        self.comm_protocol = CommunicationProtocolSelect()
        CommProtocolSelectController.get_instance(self.comm_protocol)

        self.no_bits = NumberBitsSelect()
        NumberBitsSelectController.get_instance(self.no_bits, self.bits_input_dialog)

        self.channel_button = SelectChannelPinsButton()
        ChannelPinsButtonController.get_instance(self.channel_button)

        self.terminal = OutputTerminal()
        self.configuration_buttons = ConfigurationButtons()

        TerminalController.get_instance(self.terminal.terminal)

        self.init_ui()
        self.start_ui_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.comm_protocol)
        self.layout().addWidget(self.no_bits)
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.terminal)
        self.layout().addWidget(self.configuration_buttons)

    def start_ui_communication(self):
        self.comm_protocol.protocol_combo.currentIndexChanged.connect(self.handle_comm_protocol_change)
        self.no_bits.bits_combo.currentIndexChanged.connect(self.handle_bits_number_change)

    def handle_comm_protocol_change(self):
        selected_protocol = self.comm_protocol.get_selected_protocol()
        if selected_protocol == "Select Comm Protocol":
            self.no_bits.setEnabled(True)

        elif selected_protocol == "None":
            self.no_bits.setEnabled(True)

        else:
            self.no_bits.setEnabled(False)

    def handle_bits_number_change(self):
        selected_bits_number = self.no_bits.get_selected_pin_number()
        if selected_bits_number == "Select bits number":
            self.comm_protocol.setEnabled(True)

        elif selected_bits_number == "None":
            self.comm_protocol.setEnabled(True)

        else:
            self.comm_protocol.setEnabled(False)
