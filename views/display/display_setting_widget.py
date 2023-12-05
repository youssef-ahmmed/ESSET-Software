from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from views.display.channel_buttons import ChannelButton
from views.display.search_timestamp import SearchTimestamp
from views.custom_component.output_terminal import OutputTerminal


class DisplaySettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.channel_button = ChannelButton()
        self.search_timestamp = SearchTimestamp()
        self.display_terminal = OutputTerminal()
        self.display_button = QPushButton("Display")

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.search_timestamp)
        self.layout().addWidget(self.display_terminal)
        self.layout().addWidget(self.display_button)
