from PyQt5.QtCore import QObject

from controllers.display_controller.last_data_checkbox_controller import LastDataCheckboxController
from controllers.display_controller.display_search_timestamp_controller import DisplaySearchTimestampController
from controllers.display_controller.waveform_controller import WaveformController
from models.log_messages import instance_exists_error
from validations.display_search_timestamp_validations import validate_search_timestamp


class DisplayButtonController(QObject):

    _instance = None

    @staticmethod
    def get_instance(display_button=None):
        if DisplayButtonController._instance is None:
            DisplayButtonController._instance = DisplayButtonController(display_button)
        return DisplayButtonController._instance

    def __init__(self, display_button):
        super(DisplayButtonController, self).__init__()

        if DisplayButtonController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.display_button = display_button

        self.start_communication()

    def start_communication(self):
        self.display_button.clicked.connect(self.display_data)

    @staticmethod
    def display_data():
        state = LastDataCheckboxController.get_instance().is_last_data_checkbox_enabled()
        if state:
            LastDataCheckboxController.get_instance().display_terminal_data()
        else:
            if not validate_search_timestamp():
                return
            DisplaySearchTimestampController.get_instance().display_terminal_data()

        WaveformController.get_instance().assign_channel_info_to_plot_widget()
