import json


class ConfigurationWriter:
    def __init__(self, programming: bool = False, operation: str = "", timer: int = 0):
        self.config = {
            "programming": programming,
            "operations": operation,
            "timer": timer
        }

    def create_config_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.config, file, indent=4)
