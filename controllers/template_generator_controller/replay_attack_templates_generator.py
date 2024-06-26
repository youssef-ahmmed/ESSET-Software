from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class ReplayAttackTemplatesGenerator(TemplateGeneratorController):

    def render_uart_templates(self, configurations):
        template_names = ['UART_Transmitter.vhd.jinja', 'UART_Receiver.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_spi_templates(self, configurations):
        template_names = ['SPI_Master.vhd.jinja', 'SPI_Slave.vhd.jinja']
        self.render_templates(template_names, configurations)
