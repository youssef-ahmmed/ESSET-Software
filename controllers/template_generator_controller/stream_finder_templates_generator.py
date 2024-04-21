from controllers.intercept_controller.stream_finder_actions_controller import StreamFinderActionsController
from controllers.template_generator_controller.template_generator_controller import TemplateGeneratorController


class StreamFinderTemplatesGenerator(TemplateGeneratorController):

    TEMPLATE_MAPPING = {
        "Flip Bits": {
            "UART": ["StreamFinderWithFlipBits.vhd.jinja", "UART_Receiver.vhd.jinja", "UART_Transmitter.vhd.jinja"],
            "SPI": ["StreamFinderWithFlipBits.vhd.jinja", "SPI_Slave.vhd.jinja", "SPI_Master.vhd.jinja"]
        },
        "Drop Communication": {
            "UART": ["ConditionalByPass.vhd.jinja", "AndGate.vhd.jinja", "StreamBuffer.vhd.jinja",
                     "UART_Receiver.vhd.jinja"],
            "SPI": ["ConditionalByPass.vhd.jinja", "AndGate.vhd.jinja", "StreamBuffer.vhd.jinja", "SPI_Slave.vhd.jinja"]
        },
        "Raise Flag": {
            "UART": ["StreamFinder.vhd.jinja", "UART_Receiver.vhd.jinja", "UART_Transmitter.vhd.jinja"],
            "SPI": ["StreamFinder.vhd.jinja", "SPI_Slave.vhd.jinja", "SPI_Master.vhd.jinja"]
        }
    }

    def __init__(self):
        super().__init__()
        self.stream_finder_action = StreamFinderActionsController.get_instance().get_selected_stream_finder_action()

    def render_stream_finder_templates(self, configurations, option):
        templates = self.TEMPLATE_MAPPING[self.stream_finder_action][option]
        self.render_templates(templates, configurations)
