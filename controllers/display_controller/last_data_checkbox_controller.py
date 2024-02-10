from PyQt5.QtCore import Qt

from controllers.display_controller.abstract_classes.abstract_data_display import AbstractDataDisplay
from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from models.dao.channels_data_dao import ChannelsDataDao


class LastDataCheckboxController(AbstractDataDisplay):

    _instance = None

    @staticmethod
    def get_instance(last_data_checkbox=None, parent=None):
        if LastDataCheckboxController._instance is None:
            LastDataCheckboxController._instance = LastDataCheckboxController(last_data_checkbox, parent)
        return LastDataCheckboxController._instance

    def __init__(self, last_data_checkbox, parent=None):
        super(LastDataCheckboxController, self).__init__(parent)

        if LastDataCheckboxController._instance is not None:
            raise Exception("An instance of LastDataCheckboxController already exists. Use get_instance() to access it.")

        self.last_data_checkbox = last_data_checkbox
        self.parent = parent

        self.start_communication()

    def start_communication(self):
        self.last_data_checkbox.stateChanged.connect(self.get_last_data_checkbox_state)

    def get_last_data_checkbox_state(self):
        state = self.last_data_checkbox.checkState()
        if state == Qt.Checked:
            SearchTimestampController.get_instance().toggle_search_timestamp_combobox(False)
        elif state == Qt.Unchecked:
            SearchTimestampController.get_instance().toggle_search_timestamp_combobox(True)
        return state

    def display_terminal_data(self):
        self.display_data_on_terminal(ChannelsDataDao.get_all_by_last_id())
