from PyQt5.QtCore import QObject

from controllers.display_controller.data_display_last_id_controller import DataDisplayLastIdController
from controllers.display_controller.data_display_start_time_controller import DataDisplayStartTimeController
from controllers.display_controller.last_data_checkbox_controller import LastDataCheckboxController
from views.display.waveform_widget import WaveformWidget


class WaveformController(QObject):
    _instance = None

    @staticmethod
    def get_instance(waveform_widget: WaveformWidget = None):
        if WaveformController._instance is None:
            WaveformController._instance = WaveformController(waveform_widget)
        return WaveformController._instance

    def __init__(self, waveform_widget: WaveformWidget):
        super(WaveformController, self).__init__()

        if WaveformController._instance is not None:
            raise Exception("An instance of WaveformController already exists. Use get_instance() to access it.")

        self.waveform_widget = waveform_widget
        self.time_period = None
        self.plot_data = None

    def assign_time_period_and_plot_data(self):
        if LastDataCheckboxController.get_instance().is_last_data_checkbox_enabled():
            self.time_period, self.plot_data = DataDisplayLastIdController().get_last_id_data()
        else:
            self.time_period, self.plot_data = DataDisplayStartTimeController().get_start_time_data()

    def calculate_time_period(self, binary_list):
        return [i * self.time_period for i in range(len(binary_list) + 1)]

    def assign_channel_info_to_plot_widget(self):
        self.assign_time_period_and_plot_data()

        for channel in self.plot_data:
            channel_number = channel.get("channel_number")
            channel_name = channel.get("channel_name")
            binary_list = channel.get("channel_data")

            self.set_channel_name(channel_number, channel_name)
            self.plot(self.waveform_widget.plot_widgets[channel_number - 1].plot_widget, binary_list)

    def set_channel_name(self, channel_number, channel_name):
        self.waveform_widget.set_channel_name(channel_number, channel_name)

    def plot(self, plot_widget, binary_list):
        time_values = self.calculate_time_period(binary_list)

        plot_widget.plot(x=time_values, y=binary_list, stepMode=True, fillLevel=None, pen='b')

        plot_widget.setRange(xRange=(min(time_values), max(time_values)),
                             yRange=(min(binary_list), max(binary_list)))
