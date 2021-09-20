import logging

from PyQt5.QtCore import QThread, pyqtSignal

from model.data_provider.omie_data_provider import OmieDataProvider


class TaskBase(QThread):
    logger = logging.getLogger(__name__)

    is_processing = pyqtSignal(bool)
    on_message = pyqtSignal(str)
    on_error = pyqtSignal(Exception)
    on_finished = pyqtSignal(bool)

    data_provider = OmieDataProvider()

    def __init__(self, parent=None) -> None:
        super(TaskBase, self).__init__(parent)
