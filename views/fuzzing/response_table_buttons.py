from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF, PrimaryDropDownPushButton, Action, RoundMenu
from qfluentwidgets import PrimaryPushButton

from controllers.fuzzing_controller.receive_button_controller import ReceiveButtonController
from controllers.fuzzing_controller.send_range_dialog_controller import SendRangeDialogController
from views.fuzzing.send_range_dialog import SendRangeDialog


class ResponseTableButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.send_range_dialog = SendRangeDialog()
        SendRangeDialogController.get_instance(self.send_range_dialog)

        self.create_send_button_actions()
        self.create_buttons()
        self.init_ui()
        self.start_communication()

    def start_communication(self):
        self.send_range_action.triggered.connect(self.open_range_dialog)

    def open_range_dialog(self):
        self.send_range_dialog.exec_()

    def create_send_button_actions(self):
        self.menu = RoundMenu()
        self.send_selected_message_action = Action(FIF.MESSAGE, 'Send Selected Messages')
        self.send_range_action = Action(FIF.MENU, 'Send Range')
        self.send_all_action = Action(FIF.SEND_FILL, 'Send All')

        self.menu.addAction(self.send_selected_message_action)
        self.menu.addAction(self.send_range_action)
        self.menu.addAction(self.send_all_action)

    def create_buttons(self):
        self.send_button = PrimaryDropDownPushButton(FIF.SEND_FILL, 'Send')
        self.receive_button = PrimaryPushButton(FIF.UPDATE, "Receive")
        ReceiveButtonController.get_instance(self.receive_button)

        self.send_button.setMenu(self.menu)

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.send_button)
        self.layout().addWidget(self.receive_button)
