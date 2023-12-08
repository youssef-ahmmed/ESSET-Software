from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from views.display.waveform_widget import WaveformWidget


class ChannelButton(QWidget):
    flag = 0

    def __init__(self):
        super().__init__()

        self.color = "#7FACD6"
        self.no_buttons = 8
        self.channel_widget = []
        self.channel_label = QLabel("Show/Hide Channel")

        self.init_ui()

    def init_ui(self):
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.hide_all_channels)

        self.all_button = QPushButton("All")
        self.all_button.clicked.connect(self.show_all_channels)

        for button in range(self.no_buttons):
            channel_button = QPushButton(f'{button}')
            channel_button.setStyleSheet(f"background-color: {self.color}")
            channel_button.clicked.connect(lambda checked, button=channel_button: self.on_button_clicked(button))
            channel_button.setFixedSize(50, 30)
            self.channel_widget.append(channel_button)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.all_button)
        h_layout.addWidget(self.clear_button)

        buttons_layout = QHBoxLayout()
        for button in self.channel_widget:
            buttons_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(self.channel_label)
        layout.addLayout(h_layout)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def on_button_clicked(self, sender_button):
        if sender_button:
            self.button_number = int(sender_button.text())
            self.toggle_channel_visibility(sender_button)

    def toggle_channel_visibility(self, sender_button):
        if ChannelButton.flag == 0:
            WaveformWidget.plot_widgets[self.button_number].hide()
            self.update_button_color(sender_button, "#33539E")
            ChannelButton.flag = 1

        elif ChannelButton.flag == 1:
            WaveformWidget.plot_widgets[self.button_number].show()
            self.update_button_color(sender_button, "#7FACD6")
            ChannelButton.flag = 0

    def update_button_color(self, button, color):
        button.setStyleSheet(f"background-color: {color}")

    def hide_all_channels(self):
        for i in range(1, len(WaveformWidget.plot_widgets)):
            WaveformWidget.plot_widgets[i].hide()

    def show_all_channels(self):
        for i in range(1, len(WaveformWidget.plot_widgets)):
            WaveformWidget.plot_widgets[i].show()
