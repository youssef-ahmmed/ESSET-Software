class SpiProtocolDto:
    def __init__(self, sniffed_data_id: int, clock_rate: int, significant_bit: str, clk_state: int, clk_phase: int, data_size: int):
        self.sniffed_data_id = sniffed_data_id
        self.clock_rate = clock_rate
        self.significant_bit = significant_bit
        self.clk_state = clk_state
        self.clk_phase = clk_phase
        self.data_size = data_size
