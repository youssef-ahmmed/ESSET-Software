from PyQt5.QtWidgets import QVBoxLayout, QWidget
from views.custom_component.custom_button import RoundButton
from channel_pins_dialog import ChannelPinsDialog


class SelectChannelPins(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Uart Settings")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.channel_pins_button = RoundButton("Select Channel Pins")
        self.channel_pins_button.clicked.connect(self.show_channel_pins_dialog)
        layout.addWidget(self.channel_pins_button)
        self.setLayout(layout)

    def show_channel_pins_dialog(self):
        dialog = ChannelPinsDialog()
        dialog.exec_()

