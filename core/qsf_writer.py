import os

from controllers.project_path_controller import ProjectPathController


class QSFWriter:
    def __init__(self):
        self.project_path_controller = ProjectPathController.get_instance()

    def find_vhdl_files(self):
        vhdl_files = []
        self.project_path = self.project_path_controller.get_project_path()

        files_in_directory = os.listdir(self.project_path)
        for file_name in files_in_directory:
            file_path = os.path.join(self.project_path, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.vhd'):
                vhdl_files.append(file_name)
        return vhdl_files

    def write_vhdl_files_to_qsf(self):
        vhdl_files = self.find_vhdl_files()
        self.top_level_name = self.project_path_controller.get_top_level_name()

        if not vhdl_files:
            print("No VHDL files found in the project path directory.")
            return

        if self.top_level_name is None:
            print("Top level name is not set.")
            return

        qsf_file_path = os.path.join(self.project_path, f"{self.top_level_name}.qsf")
        lines_to_write = [f"set_global_assignment -name VHDL_FILE {vhdl_file}\n" for vhdl_file in vhdl_files]

        existing_lines = []
        if os.path.exists(qsf_file_path):
            with open(qsf_file_path, 'r') as qsf_file:
                existing_lines = qsf_file.readlines()

        updated_lines = [line for line in existing_lines if
                         not line.startswith("set_global_assignment -name VHDL_FILE")]

        updated_lines.extend(lines_to_write)

        with open(qsf_file_path, 'w') as qsf_file:
            qsf_file.writelines(updated_lines)
