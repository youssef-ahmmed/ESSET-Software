from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QHBoxLayout, QLabel
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton, StrongBodyLabel, LineEdit, CaptionLabel
from qframelesswindow import FramelessDialog

from models import log_messages
from views.common.info_bar import create_info_bar


class BitsInputDialog(FramelessDialog):

    def __init__(self, label_text=None):
        super().__init__()

        self.bits_label = None
        self.bits_input = None
        self.save_button = None
        self.cancel_button = None

        self.init_ui(label_text)
        self.create_layout()
        self.center_dialog()

    def center_dialog(self):
        screen_geometry = QApplication.desktop().availableGeometry()
        x = int((screen_geometry.width() - self.width()) / 2)
        y = int((screen_geometry.height() - self.height()) / 2)
        self.move(x, y)

    def init_ui(self, label_text):
        self.bits_label = CaptionLabel(label_text)
        self.bits_input = LineEdit()
        self.clock_rate_label = CaptionLabel("Enter Clock Rate (MHz)")
        self.clock_rate = LineEdit()

        self.save_button = PrimaryPushButton(FIF.SAVE, "Save")
        self.cancel_button = PrimaryPushButton(FIF.CANCEL, "Cancel")

    def create_layout(self):
        self.setGeometry(200, 200, 300, 150)
        self.setContentsMargins(0, 20, 0, 0)
        title = StrongBodyLabel("Bit Sniffing")
        title.setAlignment(Qt.AlignCenter)

        self.setLayout(QVBoxLayout())
        bits_layout = QHBoxLayout()
        clock_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()

        bits_layout.addWidget(self.bits_label)
        bits_layout.addWidget(self.bits_input)

        clock_layout.addWidget(self.clock_rate_label)
        clock_layout.addWidget(self.clock_rate)

        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.addWidget(self.save_button)

        self.layout().addWidget(title)
        self.layout().addLayout(bits_layout)
        self.layout().addLayout(clock_layout)
        self.layout().addLayout(buttons_layout)

    def reset_bits_number_settings(self):
        self.bits_input.setText('')
        self.clock_rate.setText('')
        create_info_bar(log_messages.NUMBER_BITS_RESET)
