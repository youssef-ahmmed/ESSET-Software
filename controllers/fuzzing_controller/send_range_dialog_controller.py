from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from core.configuration_writer import ConfigurationWriter
from core.data_processing import DataProcessing
from core.ftp_sender import FtpSender
from core.generator_based_fuzzing import GeneratorBasedFuzzing
from core.message_response_fuzzing_writer import MessageResponseFuzzingWriter
from models import log_messages
from reusable_functions.os_operations import join_paths
from validations.fuzzing_send_data_validations import validate_send_data
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar, create_error_bar
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

        self.send_range_dialog.accept()
        self.prepare_and_send_fuzzing_data(range_generator_fuzzed_data)

    def get_start_range_number(self):
        return self.send_range_dialog.get_start_range_number()

    def get_end_range_number(self):
        return self.send_range_dialog.get_end_range_number()

    def prepare_and_send_fuzzing_data(self, generated_data):
        data_processing = DataProcessing(generated_data)
        data_as_hex_list = data_processing.combine_fuzzed_data_to_hex_list()

        MessageResponseFuzzingWriter(data_as_hex_list)
        self.set_files_paths()
        self.create_config_file()

        try:
            self.send_files_via_ftp()
            create_success_bar(log_messages.FUZZING_MESSAGES_SEND)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def set_files_paths(self):
        project_path = ProjectPathController.get_instance().get_project_path()
        self.local_config_file_path = join_paths(project_path, 'config.json')
        self.remote_config_file_path = 'config/config.json'

        self.local_data_file_path = join_paths(project_path, 'fuzzing_data.json')
        self.remote_data_file_path = 'fuzzing/fuzzing_data.json'

    def create_config_file(self):
        config_writer = ConfigurationWriter(operation="Fuzzing")
        config_writer.create_config_file(self.local_config_file_path)

    def send_files_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
        ftp_sender.send_file_via_ftp(self.local_data_file_path, self.remote_data_file_path)
