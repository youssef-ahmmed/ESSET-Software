import os
import subprocess
import time

from PyQt5.QtCore import QTimer
from loguru import logger

from controllers.sniffing_controller.terminal_controller import TerminalController
from models import log_messages


class ScriptExecutor:
    def __init__(self, script_path):
        self.script_path = script_path
        # TODO: Set the environment path dynamically
        os.environ["PATH"] += os.pathsep + "/home/ahmedhamdi/Programs/FPGA/Quartus/quartus/bin"

    def execute_script_async(self):
        try:
            logger.info(log_messages.SYNTHESIZE_INITIATED)
            script_directory = os.path.dirname(self.script_path)
            os.chdir(script_directory)

            start_time = time.time()
            # TODO: handle bat script for windows users
            process = subprocess.Popen(['bash', os.path.basename(self.script_path)], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)

            QTimer.singleShot(0, lambda: self.read_output(process, start_time))
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return None

    def read_output(self, process, start_time):
        output, _ = process.communicate()
        end_time = time.time()

        execution_time = round(end_time - start_time, 2)
        output = output.decode('utf-8') if output else None
        TerminalController.get_instance().write_text(output)

        if process.returncode == 0:
            logger.success(f"{log_messages.SYNTHESIZE_SUCCESS} {execution_time} seconds.")
        else:
            logger.error(log_messages.SYNTHESIZE_FAILED)

    def chmod_script(self):
        try:
            os.chmod(self.script_path, 0o755)
        except Exception as e:
            print(f"An error occurred while executing the script with permission: {str(e)}")
            return None

    # To run the script in the terminal
    def execute_script(self):
        try:
            logger.info("Synthesizing Process Initiated. Please Await Completion...")
            script_directory = os.path.dirname(self.script_path)
            os.chdir(script_directory)

            start_time = time.time()
            process = subprocess.Popen(['bash', os.path.basename(self.script_path)], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
            output, _ = process.communicate()
            end_time = time.time()

            execution_time = round(end_time - start_time, 2)
            output = output.decode('utf-8') if output else None
            print(output)
            logger.success(f"Synthesizing Process Completed Successfully in: {execution_time} seconds.")
            return output
        except Exception as e:
            logger.error(f"Synthesizing process failed with exit code: {process.returncode}. Please review and try again.")
            return None
