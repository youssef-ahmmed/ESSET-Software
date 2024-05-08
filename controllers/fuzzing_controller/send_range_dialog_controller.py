from PyQt5.QtCore import QObject

from core.data_processing import DataProcessing
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from core.message_response_fuzzing_writer import MessageResponseFuzzingWriter
from models import log_messages
from validations.fuzzing_send_data_validations import validate_send_data
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar
from views.fuzzing.send_range_dialog import SendRangeDialog


class SendRangeDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(send_range_dialog: SendRangeDialog = None):
        if SendRangeDialogController._instance is None:
            SendRangeDialogController._instance = SendRangeDialogController(send_range_dialog)
        return SendRangeDialogController._instance

    def __init__(self, send_range_dialog: SendRangeDialog):
        super(SendRangeDialogController, self).__init__(send_range_dialog)

        self.send_range_dialog = send_range_dialog
        self.cancel_button = send_range_dialog.cancel_button
        self.ok_button = send_range_dialog.ok_button

        self.start_communication()

    def start_communication(self):
        self.cancel_button.clicked.connect(self.send_range_dialog.reject)
        self.ok_button.clicked.connect(self.send_range_generator_fuzzing_data)

    def send_range_generator_fuzzing_data(self):
        start_range = self.get_start_range_number()
        end_range = self.get_end_range_number()

        if not validate_send_data(start_range, end_range) or not validate_project_path():
            return

        generator_fuzzed_data = GeneratorBasedFuzzing.get_fuzzed_data()
        range_generator_fuzzed_data = generator_fuzzed_data[int(start_range) - 1: int(end_range)]

        data_processing = DataProcessing(range_generator_fuzzed_data)
        data_as_hex_list = data_processing.combine_fuzzed_data_to_hex_list()

        MessageResponseFuzzingWriter(data_as_hex_list)

        self.send_range_dialog.accept()
        create_success_bar(log_messages.FUZZING_MESSAGES_SEND)

    def get_start_range_number(self):
        return self.send_range_dialog.get_start_range_number()

    def get_end_range_number(self):
        return self.send_range_dialog.get_end_range_number()
