import os

from jinja2 import Environment, select_autoescape, PackageLoader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.join(ROOT_DIR, 'models', 'VHDL')


class VhdlGenerator:

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("models", "vhdl_templates"),
            autoescape=select_autoescape()
        )

    def render_template(self, template_name, configurations, output_path):
        template = self.env.get_template(template_name)
        rendered_content = template.render(configurations)

        template_path = os.path.join(output_path, template_name.replace('.jinja', ''))
        with open(template_path, 'w') as file:
            file.write(rendered_content)


# Dummy Data
renderer = VhdlGenerator()

config = {
    'channels_number': 6,
    'output_channels_number': 8,
    'clocks_per_bit': 5208,
    'option': "UART",
    'project_name': "new_test",
    'bits_per_frame': 8,
}

renderer.render_template('top_level.vhd.jinja', config, PROJECT_PATH)
