from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QComboBox, QLabel, QHBoxLayout

from views.sniffing.spi_config import SpiConfigurations
from views.sniffing.uart_config import UartConfigurations


class CommunicationProtocolSelect(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Communication Settings")
        self.setGeometry(100, 100, 400, 300)

        self.create_layout()

    def create_layout(self):
        layout = QHBoxLayout()

        self.comm_label = QLabel("Communication Protocol")
        self.protocol_combo = QComboBox()
        self.protocol_combo.addItem("Select Comm Protocol")
        self.protocol_combo.addItems(["SPI", "UART", "I2C", "None"])
        self.protocol_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.protocol_combo.setCurrentIndex(0)
        self.protocol_combo.activated.connect(self.show_selected_settings)

        self.protocol_pages = QStackedWidget()

        spi_page = SpiConfigurations()
        self.protocol_pages.addWidget(spi_page)

        uart_page = UartConfigurations()
        self.protocol_pages.addWidget(uart_page)

        layout.addWidget(self.comm_label)
        layout.addWidget(self.protocol_combo)

        self.setLayout(layout)

    def show_selected_settings(self, index):
        if index >= 0:
            self.selected_protocol = self.protocol_combo.itemText(index)

            if self.selected_protocol == "SPI":
                self.show_spi_settings()

            elif self.selected_protocol == "UART":
                self.show_uart_settings()

    def show_spi_settings(self):
        spi_dialog = SpiConfigurations()
        spi_dialog.exec_()

    def show_uart_settings(self):
        uart_dialog = UartConfigurations()
        uart_dialog.exec_()

    def get_selected_protocol(self):
        return self.protocol_combo.currentText()
