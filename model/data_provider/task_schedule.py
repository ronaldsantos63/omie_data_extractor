import logging
from datetime import datetime
from PyQt5.QtCore import QThread, pyqtSignal

from model.data_provider.task_import_sales_and_persist import TaskImportSalesAndPersist


class TaskSchedule(QThread):
    __logger = logging.getLogger(__name__)
    __hour_for_execute: str
    __should_stop = False

    is_processing = pyqtSignal(bool)
    on_error = pyqtSignal(Exception)
    is_importing = pyqtSignal(bool)
    on_message = pyqtSignal(str)

    def __init__(self, parent=None, hour_for_execute: str = None) -> None:
        super(TaskSchedule, self).__init__(parent)
        self.__hour_for_execute = hour_for_execute

    def stop(self):
        self.__should_stop = True

    def run(self) -> None:
        self.on_message.emit("Monitoramento iniciado!")
        try:
            while True:
                if self.__should_stop:
                    self.on_message.emit("Encerrando monitoramento...")
                    break
                if self.__hour_for_execute == datetime.now().strftime("%H:%M:%S"):
                    self.is_importing.emit(True)
                    self.__logger.info("Importação de Vendas iniciada...")
                    current_date_str = datetime.now().strftime("%d/%m/%Y")
                    task = TaskImportSalesAndPersist(self.parent(), current_date_str, current_date_str)
                    task.on_error.connect(lambda error: self.on_error.emit(error))
                    task.on_message.connect(lambda message: self.on_message.emit(message))
                    task.start()

                    while task.isRunning():
                        if self.__should_stop:
                            self.on_message.emit("Encerrando monitoramento...")
                            break
                        continue
                    self.is_importing.emit(False)
                    self.__logger.info("Importação finalizada")
            self.is_processing.emit(False)
            self.on_message.emit("Monitoramento encerrado")
        except Exception as e:
            self.__logger.error(
                "Ocorreu um erro desconhecido na importação das vendas na thread de agenda",
                exc_info=True,
                stack_info=True
            )
            self.on_message.emit("Ocorreu um erro inesperado, por favor veja o log de erro.")
            self.is_processing.emit(False)
            self.on_error.emit(e)
