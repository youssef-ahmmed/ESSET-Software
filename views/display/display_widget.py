from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from views.display.waveform_widget import WaveformWidget
from views.display.display_setting_widget import DisplaySettingsWidget


class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.waveform_widget = WaveformWidget()
        self.display_settings_widget = DisplaySettingsWidget()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.waveform_widget)
        self.layout().addWidget(self.display_settings_widget)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.waveform_widget)
        splitter.addWidget(self.display_settings_widget)

        self.layout().addWidget(splitter)
