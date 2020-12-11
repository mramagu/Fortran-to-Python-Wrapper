from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
import sys
import os
import fortran_files as ffiles
import makefile as make

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ventana principal de la GUI 
    def __init__(self, *args, **kwargs):
        #Configuration 
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs) #Inicializar clases heredadas
        self.ui=Ui_MainWindow() #Inicializamos la ventanan de la GUI 
        self.ui.setupUi(self)
        #Arrow
        icon = QtGui.QIcon()
        arrow=os.path.dirname(os.path.abspath(__file__))+'/Arrow.jpg'
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.toolButton_arrow.setIcon(icon)
        
        #Set style 
        with open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css') as f:
            self.setStyleSheet(f.read())

        #Properties 
        self.main_dir=''
        self.files=[] 
        self.filter=["Python (*.py)","Fortran files (*.f90)"]
        self.fcomments='before'
        self.terminal=True
        self.lib=''
        #Crear interface en nueva carpeta 
        self.interface=''
        self.window_fmodule=ffiles.Window_fmodule(self_fparser=self)
        self.window_options=ffiles.Window_options(self_fparser=self)
        self.terminal_text=ffiles.Terminal(self_fparser=self)
        self.makefile=make.Makefile(self_fparser=self)

        #Connect signals
        #Use .connect(lambda: function(args)) to send extra arguments through the function 
        self.ui.menuFile.triggered[QtWidgets.QAction].connect(self.action)
        self.ui.toolButton_arrow.clicked.connect(lambda: ffiles.select_ffiles(self))
        self.ui.pushButton_fparser.clicked.connect(lambda: ffiles.fortran_parser(self))
        # self.ui.combobox.signal.connect(lambda: make.function(self.ui,self.makefile))
        #self.ui.pushButton_makeOK.clicked.connect(lambda: make.selectOS(self.ui))
        self.ui.pushButton_searchFC.clicked.connect(self.makefile.searchFC())
        self.ui.pushButton_makeOK.clicked.connect(self.makefile.properties())
        #self.ui.pushButton_makeOK.clicked.connect(lambda: make.runmake(self.ui))

    def action(self,selected_action):
        if selected_action.text()=='Open Files':
            ffiles.open_files(self)
        elif selected_action.text()=='Open Folder':
            ffiles.open_folder(self)
        elif selected_action.text()=='Options':
            ffiles.select_options(self)
        elif selected_action.text()=='Clear':
            ffiles.clear(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Definir aplicación 
    window = Mainwindow() #Crear el objeto ventana principal 
    window.show()
    sys.exit(app.exec_())