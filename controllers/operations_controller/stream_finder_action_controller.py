from controllers.synthesis_files_controller.config_file_controller import ConfigFileController


class StreamFinderActionController:
    def __init__(self):
        ConfigFileController.get_instance().send_config_file(False, "Stream Finder")
