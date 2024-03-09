from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import StrongBodyLabel

from views.common.search_timestamp import SearchTimestamp
from views.intercept.custom_data_widget import CustomDataWidget
from views.intercept.data_operation_widget import DataOperationWidget
from views.intercept.send_button import SendButton


class ReplayAttackSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.search_timestamp = SearchTimestamp()
        self.custom_data_widget = CustomDataWidget()
        self.data_operation_widget = DataOperationWidget()
        self.send_button = SendButton()

        self.init_ui()
        self.setup_replay_attack_layout()

    def init_ui(self):
        self.replay_attack = StrongBodyLabel("Replay Attack")
        self.replay_attack.setContentsMargins(10, 0, 0, 0)

    def setup_replay_attack_layout(self):
        self.replay_attack_layout = QVBoxLayout()

        self.replay_attack_layout.addWidget(self.replay_attack)
        self.replay_attack_layout.addWidget(self.search_timestamp)
        self.replay_attack_layout.addWidget(self.data_operation_widget)
        self.replay_attack_layout.addWidget(self.custom_data_widget)
        self.replay_attack_layout.addWidget(self.send_button)

        self.setLayout(self.replay_attack_layout)
