from controllers.intercept_controller.stream_finder_input_controller import StreamFinderInputController
from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_stream_finder():
    attack_operation = AttackOperationSelectController.get_instance().get_selected_attack_operation()
    if attack_operation in ["Conditional Bypass", "Stream Finder"]:
        stream_finder_validation = StreamFinderValidation()

        try:
            stream_finder_validation.validate_stream_finder_input()
            return True
        except InputValidationError as e:
            create_error_bar(str(e))
            return False
    else:
        return True


class InputValidationError(Exception):
    pass


class StreamFinderValidation:

    def __init__(self):
        self.stream_finder_input_controller = StreamFinderInputController.get_instance()

    def validate_stream_finder_input(self):
        if self.stream_finder_input_controller.get_input_stream() == "":
            raise InputValidationError(log_messages.NO_STREAM_FINDER_INPUT)
