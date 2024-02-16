import platform

from controllers.project_path_controller import ProjectPathController
from core.jinja_generator import JinjaGenerator
from core.qsf_writer import QsfWriter
from reusable_functions.file_operations import delete_files
from reusable_functions.os_operations import join_paths


class TemplateGeneratorController:
    def __init__(self):
        self.jinja_generator = JinjaGenerator()
        self.qsf_writer = QsfWriter()
        self.project_path = ProjectPathController.get_instance().get_project_path()
        self.top_level_name = ProjectPathController.get_instance().get_top_level_name()

    def render_templates(self, template_names, configurations):
        common_template_names = [
            f'{self.top_level_name}.vhd.jinja',
            'Common_Ports.vhd.jinja',
            'Communication_Module.vhd.jinja'
        ]
        delete_files(self.project_path, '.vhd')
        self.jinja_generator.render_templates(common_template_names + template_names, configurations, self.project_path)
        self.render_synthesis_script()
        self.qsf_writer.write_vhdl_files_to_qsf()

    def render_uart_templates(self, configurations):
        template_names = ['UART_Receiver.vhd.jinja', 'UART_Transmitter.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_spi_slave_templates(self, configurations):
        template_names = ['SPI_Slave.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_bit_templates(self, configurations, sniffing_type):
        template_names = [f'{sniffing_type}_Sniffing.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_synthesis_script(self):
        configurations = {'top_level_name': self.top_level_name}
        script_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.sh.jinja'
        script_file = 'synthesis_linux.sh' if platform.system() == 'Linux' else 'synthesis_windows.sh'

        self.jinja_generator.render_templates([script_template], configurations, self.project_path)
        return join_paths(self.project_path, script_file)
