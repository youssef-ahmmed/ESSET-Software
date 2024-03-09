from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import CheckBox, ComboBox, LineEdit

from views.common.output_terminal import OutputTerminal


class StreamFinderWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.conditions = ["cond1", "cond2", "cond3", "cond4"]

        self.initialize_components()

    def initialize_components(self):
        self.init_ui()
        self.setup_stream_layout()
        self.setup_conditional_layout()
        self.create_layout()
        self.connect_checkbox_state_changed()
        self.make_terminal_editable()

    def init_ui(self):
        self.stream_finder_checkbox = QLabel("Stream Finder")

        self.conditional_bypass_checkbox = CheckBox("Set Condition")
        self.input_stream = LineEdit()

        self.conditional_bypass_combobox = ComboBox()
        self.conditional_bypass_combobox.setEnabled(False)
        self.conditional_bypass_combobox.addItems(self.conditions)

        self.terminal = OutputTerminal()

    def create_layout(self):
        self.layout = QVBoxLayout()

        self.layout.addLayout(self.stream_layout)
        self.layout.addLayout(self.conditional_layout)
        self.layout.addWidget(self.terminal)

        self.setLayout(self.layout)

    def setup_stream_layout(self):
        self.stream_layout = QVBoxLayout()

        self.stream_layout.setContentsMargins(11, 0, 11, 0)
        self.stream_layout.addWidget(self.stream_finder_checkbox)
        self.stream_layout.addWidget(self.input_stream)

    def setup_conditional_layout(self):
        self.conditional_layout = QVBoxLayout()

        self.conditional_layout.setContentsMargins(11, 20, 11, 0)
        self.conditional_layout.addWidget(self.conditional_bypass_checkbox)
        self.conditional_layout.addWidget(self.conditional_bypass_combobox)

    def connect_checkbox_state_changed(self):
        self.conditional_bypass_checkbox.stateChanged.connect(self.toggle_visibility)

    def toggle_visibility(self, state):
        if state == 2:
            self.conditional_bypass_combobox.setEnabled(True)
        else:
            self.conditional_bypass_combobox.setEnabled(False)

    def reset_to_default(self):
        self.input_stream.clear()
        self.conditional_bypass_combobox.setCurrentIndex(0)
        self.terminal.terminal.clear()

    def make_terminal_editable(self):
        if self.terminal.terminal.toPlainText():
            self.terminal.set_editable(True)
