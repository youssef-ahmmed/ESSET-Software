import os

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QPushButton
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from core.vhdl_parser import VhdlParser
from models import log_messages
from views.sniffing.buttons.select_channel_pins_button import SelectChannelPinsButton


class ChannelPinsButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(channel_pins=None):
        if ChannelPinsButtonController._instance is None:
            ChannelPinsButtonController._instance = ChannelPinsButtonController(channel_pins)
        return ChannelPinsButtonController._instance

    def __init__(self, channel_pins: SelectChannelPinsButton) -> None:
        super(ChannelPinsButtonController, self).__init__()

        if ChannelPinsButtonController._instance is not None:
            raise Exception("An instance of ChannelPinsButtonController already exists. "
                            "Use get_instance() to access it.")

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
            self.project_path_controller.show_error_dialog(self.channel_pins_button)
            return

        top_level_name: str = self.project_path_controller.get_top_level_name()
        if top_level_name == "not exist":
            logger.error(log_messages.NO_TOP_LEVEL_FILE)
            return

        return os.path.join(project_path, top_level_name + '.vhd')

    def get_vhdl_nodes_name(self) -> list[str]:
        vhdl_parser = VhdlParser(self.top_level_file_path)
        return vhdl_parser.get_all_nodes_variables()

    def send_data_to_pin_planner(self):
        self.top_level_file_path: str = self.get_top_level_file_path()
        if not self.top_level_file_path:
            return

        current_timestamp: float = os.path.getmtime(self.top_level_file_path)
        if current_timestamp == self.previous_opened_timestamp:
            self.channel_pins.show_pin_planner_dialog()
            return

        nodes_name: list[str] = self.get_vhdl_nodes_name()
        self.previous_opened_timestamp = os.path.getmtime(self.top_level_file_path)

        self.pin_planner_table.populate_pin_planner(nodes_name)
        self.channel_pins.show_pin_planner_dialog()

        self.pin_planner_table.get_table_data()
