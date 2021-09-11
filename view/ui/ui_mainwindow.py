# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 280))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.config_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.config_gb.setObjectName("config_gb")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.config_gb)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.omie_app_key_label = QtWidgets.QLabel(self.config_gb)
        self.omie_app_key_label.setObjectName("omie_app_key_label")
        self.horizontalLayout.addWidget(self.omie_app_key_label)
        self.omie_app_key_line_edit = QtWidgets.QLineEdit(self.config_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.omie_app_key_line_edit.sizePolicy().hasHeightForWidth())
        self.omie_app_key_line_edit.setSizePolicy(sizePolicy)
        self.omie_app_key_line_edit.setObjectName("omie_app_key_line_edit")
        self.horizontalLayout.addWidget(self.omie_app_key_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.omie_app_secret_label = QtWidgets.QLabel(self.config_gb)
        self.omie_app_secret_label.setObjectName("omie_app_secret_label")
        self.horizontalLayout_2.addWidget(self.omie_app_secret_label)
        self.omie_app_secret_line_edit = QtWidgets.QLineEdit(self.config_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.omie_app_secret_line_edit.sizePolicy().hasHeightForWidth())
        self.omie_app_secret_line_edit.setSizePolicy(sizePolicy)
        self.omie_app_secret_line_edit.setObjectName("omie_app_secret_line_edit")
        self.horizontalLayout_2.addWidget(self.omie_app_secret_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.config_gb)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.page_size_spin_box = QtWidgets.QSpinBox(self.config_gb)
        self.page_size_spin_box.setMaximum(100)
        self.page_size_spin_box.setProperty("value", 20)
        self.page_size_spin_box.setObjectName("page_size_spin_box")
        self.horizontalLayout_5.addWidget(self.page_size_spin_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.config_gb)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.hour_for_importation_time_edit = QtWidgets.QTimeEdit(self.config_gb)
        self.hour_for_importation_time_edit.setObjectName("hour_for_importation_time_edit")
        self.horizontalLayout_5.addWidget(self.hour_for_importation_time_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.start_monit_push_button = QtWidgets.QPushButton(self.config_gb)
        self.start_monit_push_button.setObjectName("start_monit_push_button")
        self.verticalLayout_2.addWidget(self.start_monit_push_button)
        self.verticalLayout.addWidget(self.config_gb)
        self.retroactive_importation_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.retroactive_importation_gb.setObjectName("retroactive_importation_gb")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.retroactive_importation_gb)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.retroactive_importation_gb)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.start_date_dateedit = QtWidgets.QDateEdit(self.retroactive_importation_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_date_dateedit.sizePolicy().hasHeightForWidth())
        self.start_date_dateedit.setSizePolicy(sizePolicy)
        self.start_date_dateedit.setCalendarPopup(True)
        self.start_date_dateedit.setObjectName("start_date_dateedit")
        self.horizontalLayout_3.addWidget(self.start_date_dateedit)
        self.label_4 = QtWidgets.QLabel(self.retroactive_importation_gb)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.end_date_dateedit = QtWidgets.QDateEdit(self.retroactive_importation_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_date_dateedit.sizePolicy().hasHeightForWidth())
        self.end_date_dateedit.setSizePolicy(sizePolicy)
        self.end_date_dateedit.setCalendarPopup(True)
        self.end_date_dateedit.setObjectName("end_date_dateedit")
        self.horizontalLayout_3.addWidget(self.end_date_dateedit)
        self.retroactive_importation_push_button = QtWidgets.QPushButton(self.retroactive_importation_gb)
        self.retroactive_importation_push_button.setObjectName("retroactive_importation_push_button")
        self.horizontalLayout_3.addWidget(self.retroactive_importation_push_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.retroactive_importation_gb)
        self.messages_label = QtWidgets.QLabel(self.centralwidget)
        self.messages_label.setText("")
        self.messages_label.setObjectName("messages_label")
        self.verticalLayout.addWidget(self.messages_label)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OMIE Data Extractor"))
        self.config_gb.setTitle(_translate("MainWindow", "Config"))
        self.omie_app_key_label.setText(_translate("MainWindow", "OMIE App Key:"))
        self.omie_app_secret_label.setText(_translate("MainWindow", "OMIE App Secret:"))
        self.label_2.setText(_translate("MainWindow", "Tamanho da página:"))
        self.label.setText(_translate("MainWindow", "Horário para importação dos dados:"))
        self.hour_for_importation_time_edit.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.start_monit_push_button.setText(_translate("MainWindow", "Iniciar monitoramento"))
        self.retroactive_importation_gb.setTitle(_translate("MainWindow", "Importar retroativo"))
        self.label_3.setText(_translate("MainWindow", "Data inicial:"))
        self.label_4.setText(_translate("MainWindow", "Data final:"))
        self.retroactive_importation_push_button.setText(_translate("MainWindow", "Iniciar importação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
