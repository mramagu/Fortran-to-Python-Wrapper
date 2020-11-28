from PyQt5 import QtCore, QtGui, QtWidgets
import os
def open_files(ui):
    file_dialog=QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #Abrir un solo archivo 
    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Opción de abrir 
    file_dialog.setNameFilters(["Python (*.py)","Fortran files (*.f90)"]) #Filtro 

    if file_dialog.exec_():
        filename = file_dialog.selectedFiles()
        dir_name=filename[0].split('/')
        dir_name='/'.join(dir_name[0:len(dir_name)-1])  
        ui.treeWidget_ffiles.setHeaderLabel(dir_name)
        for f in filename:
            QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[f.split('/')[-1]])


def open_folder(ui):
    file_dialog=QtWidgets.QFileDialog()
    folder=file_dialog.getExistingDirectory()
    ct=0
    for dir_name, dirs, files in os.walk(folder):
        if ct==0:
            ui.treeWidget_ffiles.setHeaderLabel(dir_name)
            for f in files:
                QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[f.split('/')[-1]])
            ct=1
        else:
            new_dir=QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[dir_name.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(new_dir,[f.split('/')[-1]])

def clear(ui):
    ui.treeWidget_ffiles.setHeaderLabel('')
    ui.treeWidget_ffiles.clear()
