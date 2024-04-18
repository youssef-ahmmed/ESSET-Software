from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class ReplayAttackTemplatesGenerator(TemplateGeneratorController):

    def render_uart_transmitter_templates(self, configurations):
        template_names = ['UART_Transmitter.vhd.jinja']
        self.render_templates(template_names, configurations)

    def render_spi_master_templates(self, configurations):
        template_names = ['SPI_Master.vhd.jinja']
        self.render_templates(template_names, configurations)
