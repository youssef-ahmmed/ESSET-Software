from datetime import datetime, timedelta

from PyQt5.QtCore import QObject
from qfluentwidgets import Action

from controllers.project_path_controller import ProjectPathController
from core.ftp_receiver import FtpReceiver
from models import log_messages
from models.dao.sniffed_data_dao import SniffedDataDao
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_error_bar, create_success_bar


class ReceiveButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(parent=None, receive_data_button: Action = None) -> None:
        if ReceiveButtonController._instance is None:
            ReceiveButtonController._instance = ReceiveButtonController(parent, receive_data_button)
        return ReceiveButtonController._instance

    def __init__(self, parent, receive_data_button: Action) -> None:
        super(ReceiveButtonController, self).__init__()

        if ReceiveButtonController._instance is not None:
            raise Exception("An instance of ReceiveButtonController already exists. "
                            "Use get_instance() to access it.")

        self.receive_data_button = receive_data_button
        self.parent = parent

        self.start_communication()

    def start_communication(self) -> None:
        self.receive_data_button.triggered.connect(self.receive_sniffed_data)

    def receive_sniffed_data(self):
        if not self.check_time_taken_passed():
            return
        self.initiate_ftp_connection()
        create_success_bar(self.parent, 'SUCCESS', log_messages.RECEIVED_SUCCESS)

    def check_time_taken_passed(self) -> bool:
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()
        start_time, time_taken = SniffedDataDao.get_start_time_and_time_taken(last_sniffed_data_id)

        finished_sniffing_time = start_time + timedelta(seconds=time_taken)
        if datetime.now() < finished_sniffing_time:
            create_error_bar(self.parent, 'ERROR', log_messages.SNIFFING_NOT_FINISHED)
            return False

        return True

    @staticmethod
    def initiate_ftp_connection():
        local_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                     'data.txt')
        remote_file_path = 'Sniffing/data.txt'
        ftp_receiver = FtpReceiver()
        ftp_receiver.receive_file_via_ftp(local_file_path, remote_file_path)
