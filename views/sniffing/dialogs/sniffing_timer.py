from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from qfluentwidgets import ComboBox, PrimaryPushButton, SearchLineEdit


class SniffingTimer(QDialog):
    def __init__(self, parent=None):
        super(SniffingTimer, self).__init__(parent)

        self.label = QLabel('Stop recording after')
        self.time_edit = SearchLineEdit()
        self.unit_combo = ComboBox()
        self.ok_button = PrimaryPushButton('OK')
        self.cancel_button = PrimaryPushButton('Cancel')

        self.init_ui()

    def init_ui(self):
        self.time_edit.setValidator(QtGui.QIntValidator())
        self.unit_combo.addItems(['s', 'm', 'h'])

        input_time_layout = QHBoxLayout()
        input_time_layout.addWidget(self.label)
        input_time_layout.addWidget(self.time_edit)
        input_time_layout.addWidget(self.unit_combo)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        timer_layout = QVBoxLayout()
        timer_layout.addLayout(input_time_layout)
        timer_layout.addLayout(buttons_layout)

        self.setLayout(timer_layout)

    def create_time_unit_layout(self):
        time_unit_layout = QHBoxLayout()
        time_unit_layout.addWidget(self.time_edit)
        time_unit_layout.addWidget(self.unit_combo)
        return time_unit_layout
