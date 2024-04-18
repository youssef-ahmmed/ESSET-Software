from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from controllers.template_generator_controller.replay_attack_templates_generator import ReplayAttackTemplatesGenerator
from controllers.template_generator_controller.sniffing_templates_generator import SniffingTemplatesGenerator
from controllers.template_generator_controller.stream_finder_templates_generator import StreamFinderTemplatesGenerator


class OperationGeneratorController:

    def __init__(self):
        self.attack_operation_option = AttackOperationSelectController.get_instance().get_selected_attack_operation()
        self.render_functions = {
            "Sniffing": {
                "UART": SniffingTemplatesGenerator().render_uart_receiver_templates,
                "SPI": SniffingTemplatesGenerator().render_spi_slave_templates,
            },
            "Replay Attack": {
                "UART": ReplayAttackTemplatesGenerator().render_uart_transmitter_templates,
                "SPI": ReplayAttackTemplatesGenerator().render_spi_master_templates,
            },
            "Stream Finder": {
                "UART": lambda config: StreamFinderTemplatesGenerator().render_stream_finder_templates(config, "UART"),
                "SPI": lambda config: StreamFinderTemplatesGenerator().render_stream_finder_templates(config, "SPI"),
            },
        }

    def render_uart_templates(self, configuration: dict):
        self._render_templates("UART", configuration)

    def render_spi_templates(self, configuration: dict):
        self._render_templates("SPI", configuration)

    def _render_templates(self, protocol, configuration):
        self.render_functions.get(self.attack_operation_option, {}).get(protocol)(configuration)
