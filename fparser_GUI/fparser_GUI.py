from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
import sys
import os

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ventana principal de la GUI 
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs) #Inicializar clases heredadas
        self.ui=Ui_MainWindow() #Inicializamos la ventanan de la GUI 
        self.ui.setupUi(self)
        
        #Set style 
        with open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css') as f:
            self.setStyleSheet(f.read())

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Definir aplicación 
    window = Mainwindow() #Crear el objeto ventana principal 
    window.show()
    sys.exit(app.exec_())