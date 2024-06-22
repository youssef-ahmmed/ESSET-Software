from PyQt5.QtCore import QObject
from qfluentwidgets import PrimaryPushButton

from ML.fuzzed_data_collector import FuzzedDataCollector
from ML.model_preprocessing import ModelPreprocessing
from controllers.data_store_controller.fuzzed_data_store_controller import FuzzedDataStoreController
from controllers.fuzzing_controller.response_table_controller import ResponseTableController
from models import log_messages
from validations.project_path_validations import validate_project_path
from views.common.info_bar import create_success_bar
from views.fuzzing.response_table import ResponseTable


class ReceiveButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(clear_button: PrimaryPushButton = None):
        if ReceiveButtonController._instance is None:
            ReceiveButtonController._instance = ReceiveButtonController(clear_button)
        return ReceiveButtonController._instance

    def __init__(self, receive_button: PrimaryPushButton):
        super(ReceiveButtonController, self).__init__(receive_button)

        self.receive_button = receive_button
        self.response_table = ResponseTable()

        self.start_communication()

    def start_communication(self):
        self.receive_button.clicked.connect(self.receive_message_response)

    def receive_message_response(self):
        if not validate_project_path():
            return
        FuzzedDataStoreController().store_fuzzed_data()
        FuzzedDataCollector().write_data_to_csv()
        create_success_bar(log_messages.FUZZING_MESSAGES_RESPONSE_RECEIVE)

        model_preprocessing = ModelPreprocessing()
        model_preprocessing.built_model()
        results = model_preprocessing.get_results()
        ResponseTableController.get_instance().populate_response_table(results.values.tolist())
