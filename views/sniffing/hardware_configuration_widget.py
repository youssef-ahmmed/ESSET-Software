from PyQt5.QtWidgets import QWidget, QVBoxLayout

from views.sniffing.comm_protocol_select import CommunicationProtocolSelect
from views.sniffing.configuration_buttons import ConfigurationButtons
from views.sniffing.number_bits_select import NumberBitsSelect
from views.sniffing.output_terminal import OutputTerminal
from views.sniffing.select_channel_pins_button import SelectChannelPinsButton


class HardwareConfigurations(QWidget):

    def __init__(self):
        super().__init__()

        self.comm_protocol = CommunicationProtocolSelect()
        self.no_bits = NumberBitsSelect()
        self.channel_button = SelectChannelPinsButton()
        self.channel_button.setEnabled(False)
        self.terminal = OutputTerminal()
        self.configuration_buttons = ConfigurationButtons()

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
            self.channel_button.setEnabled(False)

        else:
            self.no_bits.setEnabled(False)
            self.channel_button.setEnabled(True)

    def handle_bits_number_change(self):
        selected_bits_number = self.no_bits.get_selected_pin_number()
        if selected_bits_number == "Select bits number":
            self.comm_protocol.setEnabled(True)

        elif selected_bits_number == "None":
            self.comm_protocol.setEnabled(True)
            self.channel_button.setEnabled(False)

        else:
            self.comm_protocol.setEnabled(False)
            self.channel_button.setEnabled(True)
