# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 733)
        MainWindow.setMinimumSize(QSize(1182, 733))
        MainWindow.setMaximumSize(QSize(1182, 733))
        icon = QIcon()
        icon.addFile(u"../assets/icon/batch.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"    background-color: #F6F6F6;\n"
"}\n"
"QFrame\n"
"{\n"
"	border: 2px solid #6D9886;\n"
"}\n"
"QLabel\n"
"{\n"
"	color: #212121;\n"
"	border: 0px;\n"
"	font-family: constantia;\n"
"}\n"
"QLCDNumber\n"
"{\n"
"	border: 0px;\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(200, 10, 771, 41))
        font = QFont()
        font.setFamily(u"constantia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 220, 381, 451))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.captura_tableWidget = QTableWidget(self.frame)
        if (self.captura_tableWidget.columnCount() < 4):
            self.captura_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.captura_tableWidget.setObjectName(u"captura_tableWidget")
        self.captura_tableWidget.setGeometry(QRect(10, 10, 361, 371))
        self.captura_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.iniciar_pushButton = QPushButton(self.frame)
        self.iniciar_pushButton.setObjectName(u"iniciar_pushButton")
        self.iniciar_pushButton.setEnabled(False)
        self.iniciar_pushButton.setGeometry(QRect(20, 410, 341, 28))
        self.iniciar_pushButton.setChecked(False)
        self.iniciar_pushButton.setFlat(False)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(400, 60, 381, 611))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lote_Actual = QLabel(self.frame_2)
        self.lote_Actual.setObjectName(u"lote_Actual")
        self.lote_Actual.setGeometry(QRect(130, 10, 31, 20))
        font1 = QFont()
        font1.setFamily(u"constantia")
        font1.setPointSize(9)
        self.lote_Actual.setFont(font1)
        self.lote_Actual.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 10, 21, 21))
        self.lote_Total = QLabel(self.frame_2)
        self.lote_Total.setObjectName(u"lote_Total")
        self.lote_Total.setGeometry(QRect(190, 10, 31, 21))
        self.lote_Total.setFont(font1)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 10, 31, 21))
        self.ejecuccion_tableWidget = QTableWidget(self.frame_2)
        if (self.ejecuccion_tableWidget.columnCount() < 5):
            self.ejecuccion_tableWidget.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.ejecuccion_tableWidget.setObjectName(u"ejecuccion_tableWidget")
        self.ejecuccion_tableWidget.setGeometry(QRect(10, 50, 361, 201))
        self.ejecuccion_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.transcurrido_lcdNumber = QLCDNumber(self.frame_2)
        self.transcurrido_lcdNumber.setObjectName(u"transcurrido_lcdNumber")
        self.transcurrido_lcdNumber.setGeometry(QRect(210, 452, 71, 21))
        self.transcurrido_lcdNumber.setAutoFillBackground(False)
        self.transcurrido_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.transcurrido_lcdNumber.setFrameShape(QFrame.Box)
        self.transcurrido_lcdNumber.setProperty("intValue", 0)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 260, 131, 21))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 350, 91, 31))
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 390, 141, 21))
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 320, 31, 21))
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 450, 191, 21))
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 480, 191, 21))
        self.restante_lcdNumber = QLCDNumber(self.frame_2)
        self.restante_lcdNumber.setObjectName(u"restante_lcdNumber")
        self.restante_lcdNumber.setGeometry(QRect(210, 480, 71, 21))
        self.restante_lcdNumber.setAutoFillBackground(False)
        self.restante_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.restante_lcdNumber.setFrameShape(QFrame.Box)
        self.restante_lcdNumber.setProperty("intValue", 0)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 530, 191, 31))
        self.total_lcdNumber = QLCDNumber(self.frame_2)
        self.total_lcdNumber.setObjectName(u"total_lcdNumber")
        self.total_lcdNumber.setGeometry(QRect(210, 530, 81, 31))
        self.total_lcdNumber.setAutoFillBackground(False)
        self.total_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.total_lcdNumber.setFrameShape(QFrame.Box)
        self.total_lcdNumber.setProperty("intValue", 0)
        self.Id_label = QLabel(self.frame_2)
        self.Id_label.setObjectName(u"Id_label")
        self.Id_label.setGeometry(QRect(120, 320, 221, 21))
        font2 = QFont()
        font2.setFamily(u"constantia")
        font2.setPointSize(10)
        self.Id_label.setFont(font2)
        self.operacion_label = QLabel(self.frame_2)
        self.operacion_label.setObjectName(u"operacion_label")
        self.operacion_label.setGeometry(QRect(140, 350, 221, 21))
        self.operacion_label.setFont(font2)
        self.tiempo_label = QLabel(self.frame_2)
        self.tiempo_label.setObjectName(u"tiempo_label")
        self.tiempo_label.setGeometry(QRect(170, 390, 191, 21))
        self.tiempo_label.setFont(font2)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(780, 60, 381, 611))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.finalizados_tableWidget = QTableWidget(self.frame_3)
        if (self.finalizados_tableWidget.columnCount() < 5):
            self.finalizados_tableWidget.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.finalizados_tableWidget.setObjectName(u"finalizados_tableWidget")
        self.finalizados_tableWidget.setGeometry(QRect(10, 50, 361, 541))
        self.finalizados_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 20, 201, 21))
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 60, 381, 161))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 50, 191, 31))
        self.N_Procesos = QSpinBox(self.frame_4)
        self.N_Procesos.setObjectName(u"N_Procesos")
        self.N_Procesos.setGeometry(QRect(220, 60, 141, 22))
        self.N_Procesos.setWrapping(False)
        self.N_Procesos.setMaximum(1000000)
        self.Empezar_pushButton = QPushButton(self.frame_4)
        self.Empezar_pushButton.setObjectName(u"Empezar_pushButton")
        self.Empezar_pushButton.setGeometry(QRect(30, 120, 331, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simular el Procesamiento por Lotes", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Procesador por lotes</span></p></body></html>", None))
        ___qtablewidgetitem = self.captura_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem1 = self.captura_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.captura_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem3 = self.captura_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        self.iniciar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.lote_Actual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\"></span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">de</span></p></body></html>", None))
        self.lote_Total.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\"></span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Lote</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.ejecuccion_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem5 = self.ejecuccion_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.ejecuccion_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem7 = self.ejecuccion_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        ___qtablewidgetitem8 = self.ejecuccion_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Restante", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Proceso Actual:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Operacion:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tiempo Estimado: </span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">ID:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tiempo transcurrido: </span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tiempo restante: </span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tiempo total: </span></p></body></html>", None))
        self.Id_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.operacion_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tiempo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        ___qtablewidgetitem9 = self.finalizados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem10 = self.finalizados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.finalizados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem12 = self.finalizados_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem13 = self.finalizados_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Procesos Finalizados:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Numero de procesos:</span></p></body></html>", None))
        self.Empezar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Empezar", None))
    # retranslateUi

