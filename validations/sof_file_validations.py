from controllers.synthesis_files_controller.sof_file_controller import SofFileController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_sof_file():
    sof_file_validation = SofFileValidation()

    try:
        sof_file_validation.validate_sof_file()

        return True
    except InputValidationError as e:
        create_error_bar(str(e))
        return False


class InputValidationError(Exception):
    pass


class SofFileValidation:

    def __init__(self):
        self.sof_file_controller = SofFileController.get_instance()

    def validate_sof_file(self):
        sof_file_path = self.sof_file_controller.get_sof_file_path()

        if sof_file_path is None:
            raise InputValidationError(log_messages.NO_SOF_FILE)
