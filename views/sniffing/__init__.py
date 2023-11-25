import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from comm_protocol_select import CommunicationSettingsWidget
from no_bits_select import BitsNumberSettingsWidget
from select_channel_button import SelectChannelPins
from views.custom_component.custom_button import RoundButton
from output_terminal import TerminalWidget


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        v_layout = QVBoxLayout(central_widget)

        self.comm_protocol = CommunicationSettingsWidget()
        self.no_bits = BitsNumberSettingsWidget()
        self.channel_button = SelectChannelPins()
        self.channel_button.setEnabled(False)
        self.terminal = TerminalWidget()
        self.start_sniffing = RoundButton('Start Sniffing')

        v_layout.addWidget(self.comm_protocol)
        v_layout.addWidget(self.no_bits)
        v_layout.addWidget(self.channel_button)
        v_layout.addWidget(self.terminal)
        v_layout.addWidget(self.start_sniffing)

        self.comm_protocol.protocol_combo.currentIndexChanged.connect(self.handle_comm_protocol_change)
        self.no_bits.bits_combo.currentIndexChanged.connect(self.handle_bits_number_change)

        self.setCentralWidget(central_widget)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
