from PyQt5.QtCore import QObject

from views.fuzzing.fuzzing_mode_widget import FuzzingModeWidget


class FuzzingModeController(QObject):
    _instance = None

    @staticmethod
    def get_instance(fuzzing_mode_widget: FuzzingModeWidget = None):
        if FuzzingModeController._instance is None:
            FuzzingModeController._instance = FuzzingModeController(fuzzing_mode_widget)
        return FuzzingModeController._instance

    def __init__(self, fuzzing_mode_widget: FuzzingModeWidget):
        super(FuzzingModeController, self).__init__(fuzzing_mode_widget)

        self.fuzzing_mode_widget = fuzzing_mode_widget

    def get_selected_fuzzing_mode(self):
        return self.fuzzing_mode_widget.get_selected_radio_button()
