from controllers.intercept_controller.custom_data_checkbox_controller import CustomDataCheckboxController
from controllers.intercept_controller.custom_data_terminal_controller import CustomDataTerminalController
from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController
from controllers.project_path_controller import ProjectPathController
from core.configuration_writer import ConfigurationWriter
from core.ftp_sender import FtpSender
from models import log_messages
from reusable_functions.file_operations import write_to_binary_file, read_binary_file
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_error_bar, create_success_bar


class ReplayAttackActionController:
    def __init__(self):
        self.local_config_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                                 'config.json')
        self.remote_config_file_path = 'config/config.json'

        self.local_data_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                               'data.bin')
        self.remote_data_file_path = 'data/data.bin'

        self.start_replay_attack()

    def start_replay_attack(self):
        try:
            self.create_config_file()
            self.create_data_file()
            self.send_files_via_ftp()
            create_success_bar(log_messages.REPLAY_ATTACK_SUCCESS)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def create_config_file(self):
        config_writer = ConfigurationWriter(operation="Replay Attack")
        config_writer.create_config_file(self.local_config_file_path)

    def create_data_file(self):
        if CustomDataCheckboxController.get_instance().is_custom_data_checkbox_enabled():
            data = CustomDataTerminalController.get_instance().get_terminal_content()
        else:
            data = InterceptTerminalController.get_instance().get_terminal_content()

        bytes_data = data.encode('latin1')
        write_to_binary_file(self.local_data_file_path, bytes_data)
        print(read_binary_file(self.local_data_file_path))

    def send_files_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
        ftp_sender.send_file_via_ftp(self.local_data_file_path, self.remote_data_file_path)
