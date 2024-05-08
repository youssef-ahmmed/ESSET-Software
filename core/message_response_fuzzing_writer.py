import json


class MessageResponseFuzzingWriter:
    def __init__(self, messages: list):
        self.message_response = {
            message: "" for message in messages
        }

    def create_fuzzing_message_response_file(self, path_name):
        with open(path_name, 'w') as file:
            json.dump(self.message_response, file, indent=4)
