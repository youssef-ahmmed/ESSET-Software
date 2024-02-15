from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from qfluentwidgets import ComboBox

from controllers.sniffing_controller.communication_protocol_controller.spi_dialog_controller import SpiDialogController
from controllers.sniffing_controller.communication_protocol_controller.uart_dialog_controller import \
    UartDialogController
from views.sniffing.communication_protocols.spi_config import SpiConfigurations
from views.sniffing.communication_protocols.uart_config import UartConfigurations


class CommunicationProtocolSelect(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        self.spi_page = SpiConfigurations()
        self.spi_controller = SpiDialogController.get_instance(self.spi_page)

        self.uart_page = UartConfigurations()
        self.uart_controller = UartDialogController.get_instance(self.uart_page)

        self.selected_protocol = None
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        comm_label = QLabel("Communication Protocol")

        self.protocol_combo = ComboBox()
        self.protocol_combo.addItems(["Choose", "UART", "SPI", "I2C"])

        layout.addWidget(comm_label)
        layout.addWidget(self.protocol_combo)

        self.setLayout(layout)
        self.protocol_combo.currentIndexChanged.connect(self.show_selected_settings)

    def show_selected_settings(self, index):
        if index >= 0:
            self.selected_protocol = self.protocol_combo.itemText(index)

            if self.selected_protocol == "SPI":
                self.show_spi_settings()

            elif self.selected_protocol == "UART":
                self.show_uart_settings()

    def show_spi_settings(self):
        self.spi_controller.show_spi_dialog()

    def show_uart_settings(self):
        self.uart_controller.show_uart_dialog()

    def get_selected_protocol(self):
        return self.protocol_combo.currentText()
