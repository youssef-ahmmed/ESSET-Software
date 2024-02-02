import platform

from jinja2 import Environment, select_autoescape, PackageLoader

from controllers.project_path_controller import ProjectPathController
from reusable_functions.file_operations import write_to_text_file
from reusable_functions.os_operations import join_paths


class VhdlGenerator:

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("models", "vhdl_templates"),
            autoescape=select_autoescape()
        )
        self.project_path_controller = ProjectPathController.get_instance()

    def render_template(self, template_name, configurations, output_path):
        top_level_name = self.project_path_controller.get_top_level_name()
        template = self.env.get_template(template_name)
        rendered_content = template.render(configurations)

        if template_name == 'top_level.vhd.jinja':
            template_path = join_paths(output_path, f"{top_level_name}.vhd")
        else:
            template_path = join_paths(output_path, template_name.replace('.jinja', ''))

        write_to_text_file(template_path, rendered_content)

    def generate_script(self, project_path):
        vhdl_generator = VhdlGenerator()
        configurations = {'top_level_name': self.project_path_controller.get_top_level_name()}
        script_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.sh.jinja'
        script_file = 'synthesis_linux.sh' if platform.system() == 'Linux' else 'synthesis_windows.sh'

        vhdl_generator.render_template(script_template, configurations=configurations, output_path=project_path)
        return join_paths(project_path, script_file)
