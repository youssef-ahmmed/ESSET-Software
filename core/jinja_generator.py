import platform

from jinja2 import Environment, select_autoescape, PackageLoader

from controllers.project_path_controller import ProjectPathController
from reusable_functions.file_operations import write_to_text_file
from reusable_functions.os_operations import join_paths


class JinjaGenerator:

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("models", "vhdl_templates"),
            autoescape=select_autoescape()
        )
        self.project_path_controller = ProjectPathController.get_instance()

    def render_templates(self, template_names, configurations, output_path):
        top_level_name = self.project_path_controller.get_top_level_name()

        for template_name in template_names:
            template = self.env.get_template(template_name)
            rendered_content = template.render(configurations)

            if template_name == 'top_level.vhd.jinja':
                template_path = join_paths(output_path, f"{top_level_name}.vhd")
            else:
                template_path = join_paths(output_path, template_name.replace('.jinja', ''))

            write_to_text_file(template_path, rendered_content)
