from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from views.display.channel_buttons import ChannelButtons
from views.display.search_timestamp import SearchTimestamp
from views.custom_component.output_terminal import OutputTerminal


class DisplaySettingsWidget(QWidget):

    channel_visibility = pyqtSignal(int)
    show_plots = pyqtSignal()
    clear_plots = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.channel_button = ChannelButtons()
        self.search_timestamp = SearchTimestamp()
        self.display_terminal = OutputTerminal()
        self.display_button = QPushButton("Display")

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.search_timestamp)
        self.layout().addWidget(self.display_terminal)
        self.layout().addWidget(self.display_button)

    def start_communication(self):
        self.channel_button.channel_visibility.connect(self.emit_channel_button_clicked)
        self.channel_button.show_plots.connect(lambda: self.show_plots.emit())
        self.channel_button.clear_plots.connect(lambda: self.clear_plots.emit())

    def emit_channel_button_clicked(self, button_number):
        self.channel_visibility.emit(button_number)
