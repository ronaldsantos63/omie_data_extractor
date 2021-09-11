import logging

from PyQt5.QtCore import QThread, pyqtSignal

from model.data_provider.omie_data_provider import OmieDataProvider


class TaskImportSalesAndPersist(QThread):
    __logger = logging.getLogger(__name__)

    is_processing = pyqtSignal(bool)
    on_message = pyqtSignal(str)
    on_error = pyqtSignal(Exception)
    on_finished = pyqtSignal(bool)

    __data_provider = OmieDataProvider()
    __start_date: str
    __end_date: str

    def __init__(self, parent=None, start_date: str = "", end_date: str = "") -> None:
        super(TaskImportSalesAndPersist, self).__init__(parent)
        self.__start_date = start_date
        self.__end_date = end_date

    def run(self) -> None:
        try:
            self.is_processing.emit(True)
            self.on_message.emit(f"Importando vendas de {self.__start_date} até {self.__end_date}")
            self.__data_provider.import_sales_history_by_period(self.__start_date, self.__end_date)
            self.on_message.emit(f"Vendas importadas com sucesso")
            self.is_processing.emit(False)
            self.on_finished.emit(True)
        except Exception as e:
            self.__logger.error(
                f"Ocorreu um erro inesperado na importação das vendas",
                exc_info=True,
                stack_info=True
            )
            self.on_message.emit("Ocorreu um erro na importação! Veja log na pasta do programa.")
            self.is_processing.emit(False)
            self.on_error.emit(e)
