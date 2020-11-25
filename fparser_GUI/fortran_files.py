from PyQt5 import QtCore, QtGui, QtWidgets
import os
def open_files(ui):
    file_dialog=QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #Abrir un solo archivo 
    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Opción de abrir 
    file_dialog.setNameFilters(["Python (*.py)","Fortran files (*.f90)"]) #Filtro 

    if file_dialog.exec_():
        filename = file_dialog.selectedFiles()
        data=''
        for i in range(0,len(filename)):
            data=data+filename[i]+'\n' 
            ui.listWidget_ffiles.addItem(filename[i])
        ui.plainTextEdit_ffiles.setPlainText(data)


def open_folder(ui):
    file_dialog=QtWidgets.QFileDialog()
    folder=file_dialog.getExistingDirectory()
    dir_string=''
    file_string=''
    for dir_name, dirs, files in os.walk(folder):
        dir_string=dir_string+dir_name+'\n '
        for f in files:
            file_string=file_string+f+'\n '  
    ui.plainTextEdit_dir.setPlainText(dir_string)  
    ui.plainTextEdit_ffiles.setPlainText(file_string) 
