from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class ConditionalBypassTemplatesGenerator(TemplateGeneratorController):

    def render_uart_conditional_bypass_templates(self, configurations):
        templates = ["ConditionalByPass.vhd.jinja", "AndGate.vhd.jinja", "StreamBuffer.vhd.jinja",
                     "UART_Receiver.vhd.jinja"]
        self.render_templates(templates, configurations)

    def render_spi_conditional_bypass_templates(self, configurations):
        templates = ["ConditionalByPass.vhd.jinja", "AndGate.vhd.jinja", "StreamBuffer.vhd.jinja",
                     "SPI_Slave.vhd.jinja"]
        self.render_templates(templates, configurations)
