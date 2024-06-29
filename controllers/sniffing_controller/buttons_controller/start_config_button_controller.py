from subprocess import CalledProcessError

from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.store_sniffing_configurations_controller import \
    StoreSniffingConfigurationsController
from controllers.synthesis_files_controller.sof_file_controller import SofFileController
from core.command_executor import CommandExecutor
from core.configuration_writer import ConfigurationWriter
from core.ftp_sender import FtpSender
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths
from validations.project_path_validations import validate_project_path
from validations.sof_file_validations import validate_sof_file
from views.common.info_bar import create_error_bar, create_success_bar


class StartConfigButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_config_button: PrimaryPushButton = None):
        if StartConfigButtonController._instance is None:
            StartConfigButtonController._instance = StartConfigButtonController(start_config_button)
        return StartConfigButtonController._instance

    def __init__(self, start_config_button: PrimaryPushButton) -> None:
        super(StartConfigButtonController, self).__init__()

        if StartConfigButtonController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.start_config_button = start_config_button
        self.project_path_controller = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self):
        self.start_config_button.clicked.connect(self.start_configuration)

    def start_configuration(self) -> None:
        if not validate_project_path() or not validate_sof_file():
            return

        try:
            self.set_files_paths()
            self.generate_svf_file()
            self.create_config_file()
            self.send_files_via_ftp()
            store_sniffing_configurations_controller = StoreSniffingConfigurationsController()
            store_sniffing_configurations_controller.store_sniffing_configurations()
            create_success_bar(log_messages.CONFIGURATION_SUCCESS)
        except CalledProcessError:
            create_error_bar(log_messages.NO_ENV_PATH)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def set_files_paths(self):
        self.project_path = self.project_path_controller.get_project_path()
        self.local_config_file_path = join_paths(self.project_path, 'config.json')
        self.remote_config_file_path = 'config/config.json'
        self.local_svf_file_path = join_paths(self.project_path, 'top_level.svf')
        self.remote_svf_file_path = 'svf/top_level.svf'

    def generate_svf_file(self) -> None:
        input_sof_file = SofFileController.get_instance().get_sof_file_path()
        output_svf_file = join_paths(self.project_path, 'output_files', 'top_level.svf')
        quartus_cpf_command = f"quartus_cpf -c -q 25MHz -g 3.3 -n p {input_sof_file} {output_svf_file}"
        CommandExecutor(quartus_cpf_command).execute_command()

    def create_config_file(self):
        config_writer = ConfigurationWriter(programming=True)
        config_writer.create_config_file(self.local_config_file_path)

    def send_files_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
        ftp_sender.send_file_via_ftp(self.local_svf_file_path, self.remote_svf_file_path)
