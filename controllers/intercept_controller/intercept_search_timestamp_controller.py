from controllers.abstract_controller.search_timestamp_controller import SearchTimestampController
from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController
from models import log_messages
from views.common.info_bar import create_success_bar


class InterceptSearchTimestampController(SearchTimestampController):

    _instance = None

    @staticmethod
    def get_instance(intercept_search_timestamp=None):
        if InterceptSearchTimestampController._instance is None:
            InterceptSearchTimestampController._instance = InterceptSearchTimestampController(intercept_search_timestamp)
        return InterceptSearchTimestampController._instance

    def __init__(self, intercept_search_timestamp):
        super(InterceptSearchTimestampController, self).__init__(intercept_search_timestamp)
        self.start_communication()

    def start_communication(self):
        self.search_timestamp_widget.time_stamp_combobox.currentIndexChanged.connect(self.display_terminal_data)

    def display_terminal_data(self):
        InterceptTerminalController.get_instance().write_text(self.get_selected_option_data())
        create_success_bar(log_messages.DATA_DISPLAYED)
