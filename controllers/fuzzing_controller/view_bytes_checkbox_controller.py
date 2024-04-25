from PyQt5.QtCore import QObject
from qfluentwidgets import CheckBox

from controllers.fuzzing_controller.fuzzing_terminal_controller import FuzzingTerminalController
from controllers.fuzzing_controller.generate_button_controller import GenerateButtonController
from core.data_processing import DataProcessing


class ViewBytesCheckboxController(QObject):
    _instance = None

    @staticmethod
    def get_instance(view_bytes_checkbox: CheckBox = None):
        if ViewBytesCheckboxController._instance is None:
            ViewBytesCheckboxController._instance = ViewBytesCheckboxController(view_bytes_checkbox)
        return ViewBytesCheckboxController._instance

    def __init__(self, view_bytes_checkbox: CheckBox):
        super(ViewBytesCheckboxController, self).__init__(view_bytes_checkbox)

        self.view_bytes_checkbox = view_bytes_checkbox

        self.start_communication()

    def start_communication(self):
        self.view_bytes_checkbox.stateChanged.connect(self.toggle_data_view)

    def toggle_data_view(self, state):
        fuzzed_data = GenerateButtonController.get_instance().get_generated_fuzzed_data()
        data_processing = DataProcessing(fuzzed_data)
        if state:
            data_as_hex = data_processing.combine_data_to_hex()
            FuzzingTerminalController.get_instance().write_text(data_as_hex)
        else:
            data_as_string = data_processing.combine_data_to_string()
            FuzzingTerminalController.get_instance().write_text(data_as_string)
