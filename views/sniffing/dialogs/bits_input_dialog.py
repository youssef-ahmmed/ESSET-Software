from PyQt5.QtWidgets import QVBoxLayout, QApplication, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PrimaryPushButton, StrongBodyLabel, LineEdit
from qframelesswindow import FramelessDialog


class BitsInputDialog(FramelessDialog):
    def __init__(self, label_text):
        super().__init__()

        self.bits_label = None
        self.bits_input = None
        self.save_button = None
        self.cancel_button = None

        self.init_ui(label_text)

    def init_ui(self, label_text):
        self.setWindowTitle("Enter Number of Bits")
        self.setGeometry(200, 200, 300, 150)
        self.setContentsMargins(0, 20, 0, 0)

        screen_geometry = QApplication.desktop().availableGeometry()
        x = int((screen_geometry.width() - self.width()) / 2)
        y = int((screen_geometry.height() - self.height()) / 2)
        self.move(x, y)

        self.create_layout(label_text)

    def create_layout(self, label_text):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.bits_label = StrongBodyLabel(label_text)
        self.bits_input = LineEdit()
        self.save_button = PrimaryPushButton(FIF.SAVE, "Save")
        self.cancel_button = PrimaryPushButton(FIF.CANCEL, "Cancel")

        v_layout.addWidget(self.bits_label)
        v_layout.addWidget(self.bits_input)

        h_layout.addWidget(self.cancel_button)
        h_layout.addWidget(self.save_button)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
