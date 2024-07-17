from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class StreamFinderTemplatesGenerator(TemplateGeneratorController):

    def render_uart_stream_finder_templates(self, configurations):
        templates = ["StreamFinder.vhd.jinja", "UART_Receiver.vhd.jinja"]
        self.render_templates(templates, configurations)

    def render_spi_stream_finder_templates(self, configurations):
        templates = ["StreamFinder.vhd.jinja", "SPI_Slave.vhd.jinja"]
        self.render_templates(templates, configurations)
