from PyQt5 import QtCore, QtGui, QtWidgets
from Window_ui import Ui_MainWindow
import sys
import os

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
        self.ui.actionOpen.setShortcut("Ctrl+O")
       

        #Conectar señales con funciones 
        self.ui.comboBox.currentIndexChanged.connect(self.operacion)
        self.ui.lineEdit_x.editingFinished.connect(self.resultado)
        self.ui.lineEdit_y.editingFinished.connect(self.resultado)
        self.ui.pushButton.clicked.connect(self.update)
        self.ui.toolButton.clicked.connect(self.select_file)
        self.ui.lineEdit_select.editingFinished.connect(self.write_file)
        self.ui.menuFile.triggered[QtWidgets.QAction] .connect(self.open_folder)

    def update(self):
        if self.result=='Suma':
            self.ui.label_resultado.setText(str(self.x+self.y))
        else:
            self.ui.label_resultado.setText(str(self.x-self.y))
        self.ui.label_resultado.adjustSize()

    def select_file(self):
        file_dialog=QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile) #Abrir un solo archivo 
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Opción de abrir 
        file_dialog.setNameFilters(["Python files (*.py)","Fortran files (*.f90)"]) #Filtro 

        if file_dialog.exec_():
            filename = file_dialog.selectedFiles()
            self.ui.lineEdit_select.setText(filename[0])
            f = open(filename[0], 'r')
			
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)
            f.close()

    def write_file(self):
        try:
            f=open(self.ui.lineEdit_select.text())
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)
            f.close()
        except:
            pass

    def open_folder(self):
        file_dialog=QtWidgets.QFileDialog()
        folder=file_dialog.getExistingDirectory()
        dir_string=''
        file_string=''
        for dir_name, dirs, files in os.walk(folder):
            dir_string=dir_string+dir_name+'\n '
            for f in files:
                file_string=file_string+f+'\n '    
        self.ui.textEdit_2.setText(dir_string)  
        self.ui.textEdit_3.setText(file_string)           

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
