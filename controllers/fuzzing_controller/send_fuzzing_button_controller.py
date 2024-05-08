from PyQt5.QtCore import QObject

from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from core.data_processing import DataProcessing
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from core.message_response_fuzzing_writer import MessageResponseFuzzingWriter
from models import log_messages
from validations.fuzzing_send_data_validations import validate_send_data
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar
from views.fuzzing.response_table_buttons import ResponseTableButtons


class SendFuzzingButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(send_button: ResponseTableButtons = None):
        if SendFuzzingButtonController._instance is None:
            SendFuzzingButtonController._instance = SendFuzzingButtonController(send_button)
        return SendFuzzingButtonController._instance

    def __init__(self, send_button: ResponseTableButtons):
        super(SendFuzzingButtonController, self).__init__(send_button)

        self.send_all = send_button.send_all_action
        self.send_selected_message = send_button.send_selected_message_action

        self.start_communication()

    def start_communication(self):
        self.send_all.triggered.connect(self.send_all_generator_fuzzing_data)
        self.send_selected_message.triggered.connect(
            self.send_selected_generator_fuzzing_data
        )

    def send_all_generator_fuzzing_data(self):
        if not validate_send_data() or not validate_project_path():
            return

        generator_fuzzed_data = GeneratorBasedFuzzing.get_fuzzed_data()
        data_processing = DataProcessing(generator_fuzzed_data)
        data_as_hex_list = data_processing.combine_fuzzed_data_to_hex_list()

        MessageResponseFuzzingWriter(data_as_hex_list)
        create_success_bar(log_messages.FUZZING_MESSAGES_SEND)

    def send_selected_generator_fuzzing_data(self):
        if not validate_send_data(send_selected=True) or not validate_project_path():
            return

        messages_indices = ResponseTableController.get_instance().get_messages_indices_from_selected_rows()
        generator_fuzzed_data = GeneratorBasedFuzzing.get_fuzzed_data()
        selected_messages = []

        for index in messages_indices:
            selected_messages.append(generator_fuzzed_data[index])

        data_processing = DataProcessing(selected_messages)
        data_as_hex_list = data_processing.combine_fuzzed_data_to_hex_list()

        MessageResponseFuzzingWriter(data_as_hex_list)
        create_success_bar(log_messages.FUZZING_MESSAGES_SEND)
