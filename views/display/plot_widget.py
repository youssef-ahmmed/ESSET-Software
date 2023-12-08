from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QFormLayout
import pyqtgraph as pg


class PlotWidget(QWidget):

    def __init__(self, channel_name):
        super().__init__()

        self.fixed_label = QLabel(f'D{channel_name}')
        self.channel_label = QLabel(f'Channel {channel_name}')
        self.channel_name = channel_name
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

        self.plot_appearance()

    def plot_appearance(self):
        self.plot_widget.setBackground((255, 255, 255))

        self.plot_widget.setTitle(f'Channel {self.channel_name} Data', color='k')

        self.plot_widget.setLabel('bottom', 'Time', color='k')
        self.plot_widget.setLabel('left', 'Amplitude', color='k')

        pen = pg.mkPen(color=(0, 120, 255), width=2)
        self.plot_widget.plot(pen=pen, symbol='o', symbolSize=5)

        self.plot_widget.getAxis("bottom").setTextPen((0, 0, 0))
        self.plot_widget.getAxis("left").setTextPen((0, 0, 0))

        self.plot_widget.showGrid(x=True, y=True, alpha=0.7)
        self.plot_widget.addLegend()

        self.plot_widget.setMouseEnabled(x=True, y=True)

    def set_size(self):
        self.plot_widget.setMinimumWidth(700)
        self.plot_widget.setMaximumWidth(1300)

        self.plot_widget.setMinimumHeight(200)
        self.plot_widget.setMaximumHeight(400)
