from controllers.sniffing_controller.data_sniffing_collector_controller import DataCollectorController
from models.dto.uart_protocol_dto import UartProtocolDto
from models.dao.uart_protocol_dao import UartProtocolDao
from models.dao.sniffed_data_dao import SniffedDataDao


class UartStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.uart_protocol_dto = None
        self.uart_protocol_dao = None

    def store_uart_protocol(self):
        uart_data = self.data_collector_controller.collect_uart_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        self.uart_protocol_dto = UartProtocolDto(last_sniffed_data_id, **uart_data)
        self.uart_protocol_dao = UartProtocolDao(self.uart_protocol_dto)
        self.uart_protocol_dao.insert()
