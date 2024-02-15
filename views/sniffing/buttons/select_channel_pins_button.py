from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton

from views.sniffing.dialogs.hardware_pin_planner import HardwarePinPlanner


class SelectChannelPinsButton(QWidget):
    def __init__(self):
        super().__init__()

        self.channel_pins_button = PrimaryPushButton(FIF.PIN, "Select Channel Pins")
        self.pin_planner_table = HardwarePinPlanner(self.channel_pins_button)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.channel_pins_button)

    def show_pin_planner_dialog(self):
        self.pin_planner_table.exec_()
