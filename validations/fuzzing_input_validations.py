from controllers.fuzzing_controller.data_operation_controller import DataOperationController
from controllers.fuzzing_controller.fuzzing_mode_controller import FuzzingModeController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_fuzzing_inputs():
    fuzzing_input_validation = FuzzingInputValidation()

    try:
        fuzzing_input_validation.validate_data_type()
        fuzzing_input_validation.validate_number_of_message()
        fuzzing_input_validation.validate_number_of_bytes()
        fuzzing_input_validation.validate_fuzzing_on()
        fuzzing_input_validation.validate_sniffing_on()
        fuzzing_input_validation.validate_fuzzing_mode()

        return True
    except InputValidationError as e:
        create_error_bar(str(e))
        return False


class InputValidationError(Exception):
    pass


class FuzzingInputValidation:

    def __init__(self):
        self.data_operation_controller = DataOperationController.get_instance()

    def validate_data_type(self):
        data_type = self.data_operation_controller.get_selected_data_type()

        if data_type == "Choose":
            raise InputValidationError(log_messages.DATA_TYPE_ERROR)

    def validate_number_of_message(self):
        number_of_message = self.data_operation_controller.get_number_of_messages()

        if not number_of_message:
            raise InputValidationError(log_messages.NO_NUMBER_OF_MESSAGES)

        if int(number_of_message) <= 0:
            raise InputValidationError(log_messages.NEGATIVE_NUMBER_OF_MESSAGES)

    def validate_number_of_bytes(self):
        number_of_bytes = self.data_operation_controller.get_number_bytes_input()

        if not number_of_bytes:
            raise InputValidationError(log_messages.NO_NUMBER_OF_BYTES)

        if int(number_of_bytes) <= 0:
            raise InputValidationError(log_messages.NEGATIVE_NUMBER_OF_BYTES)

    def validate_fuzzing_on(self):
        fuzzing_on = self.data_operation_controller.get_selected_fuzzing_protocol()

        if fuzzing_on == "Choose":
            raise InputValidationError(log_messages.NO_FUZZING_ON)

    def validate_sniffing_on(self):
        sniffing_on = self.data_operation_controller.get_selected_sniffing_protocol()

        if sniffing_on == "Choose":
            raise InputValidationError(log_messages.NO_SNIFFING_ON)

    def validate_fuzzing_mode(self):
        fuzzing_mode = FuzzingModeController.get_instance().get_selected_fuzzing_mode()

        if not fuzzing_mode:
            raise InputValidationError(log_messages.NO_FUZZING_MODE)
