from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController
from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class SniffingActionController:
    def __init__(self) -> None:
        self.sniffing_timer_dialog = SniffingTimer()
        SniffingTimerDialogController.get_instance(self.sniffing_timer_dialog)
        SniffingTimerDialogController.get_instance().show_sniffing_timer_dialog()
