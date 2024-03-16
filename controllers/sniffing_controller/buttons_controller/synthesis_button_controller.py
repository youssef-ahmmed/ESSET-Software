import time

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.template_generator_controller import TemplateGeneratorController
from controllers.sniffing_controller.synthesis_terminal_controller import SynthesisTerminalController
from core.script_executor import ScriptExecutor
from models import log_messages
from models.log_messages import instance_exists_error
from views.common.info_bar import create_success_bar, create_error_bar, create_info_bar
from views.common.message_box import MessageBox


class ScriptThread(QObject):
    finished = pyqtSignal(int, float)
    progress = pyqtSignal(str)

    def __init__(self, script_path):
        super().__init__()
        self.executor = ScriptExecutor(script_path)
        self.script_path = script_path

    def run(self):
        return_code = 0
        start_time = time.time()
        for line in self.executor.execute_synthesis_script():
            if line.startswith("return code"):
                return_code = int(line[-1])
            self.progress.emit(line)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        self.finished.emit(return_code, execution_time)


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
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.synthesis_button = synthesis_button
        self.start_communication()

    def start_communication(self):
        self.synthesis_button.clicked.connect(self.execute_script)

    def execute_script(self):
        script_path = self.get_script_path()
        if script_path is None:
            return
        create_info_bar(log_messages.SYNTHESIZE_INITIATED)
        self.thread = QThread()
        self.worker = ScriptThread(script_path)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(SynthesisTerminalController.get_instance().append_line)
        SynthesisTerminalController.get_instance().clear_terminal()
        self.thread.start()
        self.synthesis_button.setEnabled(False)
        self.thread.finished.connect(lambda: self.synthesis_button.setEnabled(True))
        self.worker.finished.connect(self.display_log_message)

    def get_script_path(self):
        project_path_controller = ProjectPathController.get_instance()
        project_path = project_path_controller.get_project_path()

        if not project_path:
            MessageBox.show_project_path_error_dialog(self.synthesis_button)
            return

        script_path = project_path_controller.get_script_path()
        if not script_path:
            template_generator_controller = TemplateGeneratorController()
            script_path = template_generator_controller.render_synthesis_script()
        return script_path

    @staticmethod
    def display_log_message(return_code, execution_time):
        if return_code == 0:
            create_success_bar(f"{log_messages.SYNTHESIZE_SUCCESS} {execution_time} seconds.")
        else:
            create_error_bar(log_messages.SYNTHESIZE_FAILED)
