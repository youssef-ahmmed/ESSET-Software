from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup
from qfluentwidgets import CheckBox, RadioButton, StrongBodyLabel

from views.common.info_bar import main_window_manager
from views.intercept.bit_position_dialog import BitPositionDialog


class DataOperationWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.flip_bit_operation_layout()
        self.create_layout()

        self.flip_bits_radio.stateChanged.connect(self.toggle_checkbox_visibilty)
        self.group_button.buttonClicked[int].connect(self.show_bit_position_dialog)

    def init_ui(self):
        self.operations_on_data = StrongBodyLabel("Operations on data: ")

        self.flip_bits_radio = CheckBox("Flip Bits")

        self.group_button = QButtonGroup()

        self.flip_one_byte = RadioButton("Flip one byte")
        self.flip_all_ones = RadioButton("Flip all ones to all zeros")
        self.flip_all_zeros = RadioButton("Flip all zeros to all ones")
        self.flip_all_bits = RadioButton("Flip all bits")
        
        self.flip_bits_options()

        self.edit_data_radio = CheckBox("Edit Data")
        
    def flip_bits_options(self):
        self.flip_one_byte.setEnabled(False)
        self.flip_all_ones.setEnabled(False)
        self.flip_all_zeros.setEnabled(False)
        self.flip_all_bits.setEnabled(False)

        self.group_button.addButton(self.flip_one_byte, 1)
        self.group_button.addButton(self.flip_all_ones, 2)
        self.group_button.addButton(self.flip_all_zeros, 3)
        self.group_button.addButton(self.flip_all_bits, 4)

    def create_layout(self):
        self.replay_attack_layout = QVBoxLayout()
        self.replay_attack_layout.addWidget(self.operations_on_data)
        self.replay_attack_layout.addWidget(self.flip_bits_radio)

        self.replay_attack_layout.addLayout(self.flip_operation_layout)
        self.replay_attack_layout.addWidget(self.edit_data_radio)

        self.setLayout(self.replay_attack_layout)

    def flip_bit_operation_layout(self):
        self.flip_operation_layout = QVBoxLayout()
        self.flip_operation_layout.setContentsMargins(20, 0, 0, 0)

        self.flip_operation_layout.addWidget(self.flip_one_byte)
        self.flip_operation_layout.addWidget(self.flip_all_zeros)
        self.flip_operation_layout.addWidget(self.flip_all_ones)
        self.flip_operation_layout.addWidget(self.flip_all_bits)

    def toggle_checkbox_visibilty(self, state):
        if state == 2:
            self.flip_one_byte.setEnabled(True)
            self.flip_all_ones.setEnabled(True)
            self.flip_all_zeros.setEnabled(True)
            self.flip_all_bits.setEnabled(True)
        else:
            self.flip_one_byte.setEnabled(False)
            self.flip_all_ones.setEnabled(False)
            self.flip_all_zeros.setEnabled(False)
            self.flip_all_bits.setEnabled(False)

    def show_bit_position_dialog(self, id):
        if id == 1:
            self.bit_position_dialog = BitPositionDialog(main_window_manager.main_window)
            self.bit_position_dialog.exec()

    def set_enabled(self, enabled):
        self.flip_bits_radio.setEnabled(enabled)
        self.edit_data_radio.setEnabled(enabled)
        self.toggle_checkbox_visibilty(enabled)
