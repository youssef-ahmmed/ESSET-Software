from loguru import logger
from qfluentwidgets import EditableComboBox

from core.qsf_writer import QsfWriter
from models import log_messages
from views.common.info_bar import create_success_bar, create_info_bar


class HardwarePinPlannerController:
    _instance = None

    @staticmethod
    def get_instance(hardware_pin_planner=None):
        if HardwarePinPlannerController._instance is None:
            HardwarePinPlannerController._instance = HardwarePinPlannerController(hardware_pin_planner)
        return HardwarePinPlannerController._instance

    def __init__(self, hardware_pin_planner):
        super(HardwarePinPlannerController, self).__init__()

        if HardwarePinPlannerController._instance is not None:
            raise Exception("An instance of HardwarePinPlannerController already exists."
                            " Use get_instance() to access it.")

        self.hardware_pin_planner = hardware_pin_planner

        self.start_communication()

    def start_communication(self):
        self.hardware_pin_planner.save_button.clicked.connect(self.send_hardware_pins)
        self.hardware_pin_planner.cancel_button.clicked.connect(self.hardware_pin_planner.reject)
        self.hardware_pin_planner.reset_button.clicked.connect(self.reset_table)

    def get_table_data(self) -> dict:
        table_data: dict[str, str] = {}

        for row in range(self.hardware_pin_planner.pin_planner.rowCount()):
            node_name = self.hardware_pin_planner.pin_planner.item(row, 0)
            hardware_pin = self.hardware_pin_planner.pin_planner.cellWidget(row, 1)

            if node_name is not None and hardware_pin is not None:
                node_name = node_name.text()
                hardware_pin = hardware_pin.currentText()
                table_data[node_name] = hardware_pin

        return table_data

    def send_hardware_pins(self):
        hardware_pins: dict[str, str] = self.get_table_data()

        qsf_writer = QsfWriter()
        qsf_writer.write_hardware_pins(hardware_pins)

        create_success_bar(log_messages.PINS_SET)
        self.hardware_pin_planner.accept()

    def reset_table(self):
        for row in range(self.hardware_pin_planner.pin_planner.rowCount()):
            combobox = self.hardware_pin_planner.pin_planner.cellWidget(row, 1)
            if combobox is not None and isinstance(combobox, EditableComboBox):
                combobox.setCurrentIndex(0)
        create_info_bar(log_messages.PINS_RESET)
