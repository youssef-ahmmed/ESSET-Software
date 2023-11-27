from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from views.sniffing.hardware_configuration_widget import HardwareConfigurations
from views.sniffing.vhdl_widget import VhdlWidget


class SniffingWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.vhdl_widget = VhdlWidget()
        self.hardware_config_widget = HardwareConfigurations()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.vhdl_widget)
        self.layout().addWidget(self.hardware_config_widget)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.vhdl_widget)
        splitter.addWidget(self.hardware_config_widget)

        self.layout().addWidget(splitter)
