from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import CheckBox, PlainTextEdit

from controllers.intercept_controller.custom_data_checkbox_controller import CustomDataCheckboxController
from controllers.intercept_controller.custom_data_terminal_controller import CustomDataTerminalController


class CustomDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.custom_data_checkbox = CheckBox("Write Your Custom Data")
        CustomDataCheckboxController.get_instance(self.custom_data_checkbox)
        self.custom_data = PlainTextEdit()
        CustomDataTerminalController.get_instance(self.custom_data)

        self.set_custom_data_properties()
        self.create_layout()
        self.connect_checkbox_state_changed()

    def set_custom_data_properties(self):
        self.custom_data.setEnabled(False)

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
            self.disable_data_operation_widgets()
        else:
            self.custom_data.setEnabled(False)
            self.enable_data_operation_widgets()

    def disable_data_operation_widgets(self):
        self.parent().data_operation_widget.set_enabled(False)
        self.parent().search_timestamp.set_enabled(False)

    def enable_data_operation_widgets(self):
        self.parent().data_operation_widget.set_enabled(True)
        self.parent().search_timestamp.set_enabled(True)
