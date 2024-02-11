from controllers.display_controller.display_terminal_controller import DisplayTerminalController
from models import log_messages
from views.common.info_bar import create_success_bar, create_error_bar


class AbstractDataDisplay:
    def __init__(self, parent=None):
        self.parent = parent

    def display_data_on_terminal(self, data):
        if data:
            for row in range(len(data)):
                DisplayTerminalController.get_instance().append_text(str(data[row].channel_data)[2:-1])
            create_success_bar(self.parent, 'SUCCESS', log_messages.TIMESTAMP_SET)
        else:
            DisplayTerminalController.get_instance().write_text('')
            create_error_bar(self.parent, 'ERROR', log_messages.NO_TIMESTAMP_SET)
