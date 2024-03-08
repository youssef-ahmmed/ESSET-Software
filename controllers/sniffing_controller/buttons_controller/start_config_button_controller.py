from subprocess import CalledProcessError

from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.project_path_controller import ProjectPathController
from controllers.synthesis_files_controller.config_file_controller import ConfigFileController
from controllers.synthesis_files_controller.sof_file_controller import SofFileController
from core.command_executor import CommandExecutor
from core.ftp_sender import FtpSender
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths
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
        if not self.project_path_controller.is_project_path_exists():
            create_error_bar(log_messages.NO_QUARTUS_PATH)
            return

        sof_file_path = SofFileController.get_instance().get_sof_file_path()
        if not sof_file_path:
            create_error_bar(log_messages.NO_SOF_FILE)
            return

        try:
            self.generate_svf_file()
            self.send_svf_file()
            ConfigFileController.get_instance().send_config_file(True)
            create_success_bar(log_messages.CONFIGURATION_SUCCESS)
        except CalledProcessError:
            create_error_bar(log_messages.NO_ENV_PATH)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def generate_svf_file(self) -> None:
        input_sof_file = SofFileController.get_instance().get_sof_file_path()
        self.output_svf_file = join_paths(self.project_path_controller.get_project_path(),
                                          'output_files', 'top_level.svf')
        quartus_cpf_command = f"quartus_cpf -c -q 25MHz -g 3.3 -n p {input_sof_file} {self.output_svf_file}"
        CommandExecutor(quartus_cpf_command).execute_command()

    def send_svf_file(self):
        remote_file_path = 'svf/top_level.svf'
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.output_svf_file, remote_file_path)
