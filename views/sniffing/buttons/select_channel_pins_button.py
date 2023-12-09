from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton

from views.sniffing.dialogs.hardware_pin_planner import HardwarePinPlanner


class SelectChannelPinsButton(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Uart Settings")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.channel_pins_button = QPushButton("Select Channel Pins")
        self.channel_pins_button.clicked.connect(self.show_pin_planner_dialog)
        layout.addWidget(self.channel_pins_button)
        self.setLayout(layout)

    def show_pin_planner_dialog(self):
        pin_planner_table = HardwarePinPlanner()
        pin_planner_table.exec_()
