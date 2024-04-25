from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.fuzzing_controller.fuzzing_terminal_controller import FuzzingTerminalController
from controllers.fuzzing_controller.generate_button_controller import GenerateButtonController
from controllers.fuzzing_controller.response_table_controller import ResponseTableController


class ClearButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(clear_button: PrimaryPushButton = None):
        if ClearButtonController._instance is None:
            ClearButtonController._instance = ClearButtonController(clear_button)
        return ClearButtonController._instance

    def __init__(self, clear_button: PrimaryPushButton):
        super(ClearButtonController, self).__init__(clear_button)

        self.clear_button = clear_button

        self.start_communication()

    def start_communication(self):
        self.clear_button.clicked.connect(self.clear_fuzzed_data)

    def clear_fuzzed_data(self):
        FuzzingTerminalController.get_instance().clear_terminal()
        ResponseTableController.get_instance().clear_all_table_data()
        GenerateButtonController.get_instance().reset_fuzzed_data()
