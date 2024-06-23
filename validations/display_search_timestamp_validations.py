from controllers.display_controller.display_search_timestamp_controller import DisplaySearchTimestampController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_search_timestamp():
    search_timestamp_validation = DisplaySearchTimestampValidation()

    try:
        search_timestamp_validation.validate_display_search_timestamp()

        return True
    except InputValidationError as e:
        create_error_bar(str(e))
        return False


class InputValidationError(Exception):
    pass


class DisplaySearchTimestampValidation:

    def __init__(self):
        self.display_search_timestamp_controller = DisplaySearchTimestampController.get_instance()

    def validate_display_search_timestamp(self):
        if self.display_search_timestamp_controller.get_selected_timestamp() == "Choose Time Stamp":
            raise InputValidationError(log_messages.NO_TIMESTAMP_SET)
