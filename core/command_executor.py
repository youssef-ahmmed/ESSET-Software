import os
import subprocess

from loguru import logger

from controllers.project_path_controller import ProjectPathController
from reusable_functions.os_operations import get_path_separation


class CommandExecutor:
    def __init__(self, command):
        self.command = command
        os.environ['PATH'] += get_path_separation() + ProjectPathController.get_instance().get_env_path()

    def execute_command(self):
        subprocess.run(self.command, shell=True, check=True, stderr=subprocess.PIPE)
