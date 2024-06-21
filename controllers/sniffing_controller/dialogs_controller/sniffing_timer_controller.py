from enum import IntEnum

from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from core.configuration_writer import ConfigurationWriter
from core.ftp_sender import FtpSender
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_success_bar, create_warning_bar, create_error_bar
from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class SniffingTimerDialogController(QObject):

    class TimeUnit(IntEnum):
        MINUTES = 60
        HOURS = 3600
        TWO_HOURS = 7200

    _instance = None

    @staticmethod
    def get_instance(sniffing_timer_dialog: SniffingTimer = None):
        if SniffingTimerDialogController._instance is None:
            SniffingTimerDialogController._instance = SniffingTimerDialogController(sniffing_timer_dialog)
        return SniffingTimerDialogController._instance

    def __init__(self, sniffing_timer_dialog: SniffingTimer):
        super(SniffingTimerDialogController, self).__init__()

        if SniffingTimerDialogController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.sniffing_timer_dialog = sniffing_timer_dialog
        self.ok_button = self.sniffing_timer_dialog.ok_button
        self.cancel_button = self.sniffing_timer_dialog.cancel_button
        self.local_config_file_path = join_paths(ProjectPathController.get_instance().get_project_path(),
                                                 'config.json')
        self.remote_config_file_path = 'config/config.json'

        self.start_communication()

    def show_sniffing_timer_dialog(self):
        self.sniffing_timer_dialog.exec_()

    def start_communication(self):
        self.ok_button.clicked.connect(self.start_sniffing)
        self.cancel_button.clicked.connect(self.sniffing_timer_dialog.reject)

    def start_sniffing(self):
        try:
            self.sniffing_timer_dialog.accept()
            self.create_config_file()
            self.send_files_via_ftp()
            # TODO: Update Sniffing Time for sniffed data table
            # TODO: ResetController.clear_all_previous_configuration()
            create_success_bar(log_messages.SNIFFING_STARTED)
        except Exception:
            create_error_bar(log_messages.FTP_NOT_OPENED)

    def create_config_file(self):
        config_writer = ConfigurationWriter(operation="Sniffing", timer=self.get_sniffing_time())
        config_writer.create_config_file(self.local_config_file_path)

    def get_sniffing_time(self):
        sniffing_time = int(self.sniffing_timer_dialog.time_edit.text())
        time_unit = self.sniffing_timer_dialog.unit_combo.currentText()

        if time_unit == 'm':
            sniffing_time = sniffing_time * self.TimeUnit.MINUTES.value
        elif time_unit == 'h':
            sniffing_time = sniffing_time * self.TimeUnit.HOURS.value

        if sniffing_time >= self.TimeUnit.TWO_HOURS.value:
            create_warning_bar(log_messages.SNIFFING_TIME_WARNING)
            sniffing_time = self.TimeUnit.TWO_HOURS.value

        return sniffing_time

    def send_files_via_ftp(self):
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(self.local_config_file_path, self.remote_config_file_path)
