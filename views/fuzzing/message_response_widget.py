from PyQt5.QtWidgets import QWidget, QVBoxLayout

from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from controllers.fuzzing_controller.send_fuzzing_button_controller import SendFuzzingButtonController
from views.fuzzing.response_table import ResponseTable
from views.fuzzing.response_table_buttons import ResponseTableButtons


class MessageResponseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.response_table = ResponseTable()
        self.response_table_buttons = ResponseTableButtons()

        SendFuzzingButtonController.get_instance(self.response_table_buttons)
        ResponseTableController.get_instance(self.response_table)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.response_table)
        self.layout().addWidget(self.response_table_buttons)
