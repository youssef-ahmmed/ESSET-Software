from PyQt5.QtCore import QObject

from core.data_processing import DataProcessing


class DataDisplayCollectorController(QObject):

    @staticmethod
    def _get_channels_data(channels_data):
        terminal_data = ""
        for row in channels_data:
            terminal_data += str(row.channel_data)[2:-1]
        return terminal_data

    @staticmethod
    def _get_plot_data(channels_data):
        plot_data: list[dict] = []
        for row in channels_data:
            plot_data.append({
                'channel_name': row.channel_name,
                'channel_number': row.channel_number,
                'channel_data': DataProcessing(row.channel_data).convert_byte_list_to_bit_list()
            })

        return plot_data
