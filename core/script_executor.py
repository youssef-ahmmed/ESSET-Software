import os
import platform
import subprocess

from loguru import logger

from controllers.environment_path_controller import EnvironmentPathController
from reusable_functions.os_operations import change_dir, change_file_mode, \
    get_path_separation, get_directory_name


class ScriptExecutor:
    def __init__(self, script_path):
        self.script_path = script_path
        os.environ['PATH'] += get_path_separation() + EnvironmentPathController.get_instance().get_env_path()

    def execute_synthesis_script(self):
        try:
            if platform.system() == 'Linux':
                self.chmod_script()
            script_directory = get_directory_name(self.script_path)
            change_dir(script_directory)

            process = subprocess.Popen(self.script_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       universal_newlines=True)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    yield output.strip()
            return_code = process.poll()
            yield f"return code: {return_code}"
        except Exception as e:
            logger.error(f"Synthesizing process failed with error: {str(e)}. Please review and try again.")
            return

    def chmod_script(self):
        try:
            change_file_mode(self.script_path, 0o755)
        except Exception as e:
            logger.error(f"An error occurred while executing the script with permission: {str(e)}")
            return None
