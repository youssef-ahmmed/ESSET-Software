from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from views.display.waveform_widget import WaveformWidget


class ChannelButton(QWidget):
    flag = 0

    def __init__(self):
        super().__init__()

        self.no_buttons = 8
        self.channel_widget = []
        self.channel_label = QLabel("Show/Hide Channel")

        self.init_ui()

    def init_ui(self):
        for button in range(self.no_buttons):
            channel_button = QPushButton(f'{button}')
            channel_button.clicked.connect(lambda checked, button=channel_button: self.on_button_clicked(button))
            channel_button.setFixedSize(50, 30)
            self.channel_widget.append(channel_button)

        buttons_layout = QHBoxLayout()
        for button in self.channel_widget:
            buttons_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(self.channel_label)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def on_button_clicked(self, sender_button):
        if sender_button:
            self.button_number = int(sender_button.text())
            self.toggle_channel_visibility()

    def toggle_channel_visibility(self):
        if ChannelButton.flag == 0:
            WaveformWidget.plot_widgets[self.button_number].hide()
            ChannelButton.flag = 1

        elif ChannelButton.flag == 1:
            WaveformWidget.plot_widgets[self.button_number].show()
            ChannelButton.flag = 0
