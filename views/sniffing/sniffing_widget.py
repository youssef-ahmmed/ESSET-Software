from PyQt5.QtWidgets import QWidget, QVBoxLayout

from views.sniffing.sniffing_modes_widget import SniffingModesWidget


class SniffingWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.sniffing_mode_widget = SniffingModesWidget()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.sniffing_mode_widget)
