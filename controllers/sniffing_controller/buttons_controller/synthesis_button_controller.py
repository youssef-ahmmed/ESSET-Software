from PyQt5.QtCore import QObject

from controllers.sniffing_controller.terminal_controller import TerminalController
from core.script_executor import ScriptExecutor


class SynthesisButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(synthesis_button=None):
        if SynthesisButtonController._instance is None:
            SynthesisButtonController._instance = SynthesisButtonController(synthesis_button)
        return SynthesisButtonController._instance

    def __init__(self, synthesis_button):
        super(SynthesisButtonController, self).__init__()

        if SynthesisButtonController._instance is not None:
            raise Exception("An instance of BitsInputDialogController already exists. Use get_instance() to access it.")

        self.synthesis_button = synthesis_button

        self.start_communication()

    def start_communication(self):
        print("start comm")
        self.synthesis_button.clicked.connect(self.run_script)

    def run_script(self, script_path):
        print('running ........')
        script_path = '/home/ahmedhamdi/Z/new_test2/run_quartus.sh'
        executor = ScriptExecutor(script_path)
        output = executor.execute_script()
        print(output)
        TerminalController.get_instance().write_text(output)
