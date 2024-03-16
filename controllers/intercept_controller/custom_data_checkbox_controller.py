from PyQt5.QtCore import QObject, Qt

from models.log_messages import instance_exists_error


class CustomDataCheckboxController(QObject):
    _instance = None

    @staticmethod
    def get_instance(custom_data_checkbox=None):
        if CustomDataCheckboxController._instance is None:
            CustomDataCheckboxController._instance = CustomDataCheckboxController(custom_data_checkbox)
        return CustomDataCheckboxController._instance

    def __init__(self, custom_data_checkbox):
        super(CustomDataCheckboxController, self).__init__()

        if CustomDataCheckboxController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.custom_data_checkbox = custom_data_checkbox

    def is_custom_data_checkbox_enabled(self):
        return self.custom_data_checkbox.checkState() == Qt.Checked
