import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtCore import QSettings, QThread, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QSystemTrayIcon, QCheckBox

import resources
from model.data_provider.task_import_products_and_persist import TaskImportProductsAndPersist
from model.data_provider.task_import_sellers_and_persist import TaskImportSellersAndPersist
from .ui.ui_mainwindow import Ui_MainWindow
from model.data.database_manager import DatabaseManager
from model.data_provider.task_import_sales_and_persist import TaskImportSalesAndPersist
from model.data_provider.task_schedule import TaskSchedule


class MainApplication(QMainWindow, Ui_MainWindow):
    __manager = DatabaseManager()
    __tray: QSystemTrayIcon
    __settings = QSettings("Ronald Santos", "OMIE Data Extractor")
    __task_schedule: TaskSchedule = None

    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setup()
        self.__manager.create_all_tables()

    def setup(self):
        self.adjustSize()
        icon = QtGui.QIcon(":/logo.png")
        self.setWindowIcon(icon)
        self.setup_tray_icon(icon)

        self.start_date_dateedit.setDate(datetime.now())
        self.end_date_dateedit.setDate(datetime.now())

        self.retroactive_importation_push_button.pressed.connect(
            self.on_click_retroactive_importation_push_button
        )
        self.start_monit_push_button.pressed.connect(
            self.on_click_start_monit_push_button
        )
        self.import_products_push_button.pressed.connect(
            self.on_click_import_products_push_button
        )
        self.import_sellers_push_button.pressed.connect(
            self.on_click_import_sellers_push_button
        )

        self.omie_app_key_line_edit.textChanged.connect(
            lambda text: self.__settings.setValue("omie_app_key", text)
        )
        self.omie_app_secret_line_edit.textChanged.connect(
            lambda text: self.__settings.setValue("omie_app_secret", text)
        )
        self.page_size_spin_box.textChanged.connect(
            lambda text: self.__settings.setValue("omie_page_size", text)
        )
        self.hour_for_importation_time_edit.timeChanged.connect(
            lambda time: self.__settings.setValue("hour_to_import", time.toString("hh:mm:ss"))
        )
        self.family_code_line_edit.textChanged.connect(
            lambda code: self.__settings.setValue("family_code", code)
        )
        self.check_products_elanco_local_check_box.stateChanged.connect(
            lambda state: self.__settings.setValue("check_elanco_products_in_local_database", state)
        )

        self.load_settings()

    def load_settings(self):
        omie_app_key = self.__settings.value("omie_app_key", defaultValue="", type=str)
        omie_app_secret = self.__settings.value("omie_app_secret", defaultValue="", type=str)
        omie_page_size = self.__settings.value("omie_page_size", defaultValue=20, type=int)
        hour_to_import = self.__settings.value("hour_to_import", defaultValue="21:00:00", type=str)
        family_code = self.__settings.value("family_code", defaultValue="", type=str)
        check_elanco_products_in_local_database = self.__settings.value(
            "check_elanco_products_in_local_database",
            defaultValue=Qt.CheckState.Unchecked,
            type=int
        )

        self.omie_app_key_line_edit.setText(omie_app_key)
        self.omie_app_secret_line_edit.setText(omie_app_secret)
        self.page_size_spin_box.setValue(omie_page_size)
        self.hour_for_importation_time_edit.setTime(datetime.strptime(hour_to_import, "%H:%M:%S").time())
        self.family_code_line_edit.setText(family_code)
        self.check_products_elanco_local_check_box.setCheckState(check_elanco_products_in_local_database)

    def setup_tray_icon(self, icon):
        self.__tray = QSystemTrayIcon(self)
        self.__tray.setIcon(icon)
        self.__tray.activated.connect(self.show)
        self.__tray.setVisible(True)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        question = QMessageBox(self)
        question.setWindowTitle("Atenção!")
        question.setText("Deseja encerrar o aplicativo?")
        question.addButton("Fechar", QMessageBox.YesRole)
        question.addButton("Minimizar", QMessageBox.NoRole)
        question.addButton("Cancelar", QMessageBox.ResetRole)
        result = question.exec_()
        if result == 0:
            a0.accept()
            return
        elif result == 1:
            self.__tray.showMessage("Atenção!", "Ainda estou em execução aqui em baixo!", QSystemTrayIcon.Information)
            self.hide()
        a0.ignore()

    def kill_app(self):
        self.__manager.close()
        sys.exit(0)

    def on_click_retroactive_importation_push_button(self):
        if self.start_date_dateedit.date() > self.end_date_dateedit.date():
            QMessageBox.warning(self, "Atenção", "A data inicial deve ser menor que a data final")
            return
        start_date = self.start_date_dateedit.date().toString('dd/MM/yyyy')
        end_date = self.end_date_dateedit.date().toString('dd/MM/yyyy')
        check_products_in_local_database = self.check_products_elanco_local_check_box.isChecked()

        task = TaskImportSalesAndPersist(self, start_date, end_date, check_products_in_local_database)
        self.bind_task_events(task)
        task.start()

    def on_click_import_products_push_button(self):
        filters: dict = None
        if self.family_code_line_edit.text().strip():
            filters = {"filtrar_apenas_familia": self.family_code_line_edit.text().strip()}
        task = TaskImportProductsAndPersist(self, filters)
        self.bind_task_events(task)
        task.start()

    def on_click_import_sellers_push_button(self):
        task = TaskImportSellersAndPersist(self)
        self.bind_task_events(task)
        task.start()

    def bind_task_events(self, task: QThread):
        task.on_error.connect(lambda error: QMessageBox.critical(self, "Ops ocorreu um erro!", str(error)))
        task.is_processing.connect(lambda is_processing: self.progress_bar.setMaximum(0 if is_processing else 100))
        task.on_finished.connect(lambda x: QMessageBox.information(self, "Opa!", "processo finalizado!"))
        task.on_message.connect(self.messages_label.setText)

    def on_click_start_monit_push_button(self):
        if self.start_monit_push_button.text() == "Iniciar monitoramento":
            self.start_monit_push_button.setText("Parar monitoramento")
            self.enable_or_disable_controls(should_enable=False)

            self.__task_schedule = TaskSchedule(self, self.hour_for_importation_time_edit.time().toString("hh:mm:ss"))
            self.__task_schedule.on_error.connect(
                lambda error: QMessageBox.critical(self, "Erro na importação", str(error))
            )
            self.__task_schedule.is_processing.connect(self.monit_status)
            self.__task_schedule.is_importing.connect(lambda is_importing: self.progress_bar.setMaximum(0 if is_importing else 100))
            self.__task_schedule.on_message.connect(self.messages_label.setText)
            self.__task_schedule.start()
        else:
            self.__task_schedule.stop()

    def monit_status(self, is_processing):
        if not is_processing:
            self.start_monit_push_button.setText("Iniciar monitoramento")
            self.enable_or_disable_controls(should_enable=True)

    def enable_or_disable_controls(self, should_enable):
        self.omie_app_key_line_edit.setEnabled(should_enable)
        self.omie_app_secret_line_edit.setEnabled(should_enable)
        self.page_size_spin_box.setEnabled(should_enable)
        self.hour_for_importation_time_edit.setEnabled(should_enable)
        self.retroactive_importation_gb.setEnabled(should_enable)