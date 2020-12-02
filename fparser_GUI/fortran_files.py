from PyQt5 import QtCore, QtGui, QtWidgets
from Window_fmodules import Ui_MainWindow
import os
def open_files(self):
    clear(self.ui) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #Open files
    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Open option
    file_dialog.setNameFilters(["Python (*.py)","Fortran files (*.f90)"]) #Filter

    if file_dialog.exec_():
        filename = file_dialog.selectedFiles()
        dir_name=filename[0].split('/')
        dir_name='/'.join(dir_name[0:len(dir_name)-1]) 
        self.main_dir=dir_name 
        self.ui.treeWidget_ffiles.setHeaderLabel(dir_name)
        for f in filename:
            QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[f.split('/')[-1]])


def open_folder(self):
    clear(self.ui) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    folder=file_dialog.getExistingDirectory() #Open directory 
    ct=0
    dirs={} 
    for dir_name, subdirs, files in os.walk(folder):
        if ct==0: #Main directory 
            self.main_dir=dir_name
            self.ui.treeWidget_ffiles.setHeaderLabel(dir_name)
            for d in subdirs:
                dirs[d]=QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[d.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[f.split('/')[-1]])
            ct=1
        else: #Subdirectories 
            for d in subdirs:
                try:
                    dirs[d]=QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[d.split('/')[-1]])
                except:
                    dirs[d]=QtWidgets.QTreeWidgetItem(dirs[dir_name.split('\\')[-1]],[d.split('/')[-1]])
            for f in files:
                try:
                    QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[f.split('/')[-1]])
                except:
                    QtWidgets.QTreeWidgetItem(dirs[dir_name.split('\\')[-1]],[f.split('/')[-1]])

def select_ffiles(self):
    #Recursive function to analyse the tree up down
    def search_child(item,text):
        text=text+'/'+item.text(0)
        children=item.childCount()
        if children==0 and text not in self.files:
            self.files.append(text)
            self.ui.listWidget_selffiles.addItem(text)
        else:
            for i in range(0,children):
                search_child(item.child(i),text)
    #Recursive function to analyse the tree down up
    def search_parent(item):
        parent=item.parent()
        if parent==None:
            return item.text(0)
        else:
            return search_parent(parent)+'/'+item.text(0)

    # Add selected items to the list 
    items=self.ui.treeWidget_ffiles.selectedItems()
    for item in items:
        parent=item.parent()
        children=item.childCount()
        if parent==None:
            text=item.text(0)
        else:
            text=search_parent(item)
        if children==0 and text not in self.files:
            self.files.append(text)
            self.ui.listWidget_selffiles.addItem(text)
        else:
            for i in range(0,children):
                search_child(item.child(i),text)
        # if text.endswith('.py'):
        #     print(text)


def clear(ui):
    ui.treeWidget_ffiles.setHeaderLabel('')
    ui.treeWidget_ffiles.clear()
    ui.listWidget_selffiles.clear()

def fortran_parser(self):
    self.window_fmodule.show()


class Window_fmodule(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,self_fparser):
        #Configuration 
        QtWidgets.QMainWindow.__init__(self) #Inheritance
        self.ui=Ui_MainWindow() #Initiate GUI window 
        self.ui.setupUi(self)
        #Arrow
        icon = QtGui.QIcon()
        arrow=os.path.dirname(os.path.abspath(__file__))+'/Arrow.jpg'
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(arrow), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.toolButton_arrow.setIcon(icon)
        #Properties
        self.self_fparser=self_fparser 
        #Signals 
        self.ui.toolButton_arrow.clicked.connect(self.select_fmod)

    def select_fmod(self):
        self.ui.listWidget_selfmod.addItem('mod1')
        QtWidgets.QTreeWidgetItem(self.self_fparser.ui.treeWidget_fsummary,['mod1'])
        
