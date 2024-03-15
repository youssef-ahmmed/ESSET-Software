from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import ComboBox, LineEdit

from views.common.output_terminal import OutputTerminal


class StreamFinderWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.actions = ["Choose Action", "Flip Bits", "Drop Communication", "Raise Flag"]

        self.initialize_components()

    def initialize_components(self):
        self.init_ui()
        self.setup_stream_layout()
        self.create_layout()
        self.make_terminal_editable()

    def init_ui(self):
        self.stream_finder_label = QLabel("Stream Finder And Conditional Bypass")
        self.input_stream = LineEdit()
        self.input_stream.setPlaceholderText("Enter your stream...")

        self.stream_finder_actions = ComboBox()
        self.stream_finder_actions.addItems(self.actions)

        self.terminal = OutputTerminal()

    def create_layout(self):
        self.layout = QVBoxLayout()

        self.layout.addLayout(self.stream_layout)
        self.layout.addWidget(self.terminal)

        self.setLayout(self.layout)

    def setup_stream_layout(self):
        self.stream_layout = QVBoxLayout()

        self.stream_layout.setContentsMargins(11, 0, 11, 0)
        self.stream_layout.addWidget(self.stream_finder_label)
        self.stream_layout.addWidget(self.input_stream)
        self.stream_layout.addWidget(self.stream_finder_actions)

    def reset_to_default(self):
        self.input_stream.clear()
        self.stream_finder_actions.setCurrentIndex(0)
        self.terminal.terminal.clear()

    def make_terminal_editable(self):
        if self.terminal.terminal.toPlainText():
            self.terminal.set_editable(True)
