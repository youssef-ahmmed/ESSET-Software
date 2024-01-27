from PyQt5.QtCore import QObject
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from models import log_messages


class SpiDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(spi_setting_dialog=None):
        if SpiDialogController._instance is None:
            SpiDialogController._instance = SpiDialogController(spi_setting_dialog)
        return SpiDialogController._instance

    def __init__(self, spi_setting_dialog):
        super(SpiDialogController, self).__init__()

        if SpiDialogController._instance is not None:
            raise Exception("An instance of SpiDialogController already exists. Use get_instance() to access it.")

        self.spi_setting_dialog = spi_setting_dialog
        self.project_path_controller = ProjectPathController.get_instance()
        self.spi_configurations = []

        self.handle_spi_settings_buttons()

    def handle_spi_settings_buttons(self):
        self.spi_setting_dialog.cancel_button.clicked.connect(self.spi_setting_dialog.reject)
        self.spi_setting_dialog.reset_button.clicked.connect(self.spi_setting_dialog.reset_settings)
        self.spi_setting_dialog.save_button.clicked.connect(self.save_spi_settings)

    def save_spi_settings(self):
        self.project_path = self.project_path_controller.get_project_path()

        if not self.project_path:
            self.project_path_controller.show_error_dialog(self.spi_setting_dialog.save_button)
            return

        self.spi_configurations = self.collect_spi_settings()
        if self.spi_configurations is not None:
            self.spi_setting_dialog.accept()
            logger.success(log_messages.SPI_CONFIG_SET)

    def show_spi_dialog(self):
        try:
            self.spi_setting_dialog.setParent(None)
            self.spi_setting_dialog.exec_()
        except Exception as e:
            print(f"Error in show_spi_dialog: {e}")

    def collect_spi_settings(self):
        mosi = self.spi_setting_dialog.mosi_combo.currentText()
        miso = self.spi_setting_dialog.miso_combo.currentText()
        clock = self.spi_setting_dialog.clock_combo.currentText()
        enable = self.spi_setting_dialog.enable_combo.currentText()
        significant_bit = self.spi_setting_dialog.significant_bit_combo.currentText()
        bits_per_transfer = self.spi_setting_dialog.bits_per_transfer_combo.currentText()
        clock_state = self.spi_setting_dialog.clock_state_combo.currentText()
        clock_phase = self.spi_setting_dialog.clock_phase_combo.currentText()

        settings = {
            "MOSI": mosi,
            "MISO": miso,
            "Clock": clock,
            "Enable": enable
        }
        spi_configurations = {
            'option': 'SPI',
            'top_level_name': self.project_path_controller.get_top_level_name(),
            "MOSI": mosi,
            "MISO": miso,
            "Clock": clock,
            "Enable": enable,
            'significant_bit': significant_bit,
            'bits_per_transfer': bits_per_transfer,
            'clock_state': clock_state,
            'clock_phase': clock_phase
        }

        for channel_name, channel_value in settings.items():
            if channel_value == "Select Channel":
                self.spi_setting_dialog.show_spi_channel_warning(channel_name)
                return None

        return spi_configurations
