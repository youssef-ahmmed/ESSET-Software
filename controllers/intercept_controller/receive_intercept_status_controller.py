from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.project_path_controller import ProjectPathController
from core.ftp_receiver import FtpReceiver
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.file_operations import read_binary_file
from reusable_functions.os_operations import join_paths
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar, create_error_bar


class ReceiveInterceptStatusController(QObject):

    _instance = None

    @staticmethod
    def get_instance(receive_intercept_status: PrimaryPushButton = None):
        if ReceiveInterceptStatusController._instance is None:
            ReceiveInterceptStatusController._instance = ReceiveInterceptStatusController(receive_intercept_status)
        return ReceiveInterceptStatusController._instance

    def __init__(self, receive_intercept_status):
        super(ReceiveInterceptStatusController, self).__init__()

        if ReceiveInterceptStatusController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.receive_intercept_status = receive_intercept_status

        self.start_communication()

    def start_communication(self):
        self.receive_intercept_status.clicked.connect(self.receive_condition_status)

    @staticmethod
    def receive_condition_status():
        if not validate_project_path():
            return

        try:
            ftp_receiver = FtpReceiver()
            local_file_path = join_paths(ProjectPathController.get_instance().get_project_path(), 'stream.bin')
            remote_file_path = 'intercept/stream.bin'
            ftp_receiver.receive_file_via_ftp(local_file_path, remote_file_path)
            condition = int(read_binary_file(local_file_path), 16)
            if condition:
                create_success_bar(log_messages.CONDITION_FOUND)
            else:
                create_error_bar(log_messages.CONDITION_NOT_FOUND)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)
