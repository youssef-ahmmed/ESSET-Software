import re

from controllers.project_path_controller import ProjectPathController
from reusable_functions.file_operations import read_text_file, write_to_text_file
from reusable_functions.os_operations import dir_list, join_paths, check_is_file


class QsfWriter:
    def __init__(self):
        self.project_path_controller = ProjectPathController.get_instance()

    def write_qsf_content(self, pattern: str, new_assignments: list):
        qsf_file_path = self.project_path_controller.get_qsf_file_path()
        if qsf_file_path == 'not exist':
            return

        qsf_file_content = read_text_file(qsf_file_path)

        assignment_pattern = re.compile(pattern)
        qsf_file_content = re.sub(assignment_pattern, '', qsf_file_content)

        write_to_text_file(qsf_file_path, ''.join([qsf_file_content] + new_assignments))

    def write_hardware_pins(self, hardware_pins: dict[str, str]):
        new_location_assignment = [f"set_location_assignment {pin} -to {node}\n" for node, pin in hardware_pins.items()]
        self.write_qsf_content(r'set_location_assignment .*', new_location_assignment)

    def write_vhdl_files_to_qsf(self):
        vhdl_files = self.find_vhdl_files()
        if not vhdl_files:
            return

        new_global_assignment = [f"set_global_assignment -name VHDL_FILE {vhdl_file}\n" for vhdl_file in vhdl_files]
        self.write_qsf_content(r'set_global_assignment -name VHDL_FILE .*', new_global_assignment)

    def find_vhdl_files(self):
        vhdl_files = []
        project_path = self.project_path_controller.get_project_path()

        files_in_directory = dir_list(project_path)
        for file_name in files_in_directory:
            file_path = join_paths(project_path, file_name)
            if check_is_file(file_path) and file_name.endswith('.vhd'):
                vhdl_files.append(file_name)
        return vhdl_files
