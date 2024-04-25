from PyQt5.QtCore import QObject

from views.fuzzing.data_operations_widget import DataOperationsWidget


class DataOperationController(QObject):
    _instance = None

    @staticmethod
    def get_instance(data_operation_widget: DataOperationsWidget = None):
        if DataOperationController._instance is None:
            DataOperationController._instance = DataOperationController(data_operation_widget)
        return DataOperationController._instance

    def __init__(self, data_operation_widget: DataOperationsWidget):
        super(DataOperationController, self).__init__(data_operation_widget)

        self.data_operation_widget = data_operation_widget

    def get_selected_fuzzing_protocol(self):
        return self.data_operation_widget.get_selected_fuzzing_protocol()

    def get_selected_sniffing_protocol(self):
        return self.data_operation_widget.get_selected_sniffing_protocol()

    def get_selected_data_type(self):
        return self.data_operation_widget.get_selected_data_type()

    def get_number_bytes_input(self):
        return self.data_operation_widget.get_number_bytes_input()

    def get_number_of_messages(self):
        return self.data_operation_widget.get_number_of_messages()
