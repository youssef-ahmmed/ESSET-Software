from PyQt5.QtCore import QObject
from loguru import logger

from controllers.sniffing_controller.dialogs_controller.hardware_pin_planner_controller import \
    HardwarePinPlannerController
from views.common.info_bar import create_error_bar
from views.common.message_box import MessageBox

from controllers.project_path_controller import ProjectPathController
from core.vhdl_parser import VhdlParser
from models import log_messages
from reusable_functions.os_operations import join_paths, get_last_modification_time
from views.sniffing.buttons.select_channel_pins_button import SelectChannelPinsButton


class ChannelPinsButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(channel_pins=None, parent=None):
        if ChannelPinsButtonController._instance is None:
            ChannelPinsButtonController._instance = ChannelPinsButtonController(channel_pins, parent)
        return ChannelPinsButtonController._instance

    def __init__(self, channel_pins: SelectChannelPinsButton, parent) -> None:
        super(ChannelPinsButtonController, self).__init__()

        if ChannelPinsButtonController._instance is not None:
            raise Exception("An instance of ChannelPinsButtonController already exists. "
                            "Use get_instance() to access it.")

        self.parent = parent
        self.channel_pins = channel_pins
        self.channel_pins_button = channel_pins.channel_pins_button
        self.pin_planner_table = channel_pins.pin_planner_table

        self.previous_opened_timestamp = None
        self.top_level_file_path = ''

        self.project_path_controller: ProjectPathController = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self) -> None:
        self.channel_pins_button.clicked.connect(self.send_data_to_pin_planner)

    def get_top_level_file_path(self):
        project_path: str = self.project_path_controller.get_project_path()
        if not project_path:
            MessageBox.show_project_path_error_dialog(self.channel_pins_button)
            return

        top_level_name: str = self.project_path_controller.get_top_level_name()
        if top_level_name == "not exist":
            logger.error(log_messages.NO_TOP_LEVEL_FILE)
            create_error_bar(self.parent, 'ERROR', log_messages.NO_TOP_LEVEL_FILE)
            return

        return join_paths(project_path, top_level_name + '.vhd')

    def get_vhdl_nodes_name(self) -> list[str]:
        vhdl_parser = VhdlParser(self.top_level_file_path)
        return vhdl_parser.get_all_nodes_variables()

    def send_data_to_pin_planner(self):
        self.top_level_file_path: str = self.get_top_level_file_path()
        if not self.top_level_file_path:
            return

        current_timestamp: float = get_last_modification_time(self.top_level_file_path)
        if current_timestamp == self.previous_opened_timestamp:
            self.channel_pins.show_pin_planner_dialog()
            return

        nodes_name: list[str] = self.get_vhdl_nodes_name()
        self.previous_opened_timestamp = get_last_modification_time(self.top_level_file_path)

        self.pin_planner_table.populate_pin_planner(nodes_name)
        self.channel_pins.show_pin_planner_dialog()

        ChannelPinsButtonController.get_pin_planner_data()

    @staticmethod
    def get_pin_planner_data():
        return HardwarePinPlannerController.get_instance().get_table_data()
