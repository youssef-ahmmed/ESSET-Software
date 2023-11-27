from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, \
    QPushButton, QFormLayout


class SniffingTimer(QDialog):
    def __init__(self, parent=None):
        super(SniffingTimer, self).__init__(parent)

        self.label = QLabel('Stop recording after')
        self.time_edit = QLineEdit()
        self.unit_combo = QComboBox()

        self.init_ui()

    def init_ui(self):
        self.time_edit.setValidator(QtGui.QIntValidator())
        self.unit_combo.addItems(['s', 'm', 'h'])

        layout = QFormLayout()
        layout.addRow(self.label, self.create_time_unit_layout())

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton('OK')
        cancel_button = QPushButton('Cancel')
        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        final_layout = QVBoxLayout()
        final_layout.addLayout(layout)
        final_layout.addLayout(buttons_layout)

        self.setLayout(final_layout)

    def create_time_unit_layout(self):
        time_unit_layout = QHBoxLayout()
        time_unit_layout.addWidget(self.time_edit)
        time_unit_layout.addWidget(self.unit_combo)
        return time_unit_layout
