from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class SniffingTemplatesGenerator(TemplateGeneratorController):

    def render_uart_receiver_templates(self, configurations):
        template_names = ['UART_Receiver.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_spi_slave_templates(self, configurations):
        template_names = ['SPI_Slave.vhd.jinja']
        self.render_templates(template_names, configurations)
