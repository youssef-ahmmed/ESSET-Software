from controllers.intercept_controller.stream_finder_actions_controller import StreamFinderActionsController
from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class StreamFinderTemplatesGenerator(TemplateGeneratorController):

    def __init__(self):
        super().__init__()
        self.stream_finder_action = StreamFinderActionsController.get_instance().get_selected_stream_finder_action()

    def render_stream_finder_templates(self, configurations, option):
        if self.stream_finder_action == "Flip Bits":
            self.render_stream_finder_with_flib_bits_templates(configurations, option)
        elif self.stream_finder_action == "Drop Communication":
            self.render_conditional_bypass_templates(configurations, option)
        elif self.stream_finder_action == "Raise Flag":
            self.render_stream_finder_with_raise_flags_templates(configurations, option)

    def render_stream_finder_with_raise_flags_templates(self, configurations, option="UART"):
        if option == "UART":
            template_names = ['StreamFinder.vhd.jinja', 'UART_Receiver.vhd.jinja', 'UART_Transmitter.vhd.jinja']
        else:
            template_names = ['StreamFinder.vhd.jinja', 'SPI_Slave.vhd.jinja', 'SPI_Master.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_stream_finder_with_flib_bits_templates(self, configurations, option="UART"):
        if option == "UART":
            template_names = ['StreamFinderWithFlipBits.vhd.jinja', 'UART_Receiver.vhd.jinja', 'UART_Transmitter.vhd.jinja']
        else:
            template_names = ['StreamFinderWithFlipBits.vhd.jinja', 'SPI_Slave.vhd.jinja', 'SPI_Master.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_conditional_bypass_templates(self, configurations, option="UART"):
        if option == "UART":
            template_names = ['ConditionalByPass.vhd.jinja', 'UART_Receiver.vhd.jinja', 'UART_Transmitter.vhd.jinja']
        else:
            template_names = ['ConditionalByPass.vhd.jinja', 'SPI_Slave.vhd.jinja', 'SPI_Master.vhd.jinja']
        self.render_templates(template_names, configurations)
