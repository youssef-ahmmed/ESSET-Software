from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class ConfigurationButtons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.synthesis_button = QPushButton('Synthesis')
        self.start_sniffing = QPushButton('Start Sniffing')

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.synthesis_button)
        self.layout().addWidget(self.start_sniffing)

        self.start_sniffing.clicked.connect(self.show_sniffing_timer_dialog)

    def show_sniffing_timer_dialog(self):
        sniffing_timer_dialog = SniffingTimer(self)
        sniffing_timer_dialog.exec_()
