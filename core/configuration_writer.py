import json


class ConfigurationWriter:
    def __init__(self, programming: bool = False, operation: str = "", timer: int = 0, svf_file: str = ""):
        self.config = {
            "programming": programming,
            "operation": operation,
            "sniffing_time": timer,
            "svf_file": svf_file
        }

    def create_config_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.config, file, indent=4)
