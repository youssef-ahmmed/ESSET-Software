from PyQt5.QtCore import QObject

from controllers.display_controller.last_data_checkbox_controller import LastDataCheckboxController
from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from controllers.display_controller.waveform_controller import WaveformController


class DisplayButtonController(QObject):

    _instance = None

    @staticmethod
    def get_instance(display_button=None, parent=None):
        if DisplayButtonController._instance is None:
            DisplayButtonController._instance = DisplayButtonController(display_button, parent)
        return DisplayButtonController._instance

    def __init__(self, display_button, parent=None):
        super(DisplayButtonController, self).__init__()

        if DisplayButtonController._instance is not None:
            raise Exception("An instance of DisplayButtonController already exists. Use get_instance() to access it.")

        self.display_button = display_button
        self.parent = parent

        self.start_communication()

    def start_communication(self):
        self.display_button.clicked.connect(self.display_data)

    def display_data(self):
        state = LastDataCheckboxController.get_instance().is_last_data_checkbox_enabled()
        if state:
            LastDataCheckboxController.get_instance().display_terminal_data()
        else:
            SearchTimestampController.get_instance().display_terminal_data()

        WaveformController.get_instance().assign_channel_info_to_plot_widget()
