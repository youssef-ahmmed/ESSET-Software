import json

from controllers.project_path_controller import ProjectPathController
from reusable_functions.os_operations import join_paths


class MessageResponseFuzzingWriter:
    def __init__(self, messages: list):
        self.message_response = {
            message: "" for message in messages
        }
        self.create_fuzzing_message_response_file()

    def create_fuzzing_message_response_file(self):
        path_name = join_paths(ProjectPathController.get_instance().get_project_path(),
                               "MessageResponseFuzzing.json")
        with open(path_name, 'w') as file:
            json.dump(self.message_response, file, indent=4)
