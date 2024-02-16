from PyQt5.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton

from controllers.sniffing_controller.buttons_controller.channel_pins_button_controller import \
    ChannelPinsButtonController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from views.sniffing.dialogs.hardware_pin_planner import HardwarePinPlanner


class SelectChannelPinsButton(QWidget):
    def __init__(self):
        super().__init__()

        self.channel_pins_button = PrimaryPushButton(FIF.PIN, "Select Channel Pins")
        self.pin_planner_table = HardwarePinPlanner(self.channel_pins_button)

        HardwarePinPlannerController.get_instance(self.pin_planner_table)
        ChannelPinsButtonController.get_instance(self.channel_pins_button, parent)
        PinPlannerDialogController.get_instance(self.pin_planner_table, parent)

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.channel_pins_button)

