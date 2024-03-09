from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import CheckBox, PlainTextEdit


class CustomDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.custom_data_checkbox = CheckBox("Write Your Custom Data")
        self.custom_data = PlainTextEdit()

        self.set_custom_data_properties()
        self.create_layout()
        self.connect_checkbox_state_changed()

    def set_custom_data_properties(self):
        self.custom_data.setEnabled(False)
        self.custom_data.setFixedHeight(500)

    def create_layout(self):
        self.custom_data_layout = QVBoxLayout()
        self.custom_data_layout.addWidget(self.custom_data_checkbox)
        self.custom_data_layout.addWidget(self.custom_data)

        self.setLayout(self.custom_data_layout)

    def connect_checkbox_state_changed(self):
        self.custom_data_checkbox.stateChanged.connect(self.toggle_custom_data_visibility)

    def toggle_custom_data_visibility(self, state):
        if state == 2:
            self.custom_data.setEnabled(True)
        else:
            self.custom_data.setEnabled(False)
