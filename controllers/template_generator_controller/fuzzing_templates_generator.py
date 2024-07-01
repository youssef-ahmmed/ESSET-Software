from controllers.fuzzing_controller.data_operation_controller import DataOperationController
from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class FuzzingTemplatesGenerator(TemplateGeneratorController):
    def __init__(self):
        super().__init__()
        self.attack_operation = AttackOperationSelectController.get_instance().get_selected_attack_operation()
        self.fuzz_on = DataOperationController.get_instance().get_selected_fuzzing_protocol()
        self.sniff_on = DataOperationController.get_instance().get_selected_sniffing_protocol()
        self.configurations = {
            "attack_operation": self.attack_operation,
            "fuzz_on": self.fuzz_on,
            "sniff_on": self.sniff_on,
            "clk_per_bit": 5208,
            "output_size": 8
        }

    def render_fuzzing_templates(self):
        templates_mapping = {
            ("UART", "UART"): ['UART_Transmitter.vhd.jinja', 'UART_Receiver.vhd.jinja'],
            ("UART", "SPI"): ['UART_Transmitter.vhd.jinja', 'SPI_Slave.vhd.jinja'],
            ("SPI", "SPI"): ['SPI_Master.vhd.jinja', 'SPI_Slave.vhd.jinja'],
            ("SPI", "UART"): ['SPI_Master.vhd.jinja', 'UART_Receiver.vhd.jinja']
        }

        templates = templates_mapping.get((self.fuzz_on, self.sniff_on))
        self.render_templates(templates, self.configurations)
