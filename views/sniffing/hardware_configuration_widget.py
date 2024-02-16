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

        self.number_bits_select = NumberBitsSelect()
        NumberBitsSelectController.get_instance(self.number_bits_select, bits_input_dialog)

        self.channel_button = SelectChannelPinsButton(parent)

        self.terminal = OutputTerminal()
        self.configuration_buttons = ConfigurationButtons(parent)

        TerminalController.get_instance(self.terminal.terminal)

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.comm_protocol)
        self.layout().addWidget(self.number_bits_select)
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.terminal)
        self.layout().addWidget(self.configuration_buttons)

    def start_communication(self):
        self.number_bits_select.comm_protocol_changed.connect(
            self.set_protocol_combo_disabled
        )
        self.comm_protocol.sniff_number_bits_changed.connect(
            self.set_bits_combo_disabled
        )

    def set_bits_combo_disabled(self, disable):
        self.number_bits_select.bits_combo.setDisabled(disable)

    def set_protocol_combo_disabled(self, disable):
        self.comm_protocol.protocol_combo.setDisabled(disable)
