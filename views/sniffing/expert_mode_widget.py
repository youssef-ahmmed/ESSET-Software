from views.sniffing.base_mode_widget import BaseModeWidget
from views.sniffing.vhdl_widget import VhdlWidget


class ExpertModeWidget(BaseModeWidget):

    def __init__(self):
        super().__init__(VhdlWidget())
