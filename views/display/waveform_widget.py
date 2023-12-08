from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QScrollArea
from views.display.plot_widget import PlotWidget


class WaveformWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.channel_numbers = 8
        self.plot_widgets = []

        self.init_ui()

    def init_ui(self):
        row_spacing = 15
        self.base_layout = QFormLayout()
        self.base_layout.setVerticalSpacing(row_spacing)

        for channel in range(self.channel_numbers):
            plot_widget = PlotWidget(channel)
            self.plot_widgets.append(plot_widget)

        for plot_widget in self.plot_widgets:
            self.base_layout.addWidget(plot_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(self.base_layout)

        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def check_visibility(self):
        for plot_number in range(1, len(self.plot_widgets)):
            if not self.plot_widgets[plot_number].isVisible():
                return True
        return False

    def toggle_visibility(self, channel_number):
        if channel_number == 0 and self.check_visibility():
            return

        self.plot_widgets[channel_number].setVisible(
           not self.plot_widgets[channel_number].isVisible()
        )

    def hide_all_channels(self):
        for plot_number in range(1, len(self.plot_widgets)):
            self.plot_widgets[plot_number].hide()

    def show_all_channels(self):
        for i in range(1, len(self.plot_widgets)):
            self.plot_widgets[i].show()
