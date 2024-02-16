from PyQt5.QtCore import Qt

from controllers.display_controller.abstract_classes.abstract_data_display import AbstractDataDisplay
from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from models.dao.channels_data_dao import ChannelsDataDao
from models.log_messages import instance_exists_error


class LastDataCheckboxController(AbstractDataDisplay):

    _instance = None

    @staticmethod
    def get_instance(last_data_checkbox=None):
        if LastDataCheckboxController._instance is None:
            LastDataCheckboxController._instance = LastDataCheckboxController(last_data_checkbox)
        return LastDataCheckboxController._instance

    def __init__(self, last_data_checkbox):
        super(LastDataCheckboxController, self).__init__()

        if LastDataCheckboxController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.last_data_checkbox = last_data_checkbox

        self.start_communication()

    def start_communication(self):
        self.last_data_checkbox.stateChanged.connect(self.toggle_search_timestamp_combobox)

    def is_last_data_checkbox_enabled(self):
        return self.last_data_checkbox.checkState() == Qt.Checked

    def toggle_search_timestamp_combobox(self):
        state = self.is_last_data_checkbox_enabled()
        SearchTimestampController.get_instance().toggle_search_timestamp_combobox(not state)

    def display_terminal_data(self):
        self.display_data_on_terminal(ChannelsDataDao.get_all_by_last_id())
