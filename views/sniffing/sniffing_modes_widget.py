from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from views.sniffing.hardware_configuration_widget import HardwareConfigurations
from views.sniffing.vhdl_widget import VhdlWidget


class SniffingModesWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.vhdl_widget = VhdlWidget()
        self.hardware_config = HardwareConfigurations()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.vhdl_widget)
        self.layout().addWidget(self.hardware_config)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.vhdl_widget)
        splitter.addWidget(self.hardware_config)

        total_size = self.vhdl_widget.sizeHint().width() + self.hardware_config.sizeHint().width()
        size_vhdl = 0.99 * total_size
        size_settings = 0.01 * total_size

        splitter.setSizes([int(size_vhdl), int(size_settings)])
        self.layout().addWidget(splitter)
