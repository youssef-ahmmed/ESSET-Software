import os.path
import platform

from PyQt5.QtCore import QObject, QTimer

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.terminal_controller import TerminalController
from core.script_executor import ScriptExecutor
from core.vhdl_generator import VhdlGenerator


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
        self.project_path_controller = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self):
        self.synthesis_button.clicked.connect(self.run_script)

    def run_script(self):
        project_path = self.project_path_controller.get_project_path()

        if not project_path:
            self.handle_no_project_path()
            return

        script_path = self.project_path_controller.get_script_path()
        if not script_path:
            script_path = self.generate_script(project_path)

        self.initiate_synthesizing_process(script_path)

    def handle_no_project_path(self):
        self.project_path_controller.show_error_dialog(self.synthesis_button)

    def generate_script(self, project_path):
        vhdl_generator = VhdlGenerator()
        configurations = {'top_level_name': self.project_path_controller.get_top_level_name()}
        script_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.sh.jinja'
        script_file = 'synthesis_linux.sh' if platform.system() == 'Linux' else 'synthesis_windows.sh'

        vhdl_generator.render_template(script_template, configurations=configurations, output_path=project_path)
        return os.path.join(project_path, script_file)

    @staticmethod
    def initiate_synthesizing_process(script_path):
        TerminalController.get_instance().write_text("Synthesizing Process Initiated. Please Await Completion...")
        executor = ScriptExecutor(script_path)
        executor.chmod_script()
        QTimer.singleShot(0, lambda: executor.execute_script_async())
