from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from views.sniffing.expert_mode_widget import ExpertModeWidget
from views.sniffing.simple_mode_widget import SimpleModeWidget


class SniffingModesWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.modes_widget = QTabWidget(self)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.modes_widget)

        simple_mode = SimpleModeWidget()
        expert_mode = ExpertModeWidget()

        self.modes_widget.addTab(simple_mode, "Simple Mode")
        self.modes_widget.addTab(expert_mode, "Expert Mode")
