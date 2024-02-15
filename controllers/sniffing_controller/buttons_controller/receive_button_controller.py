from datetime import datetime, timedelta

from PyQt5.QtCore import QObject
from qfluentwidgets import Action

from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from controllers.project_path_controller import ProjectPathController
from core.ftp_receiver import FtpReceiver
from models import log_messages
from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.sniffed_data_dao import SniffedDataDao
from reusable_functions.file_operations import delete_file, read_binary_file
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_error_bar, create_success_bar


class ReceiveButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(receive_data_button: Action = None) -> None:
        if ReceiveButtonController._instance is None:
            ReceiveButtonController._instance = ReceiveButtonController(receive_data_button)
        return ReceiveButtonController._instance

    def __init__(self, receive_data_button: Action) -> None:
        super(ReceiveButtonController, self).__init__()

        if ReceiveButtonController._instance is not None:
            raise Exception("An instance of ReceiveButtonController already exists. "
                            "Use get_instance() to access it.")

        self.receive_data_button = receive_data_button

        self.start_communication()

    def start_communication(self) -> None:
        self.receive_data_button.triggered.connect(self.receive_sniffed_data)

    def receive_sniffed_data(self):
        try:
            if not self.check_time_taken_passed():
                return
            self.initiate_ftp_connection()
            self.store_sniffed_data()
            SearchTimestampController.get_instance().update_timestamp_combobox()
            create_success_bar(log_messages.RECEIVED_SUCCESS)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def check_time_taken_passed(self) -> bool:
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()
        start_time, time_taken = SniffedDataDao.get_start_time_and_time_taken(last_sniffed_data_id)

        finished_sniffing_time = start_time + timedelta(seconds=time_taken)
        if datetime.now() < finished_sniffing_time:
            create_error_bar(log_messages.SNIFFING_NOT_FINISHED)
            return False

        return True

    def initiate_ftp_connection(self):
        self.local_file_path = join_paths(ProjectPathController.get_instance().get_project_path(), 'data.bin')
        remote_file_path = 'Sniffing/data.bin'
        ftp_receiver = FtpReceiver()
        ftp_receiver.receive_file_via_ftp(self.local_file_path, remote_file_path)

    def store_sniffed_data(self):
        self.local_file_path = join_paths(ProjectPathController.get_instance().get_project_path(), 'data.bin')
        file_content = read_binary_file(self.local_file_path)
        ChannelsDataDao.update_channel_data(file_content)
        delete_file(self.local_file_path)
