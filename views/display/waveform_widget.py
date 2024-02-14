from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QScrollArea, QVBoxLayout
from qfluentwidgets import TableWidget

from views.display.plot_widget import PlotWidget


class WaveformWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.channel_numbers = 8
        self.table_widget = None
        self.plot_widgets = []

        self.init_ui()

    def init_ui(self):
        self.table_widget = TableWidget(self)
        self.table_widget.setColumnCount(1)
        self.table_widget.setRowCount(self.channel_numbers)

        self.table_size()
        self.create_rows()

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

    def table_size(self):
        self.table_widget.setMinimumWidth(700)
        self.table_widget.setMinimumHeight(400)

    def set_channel_name(self, index, text):
        self.plot_widgets[index - 1].update_channel_label(text)

    def create_rows(self):
        for channel in range(1, self.channel_numbers + 1):
            plot_widget = PlotWidget(channel)
            self.table_widget.setCellWidget(channel - 1, 0, plot_widget)
            self.table_widget.setRowHeight(channel - 1, 200)
            self.table_widget.setColumnWidth(0, 1320)

            self.table_widget.setVerticalHeaderItem(channel - 1, QTableWidgetItem(f'D{channel}'))

            self.plot_widgets.append(plot_widget)
        self.table_widget.horizontalHeader().setVisible(False)

    def toggle_visibility(self, channel_number):
        visible_channels = [i for i, plot_widget in enumerate(self.plot_widgets) if plot_widget.isVisible()]
        num_visible_channels = len(visible_channels)

        if channel_number == 1 and num_visible_channels == 1:
            self.plot_widgets[0].show()

        elif channel_number != 1 and num_visible_channels == 1:
            self.plot_widgets[0].show()
            self.plot_widgets[channel_number - 1].setVisible(
                not self.plot_widgets[channel_number - 1].isVisible())

        elif num_visible_channels > 0:
            self.plot_widgets[channel_number - 1].setVisible(
                not self.plot_widgets[channel_number - 1].isVisible())

        self.update_row_heights(self.plot_widgets)

    def update_row_heights(self, plot_widgets):
        for i, plot_widget in enumerate(plot_widgets):
            self.table_widget.setRowHeight(i, 200 if plot_widget.isVisible() else 0)

    def hide_all_channels(self):
        for plot_number in range(0, len(self.plot_widgets)):
            if plot_number == 0:
                self.plot_widgets[plot_number].show()
                self.table_widget.setRowHeight(plot_number, 200)
            else:
                self.plot_widgets[plot_number].hide()
                self.table_widget.setRowHeight(plot_number, 0)

    def show_all_channels(self):
        for plot_widget in self.plot_widgets:
            plot_widget.show()

        for i, plot_widget in enumerate(self.plot_widgets):
            self.table_widget.setRowHeight(i, 200)
