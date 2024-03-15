from controllers.data_store_controller.channel_pins_store_controller import ChannelPinsStoreController
from controllers.data_store_controller.channels_data_store_controller import ChannelsDataStoreController
from controllers.data_store_controller.n_bit_store_controller import NBitStoreController
from controllers.data_store_controller.one_bit_store_controller import OneBitStoreController
from controllers.data_store_controller.sniffed_data_store_controller import SniffedDataStoreController
from controllers.data_store_controller.spi_store_controller import SpiStoreController
from controllers.data_store_controller.uart_store_controller import UartStoreController
from controllers.sniffing_controller.data_sniffing_collector_controller import DataCollectorController


class StoreSniffingConfigurationsController:

    def __init__(self):
        self.data_collector = DataCollectorController()

    def store_sniffing_configurations(self):
        sniffed_data_store = SniffedDataStoreController()
        sniffed_data_store.store_sniffed_data()

        channel_pins_store = ChannelPinsStoreController()
        channel_pins_store.store_channel_pins()

        _, connection_way, comm_protocol = self.data_collector.collect_sniffing_option().values()

        self.store_comm_protocol(comm_protocol)
        self.store_connection_way(connection_way)

        channels_data_store = ChannelsDataStoreController()
        channels_data_store.store_channels_data()

    @staticmethod
    def store_comm_protocol(comm_protocol):
        uart_store = UartStoreController()
        spi_store = SpiStoreController()
        comm_protocol_handlers = {
            'UART': uart_store.store_uart_protocol,
            'SPI': spi_store.store_spi_protocol,
        }
        if comm_protocol in comm_protocol_handlers:
            comm_protocol_handlers[comm_protocol]()

    @staticmethod
    def store_connection_way(connection_way):
        one_bit_store = OneBitStoreController()
        n_bit_store = NBitStoreController()
        connection_way_handlers = {
            '1Bit': one_bit_store.store_one_bit_sniffing,
            'NBits': n_bit_store.store_n_bit_sniffing,
        }
        if connection_way in connection_way_handlers:
            connection_way_handlers[connection_way]()
