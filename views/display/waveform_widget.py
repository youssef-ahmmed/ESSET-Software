from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QScrollArea
from views.display.plot_widget import PlotWidget


class WaveformWidget(QWidget):
    plot_widgets = []

    def __init__(self):
        super().__init__()

        self.no_channels = 8

        self.init_ui()

    def init_ui(self):
        row_spacing = 15
        self.base_layout = QFormLayout()
        self.base_layout.setVerticalSpacing(row_spacing)

        for channel in range(self.no_channels):
            plot_widget = PlotWidget(channel)
            WaveformWidget.plot_widgets.append(plot_widget)

        for plot_widget in WaveformWidget.plot_widgets:
            self.base_layout.addWidget(plot_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(self.base_layout)

        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)
