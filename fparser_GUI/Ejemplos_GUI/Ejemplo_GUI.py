from PyQt5 import QtCore, QtGui, QtWidgets
from Window_ui import Ui_MainWindow
import sys

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ventana principal de la GUI 
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs) #Inicializar clases heredadas 

        self.ui=Ui_MainWindow() #Inicializamos la ventanan de la GUI 
        self.ui.setupUi(self) #Renderizar GUI con el diseño de window_ui.py 

        #Definir propiedades
        self.result='Suma'
        self.x=0
        self.y=0

        #Aplicar estilo
        with open("style.css") as f:
            self.setStyleSheet(f.read()) 

        #Modificar objetos 
        self.ui.lineEdit_x.setValidator(QtGui.QDoubleValidator(-10**12.,10**12.,12))#min, max, N_decimales 
        self.ui.lineEdit_y.setValidator(QtGui.QDoubleValidator(-10**12.,10**12.,12))
       

        #Conectar señales con funciones 
        self.ui.comboBox.currentIndexChanged.connect(self.operacion)
        self.ui.lineEdit_x.editingFinished.connect(self.resultado)
        self.ui.lineEdit_y.editingFinished.connect(self.resultado)
        self.ui.pushButton.clicked.connect(self.update)

    def update(self):
        if self.result=='Suma':
            self.ui.label_resultado.setText(str(self.x+self.y))
        else:
            self.ui.label_resultado.setText(str(self.x-self.y))
        self.ui.label_resultado.adjustSize()

    def operacion(self,i):
        print('Selected index ',i,':',self.ui.comboBox.currentText())
        if i==0:
            self.result='Suma'
            self.ui.label.setText('x+y=')
        else:
            self.result='Resta'
            self.ui.label.setText('x-y=')
        self.ui.label.adjustSize()

    def resultado(self):
        self.x=float(self.ui.lineEdit_x.text())
        self.y=float(self.ui.lineEdit_y.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Definir aplicación 
    window = Mainwindow() #Crear el objeto ventana principal 
    window.show()
    sys.exit(app.exec_())
