from PyQt5.QtCore import QObject

from views.fuzzing.response_table import ResponseTable


class ResponseTableController(QObject):
    _instance = None

    @staticmethod
    def get_instance(response_table: ResponseTable = None):
        if ResponseTableController._instance is None:
            ResponseTableController._instance = ResponseTableController(response_table)
        return ResponseTableController._instance

    def __init__(self, response_table: ResponseTable):
        super(ResponseTableController, self).__init__(response_table)

        self.response_table = response_table

    def populate_response_table(self, random_data):
        self.response_table.create_table_rows(random_data)

    def clear_all_table_data(self):
        self.response_table.delete_all_data()
