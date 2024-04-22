from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF, PrimaryDropDownPushButton, Action, RoundMenu
from qfluentwidgets import PrimaryPushButton


class ResponseTableButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.menu = RoundMenu()
        self.send_selected_message_action = Action(FIF.MESSAGE, 'Send Selected Message')
        self.send_range_action = Action(FIF.MENU, 'Send Range')
        self.send_all_action = Action(FIF.SEND_FILL, 'Send All')

        self.menu.addAction(self.send_selected_message_action)
        self.menu.addAction(self.send_range_action)
        self.menu.addAction(self.send_all_action)

        self.send_button = PrimaryDropDownPushButton(FIF.SEND_FILL, 'Send')
        self.cancel_button = PrimaryPushButton(FIF.CANCEL_MEDIUM, "Cancel")
        self.send_button.setMenu(self.menu)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.send_button)
        self.layout().addWidget(self.cancel_button)
