from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import LineEdit, CheckBox, PrimaryPushButton

from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController
from controllers.intercept_controller.receive_intercept_status_controller import ReceiveInterceptStatusController
from controllers.intercept_controller.stream_finder_input_controller import StreamFinderInputController
from views.common.output_terminal import OutputTerminal


class StreamFinderWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initialize_components()
        self.start_ui_communication()

    def start_ui_communication(self):
        self.edit_data_checkbox.stateChanged.connect(self.make_terminal_editable)

    def initialize_components(self):
        self.init_ui()
        self.setup_stream_layout()
        self.create_layout()

    def init_ui(self):
        self.stream_finder_label = QLabel("Stream Finder And Conditional Bypass")
        self.input_stream = LineEdit()
        StreamFinderInputController.get_instance(self.input_stream)
        self.input_stream.setPlaceholderText("Enter your stream...")

        self.edit_data_checkbox = CheckBox("Edit Data")

        self.terminal = OutputTerminal()
        InterceptTerminalController.get_instance(self.terminal.terminal)

        self.receive_intercept_status = PrimaryPushButton(FIF.FEEDBACK,"Receive Intercept Status")
        ReceiveInterceptStatusController.get_instance(self.receive_intercept_status)

    def create_layout(self):
        self.layout = QVBoxLayout()

        self.layout.addLayout(self.stream_layout)
        self.layout.addWidget(self.terminal)
        self.layout.addWidget(self.receive_intercept_status)

        self.setLayout(self.layout)

    def setup_stream_layout(self):
        self.stream_layout = QVBoxLayout()

        self.stream_layout.setContentsMargins(11, 0, 11, 0)
        self.stream_layout.addWidget(self.stream_finder_label)
        self.stream_layout.addWidget(self.input_stream)
        self.stream_layout.addWidget(self.edit_data_checkbox)

    def reset_to_default(self):
        self.input_stream.clear()
        self.terminal.terminal.clear()

    def make_terminal_editable(self, state):
        if self.terminal.terminal.toPlainText() and state == 2:
            self.terminal.set_editable(True)
        else:
            self.terminal.set_editable(False)
