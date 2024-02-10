from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import CheckBox


class LastDataCheckbox(QWidget):

    def __init__(self):
        super().__init__()
        self.last_data_checkbox = CheckBox('Display Last Sniffed Data', self)
        self.last_data_checkbox.setTristate(False)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.last_data_checkbox)
