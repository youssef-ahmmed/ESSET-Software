from PyQt5.QtCore import QObject
from qfluentwidgets import PrimarySplitPushButton

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController
from controllers.synthesis_files_controller.sof_file_controller import SofFileController
from controllers.synthesis_files_controller.top_level_file_controller import TopLevelFileController
from core.command_executor import CommandExecutor
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_error_bar


class StartSniffingButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_sniffing_button: PrimarySplitPushButton = None) -> None:
        if StartSniffingButtonController._instance is None:
            StartSniffingButtonController._instance = StartSniffingButtonController(start_sniffing_button)
        return StartSniffingButtonController._instance

    def __init__(self, start_sniffing_button: PrimarySplitPushButton) -> None:
        super(StartSniffingButtonController, self).__init__()

        if StartSniffingButtonController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.start_sniffing_button = start_sniffing_button
        self.project_path_controller = ProjectPathController.get_instance()
