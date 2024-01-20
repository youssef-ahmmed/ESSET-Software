class UartProtocolDto:
    def __init__(self, sniffed_data_id: int, clk_per_bit: int, baud_rate: int,
                 data_size: int, stop_bit: int, parity_bit: str):
        self.sniffed_data_id = sniffed_data_id
        self.clk_per_bit = clk_per_bit
        self.baud_rate = baud_rate
        self.data_size = data_size
        self.stop_bit = stop_bit
        self.parity_bit = parity_bit
