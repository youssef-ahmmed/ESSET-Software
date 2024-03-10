from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import PlainTextEdit


class OutputTerminal(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.terminal = PlainTextEdit(self)
        self.terminal.setReadOnly(True)
        layout.addWidget(self.terminal)

    def set_editable(self, editable):
        self.terminal.setReadOnly(not editable)
        if editable:
            self.terminal.setFocus()
