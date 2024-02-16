import platform

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController
from core.qsf_writer import QsfWriter
from core.vhdl_generator import VhdlGenerator
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.file_operations import delete_files
from views.common.info_bar import create_success_bar
from views.common.message_box import MessageBox
from views.sniffing.dialogs.bits_input_dialog import BitsInputDialog

MEGA_HZ = 1_000_000


class BitsInputDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(parent=None, bits_input_dialog: BitsInputDialog = None):
        if BitsInputDialogController._instance is None:
            BitsInputDialogController._instance = BitsInputDialogController(parent, bits_input_dialog)
        return BitsInputDialogController._instance

    def __init__(self, parent, bits_input_dialog: BitsInputDialog):
        super(BitsInputDialogController, self).__init__()

        if BitsInputDialogController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.parent = parent
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
            MessageBox.show_project_path_error_dialog(self.bits_input_dialog)
            return

        bits_number = self.get_bits_number()
        if bits_number is not None:
            self.bits_input_dialog.accept()
            self.render_bit_templates()
            PinPlannerDialogController.get_instance().send_data_to_pin_planner()
            if self.sniffing_type == "One_Bit":
                create_success_bar(self.parent, 'SUCCESS', log_messages.ONE_BIT_CONFIG_SET)
                logger.success(log_messages.ONE_BIT_CONFIG_SET)
            elif self.sniffing_type == "NBits":
                create_success_bar(self.parent, 'SUCCESS', log_messages.N_BITS_CONFIG_SET)
                logger.success(log_messages.N_BITS_CONFIG_SET)

    def get_bits_number(self):
        no_of_bits = self.bits_input_dialog.bits_input.text()
        clock_rate = self.bits_input_dialog.clock_rate.text()
        if not no_of_bits:
            QMessageBox.warning(self.bits_input_dialog, "Warning", "Please enter the number of bits.")
            return None
        self.sniffing_type = NumberBitsSelectController.get_instance().get_selected_option()
        if self.sniffing_type == '1Bit':
            self.sniffing_type = 'One_Bit'
        return {
            'option': self.sniffing_type,
            'top_level_name': ProjectPathController.get_instance().get_top_level_name(),
            'channel_number': no_of_bits,
            'clock_rate': int(clock_rate) * MEGA_HZ
        }

    def render_bit_templates(self):
        vhdl_generator = VhdlGenerator()
        qsf_writer = QsfWriter()

        templates = [
            'top_level.vhd.jinja',
            str(self.sniffing_type) + '_Sniffing.vhd.jinja',
            'Common_Ports.vhd.jinja',
            'Communication_Module.vhd.jinja'
        ]
        delete_files(self.project_path, '.vhd')

        for template in templates:
            vhdl_generator.render_template(template_name=template,
                                           configurations=self.get_bits_number(),
                                           output_path=self.project_path)

        synthesis_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.bat.jinja'
        vhdl_generator.render_template(template_name=synthesis_template,
                                       configurations=self.get_bits_number(),
                                       output_path=self.project_path)
        qsf_writer.write_vhdl_files_to_qsf()
