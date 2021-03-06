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
        #Set style 
        try:
            self.real_path=os.path.dirname(os.path.abspath(__file__))
            with open(self.real_path+'/GUI_style.css') as f:
                self.setStyleSheet(f.read())  
        except:
            self.real_path=os.path.dirname(sys.executable)
            with open(self.real_path+'/GUI_style.css') as f:
                self.setStyleSheet(f.read())  
        #Arrow
        icon = QtGui.QIcon()
        arrow=self.real_path+'/Arrow.jpg'
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.toolButton_arrow.setIcon(icon)

        #Properties 
        self.main_dir=''
        self.files=[] 
        self.files_order=[] 
        self.files_f=[] 
        self.filter=["Python (*.py)","Fortran files (*.f90)"]
        self.fcomments='before'
        self.terminal=True
        self.lib=''
        self.new_folder=''
        self.folder_path=''
        self.interface=''
        self.py_interface=''
        self.module_list=[] 
        self.window_fmodule=ffiles.Window_fmodule(self_fparser=self)
        self.window_options=ffiles.Window_options(self_fparser=self)
        self.terminal_text=ffiles.Terminal(self_fparser=self)
        self.makefile=make.Makefile(self_fparser=self)
        self.ui.actionOpen_Directory.setShortcut("Ctrl+O")
        self.ui.actionOpen_Files.setShortcut("Ctrl+F")
        self.ui.actionOptions.setShortcut("Ctrl+T")
        self.ui.actionClear.setShortcut("Ctrl+W")

        #Connect signals
        #Use .connect(lambda: function(args)) to send extra arguments through the function 
        self.ui.menuFile.triggered[QtWidgets.QAction].connect(self.action)
        self.ui.toolButton_arrow.clicked.connect(lambda: ffiles.select_ffiles(self))
        self.ui.pushButton_fparser.clicked.connect(lambda: ffiles.fortran_parser(self))
        # self.ui.combobox.signal.connect(lambda: make.function(self.ui,self.makefile))
        #self.ui.pushButton_makeOK.clicked.connect(lambda: make.selectOS(self.ui))
        self.ui.comboBox_makeFC.activated.connect(self.makefile.fcompiler)
        self.ui.pushButton_searchFC.clicked.connect(self.makefile.searchFC)
        self.ui.toolButton_lib.clicked.connect(self.makefile.searchLib)
        #self.ui.pushButton_makeOK.clicked.connect(self.makefile.properties)
        self.ui.pushButton_makeOK.clicked.connect(self.makefile.runmake)
        
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