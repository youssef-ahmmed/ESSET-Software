from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QFormLayout
import pyqtgraph as pg


class PlotWidget(QWidget):
    def __init__(self, channel_name):
        super().__init__()

        self.fixed_label = QLabel(f'D{channel_name}')
        self.channel_label = QLabel(f'Channel {channel_name}')
        self.plot_widget = pg.PlotWidget()

        self.set_size()
        self.init_ui()

    def init_ui(self):
        self.label_layout = QFormLayout()

        v_spacing = 15
        h_spacing = 1

        self.label_layout.setVerticalSpacing(v_spacing)
        self.label_layout.setHorizontalSpacing(h_spacing)

        self.label_layout.addWidget(self.fixed_label)
        self.label_layout.addWidget(self.channel_label)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.label_layout)
        self.layout.addWidget(self.plot_widget)

        self.setLayout(self.layout)

    def set_size(self):
        self.plot_widget.setMinimumWidth(700)
        self.plot_widget.setMaximumWidth(1300)

        self.plot_widget.setMinimumHeight(130)
        self.plot_widget.setMaximumHeight(400)
