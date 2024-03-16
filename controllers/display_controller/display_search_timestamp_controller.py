from controllers.abstract_controller.search_timestamp_controller import SearchTimestampController
from controllers.display_controller.display_terminal_controller import DisplayTerminalController
from models import log_messages
from views.common.info_bar import create_success_bar


class DisplaySearchTimestampController(SearchTimestampController):

    _instance = None

    @staticmethod
    def get_instance(display_search_timestamp=None):
        if DisplaySearchTimestampController._instance is None:
            DisplaySearchTimestampController._instance = DisplaySearchTimestampController(display_search_timestamp)
        return DisplaySearchTimestampController._instance

    def __init__(self, display_search_timestamp):
        super(DisplaySearchTimestampController, self).__init__(display_search_timestamp)
        self.start_communication()

    def start_communication(self):
        self.search_timestamp_widget.time_stamp_combobox.currentIndexChanged.connect(self.get_selected_start_time)

    def toggle_search_timestamp_combobox(self, enable=True):
        self.search_timestamp_widget.setEnabled(enable)

    def display_terminal_data(self):
        DisplayTerminalController.get_instance().write_text(self.get_selected_option_data())
        create_success_bar(log_messages.DATA_DISPLAYED)
