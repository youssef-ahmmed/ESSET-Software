from enum import Enum

import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel


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

    def update_channel_label(self, text):
        self.item(0, 0).setText(text)

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
        self.plot_widget.setMouseEnabled(x=True, y=False)
