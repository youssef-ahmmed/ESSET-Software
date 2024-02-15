from datetime import datetime

from controllers.display_controller.abstract_classes.abstract_data_display import AbstractDataDisplay
from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.sniffed_data_dao import SniffedDataDao


class SearchTimestampController(AbstractDataDisplay):

    _instance = None

    @staticmethod
    def get_instance(search_timestamp=None):
        if SearchTimestampController._instance is None:
            SearchTimestampController._instance = SearchTimestampController(search_timestamp)
        return SearchTimestampController._instance

    def __init__(self, search_timestamp):
        super(SearchTimestampController, self).__init__()

        if SearchTimestampController._instance is not None:
            raise Exception("An instance of SearchTimestampController already exists. Use get_instance() to access it.")

        self.search_timestamp = search_timestamp
        self.update_timestamp_combobox()
        self.start_communication()

    def start_communication(self):
        self.search_timestamp.time_stamp_combobox.currentIndexChanged.connect(self.get_selected_start_time)

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

        self.search_timestamp.update_timestamp_items(items)

    def get_selected_start_time(self):
        if self.search_timestamp.time_stamp_combobox.currentText() == "Choose Time Stamp":
            return
        return self.search_timestamp.time_stamp_combobox.currentText()[0:19]

    def get_sniffing_option(self):
        if self.search_timestamp.time_stamp_combobox.currentText() == "Choose Time Stamp":
            return
        return self.search_timestamp.time_stamp_combobox.currentText()[22:]

    def get_start_time_obj(self):
        if not self.get_selected_start_time():
            return
        return datetime.strptime(self.get_selected_start_time(), '%Y-%m-%d %H:%M:%S')

    def display_terminal_data(self):
        start_time_obj = self.get_start_time_obj()
        self.display_data_on_terminal(ChannelsDataDao.get_data_by_start_time(start_time_obj))

    def toggle_search_timestamp_combobox(self, enable=True):
        self.search_timestamp.setEnabled(enable)
