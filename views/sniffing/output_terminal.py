from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget
from views.custom_component.custom_button import RoundButton


class TerminalWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.terminal = QPlainTextEdit(self)
        self.terminal.setReadOnly(True)
        layout.addWidget(self.terminal)

        input_button = RoundButton("Synthesis")
        input_button.clicked.connect(self.send_command)
        layout.addWidget(input_button)

        self.setCentralWidget(central_widget)

    def send_command(self):
        command = "command"
        result = "Result"
        self.terminal.appendPlainText(f"> {command}\n{result}\n")
