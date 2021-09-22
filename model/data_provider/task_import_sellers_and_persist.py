from model.data_provider.task_base import TaskBase


class TaskImportSellersAndPersist(TaskBase):
    def __init__(self, parent=None) -> None:
        super(TaskImportSellersAndPersist, self).__init__(parent)

    def run(self) -> None:
        try:
            self.is_processing.emit(True)
            self.on_message.emit(f"Importando vendedores...")
            self.data_provider.import_sellers()
            self.on_message.emit(f"Vendedores importadas com sucesso")
            self.is_processing.emit(False)
            self.on_finished.emit(True)
        except Exception as e:
            self.logger.error(
                f"Ocorreu um erro inesperado na importação dos vendedores",
                exc_info=True,
                stack_info=True
            )
            self.on_message.emit("Ocorreu um erro na importação! Veja log na pasta do programa.")
            self.is_processing.emit(False)
            self.on_error.emit(e)