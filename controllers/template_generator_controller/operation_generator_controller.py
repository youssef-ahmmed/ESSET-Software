from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from controllers.template_generator_controller.replay_attack_templates_generator import ReplayAttackTemplatesGenerator
from controllers.template_generator_controller.sniffing_templates_generator import SniffingTemplatesGenerator
from controllers.template_generator_controller.stream_finder_templates_generator import StreamFinderTemplatesGenerator


class OperationGeneratorController:

    def __init__(self):
        self.attack_operation_option = AttackOperationSelectController.get_instance().get_selected_attack_operation()

    def render_uart_templates(self, configuration: dict):
        if self.attack_operation_option == "Sniffing":
            SniffingTemplatesGenerator().render_uart_receiver_templates(configuration)
        elif self.attack_operation_option == "Replay Attack":
            ReplayAttackTemplatesGenerator().render_uart_transmitter_templates(configuration)
        elif self.attack_operation_option == "Stream Finder":
            StreamFinderTemplatesGenerator().render_stream_finder_templates(configuration, "UART")

    def render_spi_templates(self, configuration: dict):
        if self.attack_operation_option == "Sniffing":
            SniffingTemplatesGenerator().render_spi_slave_templates(configuration)
        elif self.attack_operation_option == "Replay Attack":
            ReplayAttackTemplatesGenerator().render_spi_master_templates(configuration)
        elif self.attack_operation_option == "Stream Finder":
            StreamFinderTemplatesGenerator().render_stream_finder_templates(configuration, "SPI")
