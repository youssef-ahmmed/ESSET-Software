from PyQt5.QtWidgets import QWidget, QHBoxLayout

from views.intercept.replay_attack_settings_widget import ReplayAttackSettingsWidget
from views.intercept.stream_finder_widget import StreamFinderWidget


class InterceptWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.replay_attack_widget = ReplayAttackSettingsWidget()
        self.stream_finder_widget = StreamFinderWidget()

        self.create_layout()

    def create_layout(self):
        widgets_layout = QHBoxLayout()
        widgets_layout.addWidget(self.replay_attack_widget)
        widgets_layout.addWidget(self.stream_finder_widget)

        self.setLayout(widgets_layout)
