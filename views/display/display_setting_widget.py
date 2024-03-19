from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton

from controllers.display_controller.display_button_controller import DisplayButtonController
from controllers.display_controller.display_terminal_controller import DisplayTerminalController
from controllers.display_controller.last_data_checkbox_controller import LastDataCheckboxController
from controllers.display_controller.display_search_timestamp_controller import DisplaySearchTimestampController
from views.common.output_terminal import OutputTerminal
from views.display.channel_buttons import ChannelButtons
from views.display.last_data_checkbox import LastDataCheckbox
from views.common.search_timestamp import SearchTimestamp


class DisplaySettingsWidget(QWidget):

    channel_visibility = pyqtSignal(int)
    show_plots = pyqtSignal()
    clear_plots = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.channel_button = ChannelButtons()
        self.search_timestamp = SearchTimestamp()
        self.display_terminal = OutputTerminal()
        self.last_data_checkbox = LastDataCheckbox()
        self.display_button = PrimaryPushButton(FIF.TRAIN, "Display")

        DisplaySearchTimestampController.get_instance(self.search_timestamp)
        DisplayTerminalController.get_instance(self.display_terminal.terminal)
        DisplayButtonController.get_instance(self.display_button)
        LastDataCheckboxController.get_instance(self.last_data_checkbox.last_data_checkbox)

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.channel_button)
        self.layout().addWidget(self.search_timestamp)
        self.layout().addWidget(self.last_data_checkbox)
        self.layout().addWidget(self.display_terminal)
        self.layout().addWidget(self.display_button)

    def start_communication(self):
        self.channel_button.channel_visibility.connect(self.emit_channel_button_clicked)
        self.channel_button.show_plots.connect(lambda: self.show_plots.emit())
        self.channel_button.clear_plots.connect(lambda: self.clear_plots.emit())

    def emit_channel_button_clicked(self, button_number):
        self.channel_visibility.emit(button_number)
