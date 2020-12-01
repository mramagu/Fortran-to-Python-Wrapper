from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
import sys
import os
import fortran_files as ffiles
import makefile as make

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ventana principal de la GUI 
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs) #Inicializar clases heredadas
        self.ui=Ui_MainWindow() #Inicializamos la ventanan de la GUI 
        self.ui.setupUi(self)
        
        #Set style 
        with open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css') as f:
            self.setStyleSheet(f.read())

        #Properties 
        self.main_dir=''
        self.files=[] 
        self.window_fmodule=ffiles.Window_fmodule()
        # self.makefile=make.Makefile()

        #Connect signals
        #Use .connect(lambda: function(args)) to send extra arguments through the function 
        self.ui.menuFile.triggered[QtWidgets.QAction].connect(self.action)
        self.ui.toolButton_arrow.clicked.connect(lambda: ffiles.select_ffiles(self))
        self.ui.pushButton_fparser.clicked.connect(lambda: ffiles.fortran_parser(self))
        # self.ui.combobox.signal.connect(lambda: make.function(self.ui,self.makefile))

    def action(self,selected_action):
        if selected_action.text()=='Open Files':
            ffiles.open_files(self)
        elif selected_action.text()=='Open Folder':
            ffiles.open_folder(self)
        elif selected_action.text()=='Clear':
            ffiles.clear(self.ui)
        print(self.main_dir)

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Definir aplicación 
    window = Mainwindow() #Crear el objeto ventana principal 
    window.show()
    sys.exit(app.exec_())