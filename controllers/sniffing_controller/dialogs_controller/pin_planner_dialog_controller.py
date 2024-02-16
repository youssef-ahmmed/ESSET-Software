from PyQt5.QtCore import QObject
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from core.vhdl_parser import VhdlParser
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.file_operations import is_modification_time_changed
from reusable_functions.os_operations import get_last_modification_time
from views.common.info_bar import create_error_bar
from views.sniffing.dialogs.hardware_pin_planner import HardwarePinPlanner


class PinPlannerDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(pin_planner_dialog: HardwarePinPlanner = None, parent=None):
        if PinPlannerDialogController._instance is None:
            PinPlannerDialogController._instance = PinPlannerDialogController(pin_planner_dialog, parent)
        return PinPlannerDialogController._instance

    def __init__(self, pin_planner_dialog: HardwarePinPlanner, parent):
        super(PinPlannerDialogController, self).__init__()

        if PinPlannerDialogController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.parent = parent
        self.pin_planner_dialog = pin_planner_dialog
        self.previous_opened_timestamp = None
        self.top_level_file_path = ""

    def send_data_to_pin_planner(self) -> None:
        self.top_level_file_path: str = self.get_top_level_file_path()
        if not self.top_level_file_path:
            return

        self.update_modification_time()

    def get_top_level_file_path(self) -> str:
        project_path_instance = ProjectPathController.get_instance()
        if project_path_instance.is_top_level_exists:
            return project_path_instance.get_top_level_file_path()

        self.emit_logger_error()

    def emit_logger_error(self):
        logger.error(log_messages.NO_TOP_LEVEL_FILE)
        create_error_bar(self.parent, "ERROR", log_messages.NO_TOP_LEVEL_FILE)

    def update_modification_time(self) -> None:
        if is_modification_time_changed(self.top_level_file_path,
                                        self.previous_opened_timestamp):
            self.previous_opened_timestamp = get_last_modification_time(self.top_level_file_path)

            self.parse_node_names_to_pin_planner()

    def parse_node_names_to_pin_planner(self) -> None:
        nodes_name: list[str] = self.get_vhdl_nodes_name()
        self.pin_planner_dialog.populate_pin_planner(nodes_name)

    def get_vhdl_nodes_name(self) -> list[str]:
        vhdl_parser = VhdlParser(self.top_level_file_path)
        return vhdl_parser.get_all_nodes_variables()

    def get_pin_planner_data(self) -> dict:
        return self.pin_planner_dialog.get_table_data()

    def open_pin_planner_dialog(self):
        self.pin_planner_dialog.show_pin_planner_dialog()
