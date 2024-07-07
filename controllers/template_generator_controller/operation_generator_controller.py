from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from controllers.template_generator_controller.conditional_bypass_templates_generator import \
    ConditionalBypassTemplatesGenerator
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
                "UART": ReplayAttackTemplatesGenerator().render_uart_templates,
                "SPI": ReplayAttackTemplatesGenerator().render_spi_templates,
            },
            "Conditional Bypass": {
                "UART": ConditionalBypassTemplatesGenerator().render_uart_conditional_bypass_templates,
                "SPI": ConditionalBypassTemplatesGenerator().render_spi_conditional_bypass_templates,
            },
            "Stream Finder": {
                "UART": StreamFinderTemplatesGenerator().render_uart_stream_finder_templates,
                "SPI": StreamFinderTemplatesGenerator().render_spi_stream_finder_templates,
            },
        }

    def render_uart_templates(self, configuration: dict):
        self._render_templates("UART", configuration)

    def render_spi_templates(self, configuration: dict):
        self._render_templates("SPI", configuration)

    def _render_templates(self, protocol, configuration):
        if self.attack_operation_option == "Fuzzing":
            return
        self.render_functions.get(self.attack_operation_option, {}).get(protocol)(configuration)
