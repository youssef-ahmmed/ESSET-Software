from controllers.intercept_controller.stream_finder_actions_controller import StreamFinderActionsController
from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class StreamFinderTemplatesGenerator(TemplateGeneratorController):

    def __init__(self):
        super().__init__()
        self.stream_finder_action = StreamFinderActionsController.get_instance().get_selected_stream_finder_action()

    def render_stream_finder_templates(self, configurations, option):
        render_functions = {
            "Flip Bits": self.render_stream_finder_with_flip_bits_templates,
            "Drop Communication": self.render_conditional_bypass_templates,
            "Raise Flag": self.render_stream_finder_with_raise_flags_templates,
        }
        render_functions.get(self.stream_finder_action)(configurations, option)

    def render_stream_finder_with_raise_flags_templates(self, configurations, option="UART"):
        template_names = self._get_template_names("StreamFinder.vhd.jinja", option)
        self.render_templates(template_names, configurations)

    def render_stream_finder_with_flip_bits_templates(self, configurations, option="UART"):
        template_names = self._get_template_names("StreamFinderWithFlipBits.vhd.jinja", option)
        self.render_templates(template_names, configurations)

    def render_conditional_bypass_templates(self, configurations, option="UART"):
        template_names = self._get_template_names("ConditionalByPass.vhd.jinja", option)
        self.render_templates(template_names, configurations)

    def _get_template_names(self, base_template, option):
        if option == "UART":
            return [base_template, 'UART_Receiver.vhd.jinja', 'UART_Transmitter.vhd.jinja']
        else:
            return [base_template, 'SPI_Slave.vhd.jinja', 'SPI_Master.vhd.jinja']
