import platform

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox

from controllers.project_path_controller import ProjectPathController
from core.qsf_writer import QsfWriter
from core.vhdl_generator import VhdlGenerator


class BitsInputDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(bits_input_dialog=None):
        if BitsInputDialogController._instance is None:
            BitsInputDialogController._instance = BitsInputDialogController(bits_input_dialog)
        return BitsInputDialogController._instance

    def __init__(self, bits_input_dialog):
        super(BitsInputDialogController, self).__init__()

        if BitsInputDialogController._instance is not None:
            raise Exception("An instance of BitsInputDialogController already exists. Use get_instance() to access it.")

        self.bits_input_dialog = bits_input_dialog
        self.n_bits = None
        self.project_path_controller = ProjectPathController.get_instance()

        self.handle_buttons()

    def handle_buttons(self):
        self.bits_input_dialog.cancel_button.clicked.connect(self.bits_input_dialog.reject)
        self.bits_input_dialog.save_button.clicked.connect(self.save_clicked)

    def save_clicked(self):
        self.project_path = self.project_path_controller.get_project_path()

        if not self.project_path:
            self.project_path_controller.show_error_dialog(self.bits_input_dialog)
            return

        bits_number = self.get_bits_number()
        if bits_number is not None:
            print(f"Number of bits: {bits_number}")
            self.bits_input_dialog.accept()
            self.render_NBit_templates()

    def get_bits_number(self):
        no_of_bits = self.bits_input_dialog.bits_input.text()
        if not no_of_bits:
            QMessageBox.warning(self.bits_input_dialog, "Warning", "Please enter the number of bits.")
            return None
        self.bits_input_dialog.bits_input.clear()

        self.NBit_configurations = {
            'option': 'NBit_Sniffing',
            'top_level_name': ProjectPathController.get_instance().get_top_level_name(),
            'channels_number': no_of_bits
        }

        return self.NBit_configurations

    def render_NBit_templates(self):
        vhdl_generator = VhdlGenerator()
        qsf_writer = QsfWriter()

        templates = [
            'top_level.vhd.jinja',
            'NBit_Sniffing.vhd.jinja',
            'Common_Ports.vhd.jinja',
            'Communication_Module.vhd.jinja'
        ]

        for template in templates:
            vhdl_generator.render_template(template_name=template,
                                           configurations=self.NBit_configurations, output_path=self.project_path)

        synthesis_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.bat.jinja'
        vhdl_generator.render_template(template_name=synthesis_template,
                                       configurations=self.NBit_configurations, output_path=self.project_path)
        qsf_writer.write_vhdl_files_to_qsf()
