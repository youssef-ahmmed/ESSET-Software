from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.fuzzing_controller.data_operation_controller import DataOperationController
from controllers.fuzzing_controller.fuzzing_mode_controller import FuzzingModeController
from controllers.fuzzing_controller.fuzzing_terminal_controller import FuzzingTerminalController
from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from core.data_processing import DataProcessing
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from validations.fuzzing_input_validations import validate_fuzzing_inputs


class GenerateButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(generate_button: PrimaryPushButton = None):
        if GenerateButtonController._instance is None:
            GenerateButtonController._instance = GenerateButtonController(generate_button)
        return GenerateButtonController._instance

    def __init__(self, generate_button: PrimaryPushButton):
        super(GenerateButtonController, self).__init__(generate_button)

        self.generate_button = generate_button
        self.data_operation_controller = DataOperationController.get_instance()

        self.start_communication()

    def start_communication(self):
        self.generate_button.clicked.connect(self.generate_fuzzing_data)

    def generate_fuzzing_data(self):
        if not validate_fuzzing_inputs():
            return

        fuzzing_mode = FuzzingModeController.get_instance().get_selected_fuzzing_mode()

        if fuzzing_mode == "Generator":
            self.generation_based_fuzzing()
        elif fuzzing_mode == "Mutation":
            # TODO: Implementation of mutation based fuzzing
            pass

    def generation_based_fuzzing(self):
        number_of_messages = self.data_operation_controller.get_number_of_messages()
        number_of_bytes = self.data_operation_controller.get_number_bytes_input()
        date_type = self.data_operation_controller.get_selected_data_type()

        generator_fuzzing = GeneratorBasedFuzzing(int(number_of_messages), int(number_of_bytes))
        generator_fuzzing.generate_random_data_by_type(date_type)
        fuzzed_data = generator_fuzzing.get_fuzzed_data()

        data_processing = DataProcessing(fuzzed_data)
        data_as_string = data_processing.combine_fuzzed_data_to_string()

        FuzzingTerminalController.get_instance().write_text(data_as_string)
        ResponseTableController.get_instance().populate_response_table(fuzzed_data)
