from controllers.fuzzing_controller.data_operation_controller import DataOperationController
from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_send_data(start_range=None, end_range=None, send_selected=False):
    try:
        fuzzing_validations = FuzzingSendDataValidations()

        fuzzing_validations.send_all_data_validation()
        if start_range is not None and end_range is not None:
            fuzzing_validations.send_range_data_validation(start_range, end_range)
        elif send_selected:
            fuzzing_validations.send_selected_table_data()

        return True
    except DataValidationError as e:
        create_error_bar(str(e))
        return False


class DataValidationError(Exception):
    pass


class FuzzingSendDataValidations:

    @staticmethod
    def send_all_data_validation():
        data = GeneratorBasedFuzzing.get_fuzzed_data()
        if not data:
            raise DataValidationError(log_messages.NO_GENERATED_DATA)

    def send_range_data_validation(self, start_range, end_range):
        self.send_all_data_validation()

        if not (start_range and end_range):
            raise DataValidationError(log_messages.START_END_RANGE_NOT_EXIST)

        number_of_messages = DataOperationController.get_instance().get_number_of_messages()

        if not (1 <= int(start_range) <= int(number_of_messages)
                and 1 <= int(end_range) <= int(number_of_messages)):
            raise DataValidationError(log_messages.START_END_RANGE_ERROR)

    def send_selected_table_data(self):
        self.send_all_data_validation()

        if not ResponseTableController.get_instance().get_selected_rows():
            raise DataValidationError(log_messages.NO_SELECTED_ROWS)
