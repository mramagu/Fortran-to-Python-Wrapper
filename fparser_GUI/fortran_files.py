from PyQt5 import QtCore, QtGui, QtWidgets
import os
def open_files(ui,self):
    clear(ui) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #Open files
    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Open option
    file_dialog.setNameFilters(["Python (*.py)","Fortran files (*.f90)"]) #Filter

    if file_dialog.exec_():
        filename = file_dialog.selectedFiles()
        dir_name=filename[0].split('/')
        dir_name='/'.join(dir_name[0:len(dir_name)-1]) 
        self.main_dir=dir_name 
        ui.treeWidget_ffiles.setHeaderLabel(dir_name)
        for f in filename:
            QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[f.split('/')[-1]])


def open_folder(ui,self):
    clear(ui) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    folder=file_dialog.getExistingDirectory() #Open directory 
    ct=0
    dirs={} 
    for dir_name, subdirs, files in os.walk(folder):
        if ct==0: #Main directory 
            self.main_dir=dir_name
            ui.treeWidget_ffiles.setHeaderLabel(dir_name)
            for d in subdirs:
                dirs[d]=QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[d.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(ui.treeWidget_ffiles,[f.split('/')[-1]])
            ct=1
        else: #Subdirectories 
            for d in subdirs:
                dirs[d]=QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[d.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[f.split('/')[-1]])

def select_ffiles(ui,self):
    #Recursive function to analyse the tree up down
    def search_child(item,text):
        text=text+'/'+item.text(0)
        children=item.childCount()
        if children==0 and text not in self.files:
            self.files.append(text)
            ui.listWidget_selffiles.addItem(text)
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
    items=ui.treeWidget_ffiles.selectedItems()
    for item in items:
        parent=item.parent()
        children=item.childCount()
        if parent==None:
            text=item.text(0)
        else:
            text=search_parent(item)
        if children==0 and text not in self.files:
            self.files.append(text)
            ui.listWidget_selffiles.addItem(text)
        else:
            for i in range(0,children):
                search_child(item.child(i),text)
        # if text.endswith('.py'):
        #     print(text)


def clear(ui):
    ui.treeWidget_ffiles.setHeaderLabel('')
    ui.treeWidget_ffiles.clear()
    ui.listWidget_selffiles.clear()

class Window_fmodule(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
