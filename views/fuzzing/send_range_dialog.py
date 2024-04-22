from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from qfluentwidgets import PrimaryPushButton, SearchLineEdit, LineEdit


class SendRangeDialog(QDialog):
    def __init__(self, parent=None):
        super(SendRangeDialog, self).__init__(parent)

        self.label = QLabel('Range')
        self.to_label = QLabel(':')

        self.range_start = LineEdit()
        self.range_end = LineEdit()

        self.ok_button = PrimaryPushButton('OK')
        self.cancel_button = PrimaryPushButton('Cancel')

        self.init_ui()

    def init_ui(self):
        self.range_start.setValidator(QtGui.QIntValidator())
        self.range_end.setValidator(QtGui.QIntValidator())

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.range_start)
        main_layout.addWidget(self.to_label)
        main_layout.addWidget(self.range_end)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        timer_layout = QVBoxLayout()
        timer_layout.addLayout(main_layout)
        timer_layout.addLayout(buttons_layout)

        self.setLayout(timer_layout)
