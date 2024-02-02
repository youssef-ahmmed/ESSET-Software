import os
import platform
import subprocess

from loguru import logger

from controllers.project_path_controller import ProjectPathController


class ScriptExecutor:
    def __init__(self, script_path):
        self.script_path = script_path
        os.environ["PATH"] += os.pathsep + ProjectPathController.get_instance().get_env_path()

    def execute_script(self):
        try:
            if platform.system() == 'Linux':
                self.chmod_script()
            script_directory = os.path.dirname(self.script_path)
            os.chdir(script_directory)

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
            os.chmod(self.script_path, 0o755)
        except Exception as e:
            logger.error(f"An error occurred while executing the script with permission: {str(e)}")
            return None
