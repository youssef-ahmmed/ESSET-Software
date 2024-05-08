from controllers.project_path_controller import ProjectPathController
from models import log_messages
from views.common.info_bar import create_error_bar


def validate_project_path():
    project_path_validation = ProjectPathValidation()

    try:
        project_path_validation.validate_project_path()

        return True
    except InputValidationError as e:
        create_error_bar(str(e))
        return False


class InputValidationError(Exception):
    pass


class ProjectPathValidation:

    def __init__(self):
        self.project_path_controller = ProjectPathController.get_instance()

    def validate_project_path(self):
        project_path = self.project_path_controller.get_project_path()

        if project_path == "":
            raise InputValidationError(log_messages.NO_QUARTUS_PATH)
