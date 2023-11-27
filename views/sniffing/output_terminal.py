from PyQt5.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget


class OutputTerminal(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.terminal = QPlainTextEdit(self)
        self.terminal.setReadOnly(True)
        layout.addWidget(self.terminal)
