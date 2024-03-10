from controllers.synthesis_files_controller.config_file_controller import ConfigFileController


class ReplayAttackActionController:
    def __init__(self):
        ConfigFileController.get_instance().send_config_file(False, "Replay Attack")
