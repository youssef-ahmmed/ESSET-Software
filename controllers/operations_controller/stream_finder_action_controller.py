from controllers.project_path_controller import ProjectPathController
from core.configuration_writer import ConfigurationWriter
from core.ftp_sender import FtpSender
from models import log_messages
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_success_bar, create_error_bar


class StreamFinderActionController: 
    def __init__(self):
        self.local_config_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                                 'config.json')
        self.remote_config_file_path = 'config/config.json'

        self.start_stream_finder()

    def start_stream_finder(self):
        try:
            self.create_config_file()
            self.send_files_via_ftp()
            create_success_bar(log_messages.STREAM_FINDER_SUCCESS)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def create_config_file(self):
        config_writer = ConfigurationWriter(operation="Stream Finder")
        config_writer.create_config_file(self.local_config_file_path)

    def send_files_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
