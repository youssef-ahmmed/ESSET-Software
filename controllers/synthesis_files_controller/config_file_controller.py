from controllers.project_path_controller import ProjectPathController
from core.configuration_writer import ConfigurationWriter
from core.ftp_sender import FtpSender
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths


class ConfigFileController:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigFileController._instance is None:
            ConfigFileController._instance = ConfigFileController()
        return ConfigFileController._instance

    def __init__(self):
        super(ConfigFileController, self).__init__()
        if ConfigFileController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.config_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                           'config.json')

    def send_config_file(self, programming: bool = False, operation: str = "", timer: int = 0):
        ConfigurationWriter(programming, operation, timer).create_config_file(self.config_file_path)
        remote_file_path = 'config/config.json'
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.config_file_path, remote_file_path)
