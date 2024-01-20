from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTabWidget, QHBoxLayout, QSplitter

from views.sniffing.expert_mode_widget import ExpertModeWidget
from views.sniffing.hardware_configuration_widget import HardwareConfigurations
from views.sniffing.simple_mode_widget import SimpleModeWidget


class SniffingModesWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.modes_widget = QTabWidget(self)
        self.hardware_config = HardwareConfigurations()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.modes_widget)
        self.layout().addWidget(self.hardware_config)

        simple_mode = SimpleModeWidget()
        expert_mode = ExpertModeWidget()

        self.modes_widget.addTab(simple_mode, "Simple Mode")
        self.modes_widget.addTab(expert_mode, "Expert Mode")

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.modes_widget)
        splitter.addWidget(self.hardware_config)

        total_size = self.modes_widget.sizeHint().width() + self.hardware_config.sizeHint().width()

        size_vhdl = 0.99 * total_size
        size_settings = 0.01 * total_size

        splitter.setSizes([int(size_vhdl), int(size_settings)])

        self.layout().addWidget(splitter)
