from random import randint
import time
from pynput import keyboard
from PySide2.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QApplication
from views.Ui_main import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.columnasTablas()
        self.interrupcion = False
        self.pausa = False
        self.continuar = True
        self.error = False
        self.boolEjecucion = False

        def pulsa(tecla):
            if tecla == keyboard.KeyCode.from_char('i') or tecla == keyboard.KeyCode.from_char('I'):
                if not self.pausa and self.boolEjecucion:
                    self.interrupcion = True
            elif tecla == keyboard.KeyCode.from_char('p') or tecla == keyboard.KeyCode.from_char('P'):
                if not self.pausa and self.boolEjecucion:
                    self.pausa = True
            elif tecla == keyboard.KeyCode.from_char('c') or tecla == keyboard.KeyCode.from_char('C'):
                if self.pausa and self.boolEjecucion:
                    self.continuar = False
            elif tecla == keyboard.KeyCode.from_char('e') or tecla == keyboard.KeyCode.from_char('E'):
                if not self.pausa and self.boolEjecucion:
                    self.error = True
                
        self.escuchador = keyboard.Listener(pulsa)
        self.escuchador.start()

        self.numeroProcesos = 0
        self.procesoActual = 1
        self.loteActual = 1
        self.totalLote = 0
        self.contadorProcesos = 0
        self.numeroEjecucion = 0
        self.tiempoTotal = 0
        self.listaRegistro = []
        self.listaEjecuccion = []
        self.listaTerminados = []

        self.ui.Empezar_pushButton.clicked.connect(self.empezar)
        self.ui.iniciar_pushButton.clicked.connect(self.iniciar)
    
    def llenarTablaRegistro(self):
        self.ui.captura_tableWidget.setRowCount(len(self.listaRegistro))

        for (index_row, row) in enumerate(self.listaRegistro):
            for(index_cell, cell) in enumerate(row):
                self.ui.captura_tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
    
    def llenarTablaEjecucion(self):
        self.ui.ejecuccion_tableWidget.setRowCount(len(self.listaEjecuccion))

        for (index_row, row) in enumerate(self.listaEjecuccion):
            for(index_cell, cell) in enumerate(row):
                self.ui.ejecuccion_tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))

    def llenarTablaTerminados(self):
        self.ui.finalizados_tableWidget.setRowCount(len(self.listaTerminados))

        for (index_row, row) in enumerate(self.listaTerminados):
            for(index_cell, cell) in enumerate(row):
                self.ui.finalizados_tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
    
    def columnasTablas(self):
        self.ui.captura_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.ejecuccion_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.finalizados_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    
    def buscarId(self, Id):
        for proceso in self.listaRegistro:
            if proceso[1] == Id:
                return False
        return True
    
    def ejecucion(self):
        self.boolEjecucion = True
        while len(self.listaEjecuccion) > 0:
            self.interrupcion = False
            self.error = False
            proceso = self.listaEjecuccion.pop(0)
            self.llenarTablaEjecucion()
            self.ui.Id_label.setText(str(proceso[1]))
            self.ui.operacion_label.setText(proceso[2])
            self.ui.tiempo_label.setText(str(proceso[3]))
            i = 0
            j = proceso[4]
            while i <= proceso[4]:
                self.ui.transcurrido_lcdNumber.display(i)
                self.ui.restante_lcdNumber.display(j)
                self.ui.total_lcdNumber.display(self.tiempoTotal)
                QApplication.processEvents()
                time.sleep(1)
                if self.pausa:
                    while self.continuar:
                        pass
                    self.pausa = False
                    self.continuar = True
                elif self.interrupcion:
                    proceso[4] = j
                    self.listaEjecuccion.append(proceso)
                    self.tiempoTotal += 1
                    break
                elif self.error:
                    proceso.insert(3, "Error")
                    proceso[4] = i
                    self.listaTerminados.append(proceso)
                    self.llenarTablaTerminados()
                    self.tiempoTotal += 1
                    break
                if self.numeroEjecucion == 0 or i != 0:
                    self.tiempoTotal += 1
                i += 1
                j -= 1
            if not self.interrupcion and not self.error:
                operacion = proceso[2].split()
                resultado = 0
                if operacion[1] == "+":
                    resultado = int(operacion[0]) + int(operacion[2])
                elif operacion[1] == "-":
                    resultado = int(operacion[0]) - int(operacion[2])
                elif operacion[1] == "*":
                    resultado = int(operacion[0]) * int(operacion[2])
                elif operacion[1] == "/":
                    resultado = int(operacion[0]) / int(operacion[2])
                else:
                    resultado = int(operacion[0]) % int(operacion[2])
                proceso.insert(3, resultado)
                self.listaTerminados.append(proceso)
                self.llenarTablaTerminados()
            self.numeroEjecucion += 1


    @Slot()
    def empezar(self):
        procesos = self.ui.N_Procesos.value()
        if procesos > 0:
            self.ui.Empezar_pushButton.setEnabled(False)
            self.numeroProcesos = procesos
            self.agregar()

    def agregar(self):
        for i in range(self.numeroProcesos):
            random = randint(1, 5)
            if random == 1:
                signo = "+"
            elif random == 2:
                signo = "-"
            elif random == 3:
                signo = "*"
            elif random == 4:
                signo = "/"
            else:
                signo = "%"
            n2 = randint(1, 100)
            n1 = randint(0, 100)
            operacion = str(n1) + ' ' + signo + ' ' + str(n2)
            tiempo = randint(6, 16)
            restante = tiempo
            Id = i
            if self.contadorProcesos < 5:
                self.contadorProcesos += 1
            else:
                self.loteActual += 1
                self.contadorProcesos = 1
            self.totalLote = self.loteActual
            self.listaRegistro.append([self.loteActual, Id, operacion, tiempo, restante])
            self.llenarTablaRegistro()
        self.ui.iniciar_pushButton.setEnabled(True)
    
    @Slot()
    def iniciar(self):
        self.ui.lote_Total.setText(str(self.totalLote))
        self.loteActual = 1
        self.ui.iniciar_pushButton.setEnabled(False)
        self.ui.N_Procesos.setEnabled(False)
        while self.loteActual <= self.totalLote:
            self.ui.lote_Actual.setText(str(self.loteActual))
            for procesos in reversed(self.listaRegistro):
                if procesos[0] == self.loteActual:
                    self.listaEjecuccion.insert(0, procesos)
                    self.listaRegistro.pop(self.listaRegistro.index(procesos))
            self.llenarTablaRegistro()
            self.llenarTablaEjecucion()
            self.ejecucion()
            self.loteActual += 1
        self.ui.Id_label.setText("")
        self.ui.operacion_label.setText("")
        self.ui.tiempo_label.setText("")
        self.ui.transcurrido_lcdNumber.display(0)
        self.ui.restante_lcdNumber.display(0)