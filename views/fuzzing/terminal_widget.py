from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import CheckBox

from views.common.output_terminal import OutputTerminal


class TerminalWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_components()
        self.create_layout()

    def create_components(self):
        self.terminal = OutputTerminal()
        self.view_as_bytes_checkbox = CheckBox("View as bytes")

    def create_layout(self):
        terminal_layout = QVBoxLayout()

        terminal_layout.addWidget(self.terminal)
        terminal_layout.addWidget(self.view_as_bytes_checkbox)

        self.setLayout(terminal_layout)
