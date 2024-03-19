from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import StrongBodyLabel

from controllers.intercept_controller.data_operation_controller import DataOperationController
from controllers.intercept_controller.intercept_search_timestamp_controller import InterceptSearchTimestampController
from views.common.search_timestamp import SearchTimestamp
from views.intercept.custom_data_widget import CustomDataWidget
from views.intercept.data_operation_widget import DataOperationWidget


class ReplayAttackSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.search_timestamp = SearchTimestamp()
        InterceptSearchTimestampController.get_instance(self.search_timestamp)

        self.custom_data_widget = CustomDataWidget()
        self.data_operation_widget = DataOperationWidget()
        DataOperationController.get_instance(self.data_operation_widget)

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

        self.setLayout(self.replay_attack_layout)
