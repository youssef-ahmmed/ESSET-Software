from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QButtonGroup
from qfluentwidgets import RadioButton


class FuzzingModeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.create_fuzzing_mode_components()
        self.create_button_group()
        self.create_layout()

    def create_fuzzing_mode_components(self):
        self.fuzzing_modes_label = QLabel("Fuzzing Mode:")

        self.generator_mode_radio = RadioButton("Generator")
        self.mutation_mode_radio = RadioButton("Mutation")

    def create_button_group(self):
        self.fuzzing_mode_button_group = QButtonGroup()
        self.fuzzing_mode_button_group.addButton(self.generator_mode_radio, 1)
        self.fuzzing_mode_button_group.addButton(self.mutation_mode_radio, 2)

    def create_layout(self):
        main_layout = QVBoxLayout()

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.generator_mode_radio)
        radio_layout.addWidget(self.mutation_mode_radio)

        radio_layout.setContentsMargins(90, 0, 0, 0)

        main_layout.addWidget(self.fuzzing_modes_label)
        main_layout.addLayout(radio_layout)

        self.setLayout(main_layout)
