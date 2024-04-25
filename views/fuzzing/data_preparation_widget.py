from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from views.fuzzing.clear_button_widget import ClearButtonWidget
from views.fuzzing.data_operations_widget import DataOperationsWidget
from views.fuzzing.fuzzing_mode_widget import FuzzingModeWidget
from views.fuzzing.generate_button_widget import GenerateButtonWidget
from views.fuzzing.terminal_widget import TerminalWidget


class DataPreparationWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.data_operations_widget = DataOperationsWidget()
        self.fuzzing_mode_widget = FuzzingModeWidget()
        self.terminal_widget = TerminalWidget()
        self.clear_button_widget = ClearButtonWidget()
        self.generate_button_widget = GenerateButtonWidget()

    def create_layout(self):
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.data_operations_widget)
        main_layout.addWidget(self.fuzzing_mode_widget)
        main_layout.addWidget(self.terminal_widget)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button_widget)
        button_layout.addWidget(self.clear_button_widget)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
