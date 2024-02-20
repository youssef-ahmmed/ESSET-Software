from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from models.log_messages import instance_exists_error
from views.common.message_box import MessageBox


class ChannelPinsButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(channel_pins_button: PrimaryPushButton = None, parent=None):
        if ChannelPinsButtonController._instance is None:
            ChannelPinsButtonController._instance = ChannelPinsButtonController(channel_pins_button, parent)
        return ChannelPinsButtonController._instance

    def __init__(self, channel_pins_button: PrimaryPushButton, parent) -> None:
        super(ChannelPinsButtonController, self).__init__()

        if ChannelPinsButtonController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.channel_pins_button = channel_pins_button

        self.start_communication()

    def start_communication(self) -> None:
        self.channel_pins_button.clicked.connect(self.open_pin_planner_dialog)

    def open_pin_planner_dialog(self):
        project_path_exist: bool = ProjectPathController.get_instance().is_project_path_exists()
        if not project_path_exist:
            MessageBox.show_project_path_error_dialog(self.channel_pins_button)
            return

        PinPlannerDialogController.get_instance().open_pin_planner_dialog()
