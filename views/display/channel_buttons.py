from enum import Enum

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PushButton, PrimaryPushButton


class ChannelButtons(QWidget):

    channel_visibility = pyqtSignal(int)
    show_plots = pyqtSignal()
    clear_plots = pyqtSignal()

    class Color(Enum):
        LIGHT_BLUE = '#7FACD6'
        DARK_BLUE = '#33539E'

    def __init__(self):
        super().__init__()

        self.button_numbers = 8
        self.channel_buttons = []
        self.channel_label = QLabel("Show/Hide Channel")

        self.init_ui()
        self.start_communication()

    def start_communication(self):
        self.clear_button.clicked.connect(lambda: self.clear_plots.emit())
        self.all_button.clicked.connect(lambda: self.show_plots.emit())

        for button_number, channel_button in enumerate(self.channel_buttons, start=1):
            channel_button.clicked.connect(lambda _, num=button_number: self.channel_visibility.emit(num))

    def init_ui(self):
        self.clear_button = PushButton(FIF.REMOVE_FROM, "Clear")
        self.all_button = PushButton(FIF.VIEW, "Show All")

        for button in range(1, self.button_numbers + 1):
            channel_button = PrimaryPushButton(f'{button}')
            channel_button.setFixedSize(50, 30)
            self.channel_buttons.append(channel_button)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.all_button)
        h_layout.addWidget(self.clear_button)

        buttons_layout = QHBoxLayout()
        for button in self.channel_buttons:
            buttons_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(self.channel_label)
        layout.addLayout(h_layout)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    @staticmethod
    def update_button_color(button, color):
        button.setStyleSheet(f"background-color: {color}")
