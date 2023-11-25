from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox, QApplication
from PyQt5.QtCore import Qt
from uart_config import UartConfigurations
from spi_config import SpiConfigurations


class ChannelPinsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Channel Pins")
        self.setGeometry(200, 200, 400, 300)

        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        h2_layout = QHBoxLayout()

        channels = ["Channel 1", "Channel 2", "Channel 3", "Channel 4"]

        for channel in channels:
            label = QLabel(channel)
            channel_combo = QComboBox()

            channel_combo.addItem("Select Pin number")
            channel_combo.addItems(["Pin1", "Pin2", "Pin3", "Pin4"])
            channel_combo.setItemData(0, 0, role=Qt.UserRole - 1)
            channel_combo.setCurrentIndex(0)
            layout.addWidget(label)
            layout.addWidget(channel_combo)

        reset_button = QPushButton("reset")
        reset_button.clicked.connect(self.reset_settings)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_settings)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)

        h2_layout.addWidget(reset_button)
        h2_layout.addWidget(cancel_button)
        h2_layout.addWidget(save_button)

        layout.addLayout(h2_layout)

        self.setLayout(layout)

    def reset_settings(self):
        for i in range(self.layout().count()):
            widget = self.layout().itemAt(i).widget()
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)

    def cancel_settings(self):
        self.close()

    def save_settings(self):
        pass


