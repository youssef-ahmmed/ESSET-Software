from controllers.intercept_controller.custom_data_checkbox_controller import CustomDataCheckboxController
from controllers.intercept_controller.custom_data_terminal_controller import CustomDataTerminalController
from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_replay_attack_data():
    replay_attack_validation = ReplayAttackValidation()

    try:
        if CustomDataCheckboxController.get_instance().is_custom_data_checkbox_enabled():
            replay_attack_validation.validate_custom_data_terminal()
        else:
            replay_attack_validation.validate_intercept_terminal()
        return True
    except InputValidationError as e:
        create_error_bar(str(e))
        return False


class InputValidationError(Exception):
    pass


class ReplayAttackValidation:

    def __init__(self):
        self.custom_data_terminal_controller = CustomDataTerminalController.get_instance()
        self.intercept_terminal_controller = InterceptTerminalController.get_instance()

    def validate_custom_data_terminal(self):
        if self.custom_data_terminal_controller.get_terminal_content() == "":
            raise InputValidationError(log_messages.NO_CUSTOM_TERMINAL_DATA)

    def validate_intercept_terminal(self):
        if self.intercept_terminal_controller.get_terminal_content() == "":
            raise InputValidationError(log_messages.NO_INTERCEPT_TERMINAL_DATA)
