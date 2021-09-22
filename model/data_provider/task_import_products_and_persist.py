from model.data_provider.task_base import TaskBase


class TaskImportProductsAndPersist(TaskBase):
    __filters: dict

    def __init__(self, parent=None, filters: dict = None) -> None:
        super(TaskImportProductsAndPersist, self).__init__(parent)
        self.__filters = filters

    def run(self) -> None:
        try:
            self.is_processing.emit(True)
            self.on_message.emit(f"Importando produtos...")
            self.data_provider.import_products(self.__filters)
            self.on_message.emit(f"Produtos importadas com sucesso")
            self.is_processing.emit(False)
            self.on_finished.emit(True)
        except Exception as e:
            self.logger.error(
                f"Ocorreu um erro inesperado na importação dos produtos",
                exc_info=True,
                stack_info=True
            )
            self.on_message.emit("Ocorreu um erro na importação! Veja log na pasta do programa.")
            self.is_processing.emit(False)
            self.on_error.emit(e)
