from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.fuzzing_controller.data_operation_controller import DataOperationController
from controllers.fuzzing_controller.fuzzing_mode_controller import FuzzingModeController
from controllers.fuzzing_controller.fuzzing_terminal_controller import FuzzingTerminalController
from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from controllers.template_generator_controller.fuzzing_templates_generator import FuzzingTemplatesGenerator
from core.data_processing import DataProcessing
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from models import log_messages
from validations.fuzzing_input_validations import validate_fuzzing_inputs
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar


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
        if not validate_fuzzing_inputs() or not validate_project_path():
            return

        self.generation_based_fuzzing()
        fuzzing_templates_generator = FuzzingTemplatesGenerator()
        fuzzing_templates_generator.render_fuzzing_templates()
        create_success_bar(log_messages.FUZZING_DATA_GENERATED)

    def generation_based_fuzzing(self):
        number_of_messages = self.data_operation_controller.get_number_of_messages()
        number_of_bytes = self.data_operation_controller.get_number_bytes_input()
        date_type = self.data_operation_controller.get_selected_data_type()

        generator_fuzzing = GeneratorBasedFuzzing(int(number_of_messages), int(number_of_bytes))
        generator_fuzzing.generate_random_data_by_type(date_type)
        fuzzed_data = generator_fuzzing.get_fuzzed_data()
        formatted_data = [
            [''.join(map(str, item)), 'None', 'None'] if isinstance(item, list) else [item, 'None', 'None']
            for item in fuzzed_data
        ]
        data_processing = DataProcessing(fuzzed_data)
        data_as_string = data_processing.combine_fuzzed_data_to_string()

        FuzzingTerminalController.get_instance().write_text(data_as_string)
        ResponseTableController.get_instance().populate_response_table(formatted_data)
