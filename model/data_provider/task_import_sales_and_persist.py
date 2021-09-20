from model.data_provider.task_base import TaskBase


class TaskImportSalesAndPersist(TaskBase):
    __start_date: str
    __end_date: str
    __check_products_in_local_database: bool

    def __init__(self, parent=None, start_date: str = "", end_date: str = "",
                 check_products_in_local_database=False) -> None:
        super(TaskImportSalesAndPersist, self).__init__(parent)
        self.__start_date = start_date
        self.__end_date = end_date
        self.__check_products_in_local_database = check_products_in_local_database

    def run(self) -> None:
        try:
            self.is_processing.emit(True)
            self.on_message.emit(f"Importando vendas de {self.__start_date} até {self.__end_date}")
            self.data_provider.import_sales_history_by_period(
                self.__start_date,
                self.__end_date,
                self.__check_products_in_local_database
            )
            self.on_message.emit(f"Vendas importadas com sucesso")
            self.is_processing.emit(False)
            self.on_finished.emit(True)
        except Exception as e:
            self.logger.error(
                f"Ocorreu um erro inesperado na importação das vendas",
                exc_info=True,
                stack_info=True
            )
            self.on_message.emit("Ocorreu um erro na importação! Veja log na pasta do programa.")
            self.is_processing.emit(False)
            self.on_error.emit(e)
