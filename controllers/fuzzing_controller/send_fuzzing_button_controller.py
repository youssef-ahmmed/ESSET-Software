from PyQt5.QtCore import QObject

from controllers.fuzzing_controller.response_table_controller import ResponseTableController
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
        self.prepare_and_send_fuzzing_data(generator_fuzzed_data)

    def send_selected_generator_fuzzing_data(self):
        if not validate_send_data(send_selected=True) or not validate_project_path():
            return

        messages_indices = ResponseTableController.get_instance().get_messages_indices_from_selected_rows()
        generator_fuzzed_data = GeneratorBasedFuzzing.get_fuzzed_data()
        selected_messages = []

        for index in messages_indices:
            selected_messages.append(generator_fuzzed_data[index])

        self.prepare_and_send_fuzzing_data(selected_messages)

    def prepare_and_send_fuzzing_data(self, generated_data):
        data_processing = DataProcessing(generated_data)
        data_as_hex_list = data_processing.combine_fuzzed_data_to_hex_list()

        MessageResponseFuzzingWriter(data_as_hex_list)
        self.set_files_paths()
        self.create_config_file()

        try:
            self.send_fuzzing_data_via_ftp()
            self.send_config_via_ftp()
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

    def send_fuzzing_data_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_data_file_path, self.remote_data_file_path)

    def send_config_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
