from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter
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

        total_size = self.waveform_widget.sizeHint().width() + self.display_settings_widget.sizeHint().width()

        size_waveform = 0.99 * total_size
        size_settings = 0.01 * total_size

        splitter.setSizes([size_waveform, size_settings])

        self.layout().addWidget(splitter)
