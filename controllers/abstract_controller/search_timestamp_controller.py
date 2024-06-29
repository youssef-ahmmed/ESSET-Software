from datetime import datetime

from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.sniffed_data_dao import SniffedDataDao
from models.log_messages import instance_exists_error


class SearchTimestampController:

    _instance = None

    def __init__(self, search_timestamp_widget):
        super(SearchTimestampController, self).__init__()

        if self.__class__._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.search_timestamp_widget = search_timestamp_widget
        self.update_timestamp_combobox()

    def update_timestamp_combobox(self):
        sniffed_data_table = SniffedDataDao.get_all_with_channel_data()
        items = []
        label = ''
        for row in range(len(sniffed_data_table)):
            if sniffed_data_table[row].communication_protocol_name:
                label = sniffed_data_table[row].communication_protocol_name
            if sniffed_data_table[row].connection_way:
                label = sniffed_data_table[row].connection_way
            items.append(f'{sniffed_data_table[row].start_time} - {label}')
        self.search_timestamp_widget.update_timestamp_items(items)

    def get_sniffing_option(self):
        return self.search_timestamp_widget.time_stamp_combobox.currentText()[22:]

    def get_selected_option_data(self):
        start_time_obj = self.get_start_time_obj()
        channel_obj = ChannelsDataDao.get_data_by_start_time(start_time_obj)[0]
        return str(channel_obj.channel_data)[2:-1]

    def get_start_time_obj(self):
        return datetime.strptime(self.get_selected_start_time(), '%Y-%m-%d %H:%M:%S')

    def get_selected_start_time(self):
        return self.search_timestamp_widget.time_stamp_combobox.currentText()[0:19]

    def get_selected_timestamp(self):
        return self.search_timestamp_widget.time_stamp_combobox.currentText()
