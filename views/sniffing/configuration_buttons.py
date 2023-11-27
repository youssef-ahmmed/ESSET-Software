from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout


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
