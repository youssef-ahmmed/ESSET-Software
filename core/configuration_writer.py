import json


class ConfigurationWriter:
    def __init__(self, programming: bool, operations: str, sniffing_time: int):
        self.config = {
            "programming": programming,
            "operations": operations,
            "sniffing_time": sniffing_time
        }

    def create_config_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.config, file, indent=4)
