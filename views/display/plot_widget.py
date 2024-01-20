from enum import Enum

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel
import pyqtgraph as pg
from PyQt5.QtCore import Qt
import numpy as np


class PlotWidget(QTableWidget):
    class Rectangle(Enum):
        WIDTH = 1150
        HEIGHT = 200

    def __init__(self, channel_number):
        super().__init__()

        self.setColumnCount(2)
        self.setRowCount(1)

        self.channel_number = channel_number
        self.channel_label = None
        self.plot_widget = None

        self.row_size()
        self.create_widgets()
        self.init_ui()

    def init_ui(self):
        self.setItem(0, 0, QTableWidgetItem())
        self.setItem(0, 1, QTableWidgetItem())

        self.item(0, 0).setTextAlignment(Qt.AlignCenter)
        self.item(0, 0).setText(f'Channel {self.channel_number}')
        self.setCellWidget(0, 1, self.plot_widget)

        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)

        self.plot_appearance()
        self.plot_signals()

    def row_size(self):
        self.setColumnWidth(1, self.Rectangle.WIDTH.value)
        self.setRowHeight(0, self.Rectangle.HEIGHT.value)

    def create_widgets(self):
        self.channel_label = QLabel()
        self.plot_widget = pg.PlotWidget()

    def plot_appearance(self):
        self.plot_widget.setBackground((255, 255, 255))
        self.plot_widget.setTitle(f'Channel {self.channel_number} Data', color='k')
        self.plot_widget.setLabel('bottom', 'Time', color='k')
        self.plot_widget.setLabel('left', 'Amplitude', color='k')

        pen = pg.mkPen(color=(0, 120, 255), width=2)
        self.plot_widget.plot(pen=pen, symbol='o', symbolSize=5)

        self.plot_widget.getAxis("bottom").setTextPen((0, 0, 0))
        self.plot_widget.getAxis("left").setTextPen((0, 0, 0))

        self.plot_widget.showGrid(x=True, y=True, alpha=0.7)
        self.plot_widget.addLegend()
        self.plot_widget.setMouseEnabled(x=True, y=True)

    def plot_signals(self):
        t = np.linspace(0, 1, 1000)

        square_wave = np.where(t % 0.5 < 0.25, 0.2, 0.8)
        self.plot_widget.plot(t, square_wave, pen=pg.mkPen(color='b', width=2), name='Square Wave')
