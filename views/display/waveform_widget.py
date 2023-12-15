from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QScrollArea, QVBoxLayout

from views.display.plot_widget import PlotWidget


class WaveformWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.channel_numbers = 8
        self.table_widget = None
        self.plot_widgets = []

        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget(self)
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

    def create_rows(self):
        for channel in range(self.channel_numbers):
            plot_widget = PlotWidget(channel)
            self.table_widget.setCellWidget(channel, 0, plot_widget)
            self.table_widget.setRowHeight(channel, 200)
            self.table_widget.setColumnWidth(0, 1320)

            vertical_header_item = QTableWidgetItem(f'D{channel}')
            self.table_widget.setVerticalHeaderItem(channel, vertical_header_item)

            self.plot_widgets.append(plot_widget)

        self.table_widget.horizontalHeader().setVisible(False)

    def toggle_visibility(self, channel_number):
        visible_channels = [i for i, plot_widget in enumerate(self.plot_widgets) if plot_widget.isVisible()]
        num_visible_channels = len(visible_channels)

        if channel_number == 0 and num_visible_channels == 1:
            self.plot_widgets[0].show()

        elif channel_number != 0 and num_visible_channels == 1:
            self.plot_widgets[0].show()
            self.plot_widgets[channel_number].setVisible(not self.plot_widgets[channel_number].isVisible())

        elif num_visible_channels > 0:
            self.plot_widgets[channel_number].setVisible(not self.plot_widgets[channel_number].isVisible())

        self.update_row_heights(self.plot_widgets)

    def update_row_heights(self, plot_widgets):
        for i, plot_widget in enumerate(plot_widgets):
            self.table_widget.setRowHeight(i, 200 if plot_widget.isVisible() else 0)

    def hide_all_channels(self):
        for plot_number, plot_widget in enumerate(self.plot_widgets):
            if plot_number == 0:
                plot_widget.setVisible(True)
            else:
                plot_widget.setVisible(False)
                self.table_widget.setRowHeight(plot_number, 0)

    def show_all_channels(self):
        for plot_widget in self.plot_widgets:
            plot_widget.setVisible(True)

        for i, plot_widget in enumerate(self.plot_widgets):
            self.table_widget.setRowHeight(i, 200)
