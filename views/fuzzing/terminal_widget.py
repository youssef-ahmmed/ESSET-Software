from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import CheckBox

from controllers.fuzzing_controller.fuzzing_terminal_controller import FuzzingTerminalController
from controllers.fuzzing_controller.view_bytes_checkbox_controller import ViewBytesCheckboxController
from views.common.output_terminal import OutputTerminal


class TerminalWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_components()
        self.create_layout()

    def create_components(self):
        self.terminal = OutputTerminal()
        self.view_as_bytes_checkbox = CheckBox("View as bytes")

        FuzzingTerminalController.get_instance(self.terminal.terminal)
        ViewBytesCheckboxController.get_instance(self.view_as_bytes_checkbox)

    def create_layout(self):
        terminal_layout = QVBoxLayout()

        terminal_layout.addWidget(self.terminal)
        terminal_layout.addWidget(self.view_as_bytes_checkbox)

        self.setLayout(terminal_layout)
