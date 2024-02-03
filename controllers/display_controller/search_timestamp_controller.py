from PyQt5.QtCore import QObject

from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.sniffed_data_dao import SniffedDataDao


class SearchTimestampController(QObject):

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
        self.search_timestamp.time_stamp_combobox.currentIndexChanged.connect(self.get_selected_option)

    def update_timestamp_combobox(self):
        sniffed_data_table = SniffedDataDao.get_all()
        items = []
        label = ''
        for row in range(len(sniffed_data_table)):
            formatted_datetime = sniffed_data_table[row].start_time.strftime("%Y-%m-%d %H:%M:%S.%f")

            if sniffed_data_table[row].communication_protocol_name:
                label = sniffed_data_table[row].communication_protocol_name
            if sniffed_data_table[row].connection_way:
                label = sniffed_data_table[row].connection_way

            items.append(f'{formatted_datetime} - {label}')

        self.search_timestamp.update_timestamp_items(items)

    def get_selected_option(self):
        return self.search_timestamp.time_stamp_combobox.currentText()[0:26]
