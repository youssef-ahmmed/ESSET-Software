import os
import subprocess
import time

from loguru import logger


class ScriptExecutor:

    def __init__(self, script_path):
        self.script_path = script_path

    def execute_script(self):
        try:
            logger.info("Synthesizing Running ....")
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
            logger.success(f"Synthesizing Executed Successfully in: {execution_time} s")
            return output
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return None
