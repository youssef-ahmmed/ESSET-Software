from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from views.sniffing.comm_protocol_select import CommunicationSettingsWidget
from views.sniffing.configuration_buttons import ConfigurationButtons
from views.sniffing.no_bits_select import BitsNumberSettingsWidget
from views.sniffing.output_terminal import TerminalWidget
from views.sniffing.select_channel_button import SelectChannelPins
from views.sniffing.vhdl_editor_buttons import VhdlEditorButtons
from views.sniffing.vhdl_widget import VhdlWidget


class SniffingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.vhdl_widget = VhdlWidget()
        self.vhdl_editor_buttons = VhdlEditorButtons()
        self.comm_protocol = CommunicationSettingsWidget()
        self.no_bits = BitsNumberSettingsWidget()
        self.channel_button = SelectChannelPins()
        self.channel_button.setEnabled(False)
        self.terminal = TerminalWidget()
        self.configuration_buttons = ConfigurationButtons()

        self.init_ui()
        self.start_ui_communication()

    def init_ui(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.vhdl_widget)
        left_layout.addWidget(self.vhdl_editor_buttons)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.comm_protocol)
        right_layout.addWidget(self.no_bits)
        right_layout.addWidget(self.channel_button)
        right_layout.addWidget(self.terminal)
        right_layout.addWidget(self.configuration_buttons)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

    def start_ui_communication(self):
        self.comm_protocol.protocol_combo.currentIndexChanged.connect(self.handle_comm_protocol_change)
        self.no_bits.bits_combo.currentIndexChanged.connect(self.handle_bits_number_change)

    def handle_comm_protocol_change(self):
        selected_protocol = self.comm_protocol.get_selected_protocol()
        if selected_protocol == "Select Comm Protocol":
            self.no_bits.setEnabled(True)
        else:
            self.no_bits.setEnabled(False)
            self.channel_button.setEnabled(True)

    def handle_bits_number_change(self):
        selected_bits_number = self.no_bits.get_selected_pin_number()
        if selected_bits_number == "Select bits number":
            self.comm_protocol.setEnabled(True)

        else:
            self.comm_protocol.setEnabled(False)
            self.channel_button.setEnabled(True)
