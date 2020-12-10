import os
import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from Window_fmodules import Ui_MainWindow as Ui_MainWindow_fmodules
from Options import Ui_MainWindow as Ui_MainWindow_options
try:
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])+'/fparser')
    import fparser
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])+'/fobjects')
    import fobjects
except:
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[0:-1])+'/fparser')
    import fparser
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[0:-1])+'/fobjects')
    import fobjects

def open_files(self):
    clear(self) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #Open files
    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen) #Open option
    fortran_filter=['Fortran files ('+self.filter[i]+')' for i in range(0,len(self.filter))] 
    file_dialog.setNameFilters(fortran_filter) #Filter

    if file_dialog.exec_():
        filename = file_dialog.selectedFiles()
        dir_name=filename[0].split('/')
        dir_name='/'.join(dir_name[0:len(dir_name)-1]) 
        self.main_dir=dir_name 
        self.ui.treeWidget_ffiles.setHeaderLabel(dir_name)
        for f in filename:
            QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[f.split('/')[-1]])


# def open_folder(self):
#     clear(self.ui) #Clean tree and list 
#     file_dialog=QtWidgets.QFileDialog()
#     folder=file_dialog.getExistingDirectory() #Open directory 
#     ct=0
#     dirs={} 
#     for dir_name, subdirs, files in os.walk(folder):
#         if ct==0: #Main directory 
#             self.main_dir=dir_name
#             self.ui.treeWidget_ffiles.setHeaderLabel(dir_name)
#             for d in subdirs:
#                 dirs[d]=QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[d.split('/')[-1]])
#             for f in files:
#                 QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[f.split('/')[-1]])
#             ct=1
#         else: #Subdirectories 
#             for d in subdirs:
#                 try:
#                     dirs[d]=QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[d.split('/')[-1]])
#                 except:
#                     dirs[d]=QtWidgets.QTreeWidgetItem(dirs[dir_name.split('\\')[-1]],[d.split('/')[-1]])
#             for f in files:
#                 try:
#                     QtWidgets.QTreeWidgetItem(dirs[dir_name.split('/')[-1]],[f.split('/')[-1]])
#                 except:
#                     QtWidgets.QTreeWidgetItem(dirs[dir_name.split('\\')[-1]],[f.split('/')[-1]])
def open_folder(self):
    clear(self) #Clean tree and list 
    file_dialog=QtWidgets.QFileDialog()
    folder=file_dialog.getExistingDirectory() #Open directory 
    ct=0
    dirs={} 
    for dir_name, subdirs, files in os.walk(folder):
        new_dir_name='/'.join(dir_name.split('\\'))
        if ct==0: #Main directory 
            self.main_dir=dir_name
            self.ui.treeWidget_ffiles.setHeaderLabel(dir_name)
            for d in subdirs:
                dirs[new_dir_name+'/'+d]=QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[d.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(self.ui.treeWidget_ffiles,[f.split('/')[-1]])
            ct=1
        else: #Subdirectories 
            for d in subdirs:
                dirs[new_dir_name+'/'+d]=QtWidgets.QTreeWidgetItem(dirs[new_dir_name],[d.split('/')[-1]])
            for f in files:
                QtWidgets.QTreeWidgetItem(dirs[new_dir_name],[f.split('/')[-1]])

def select_ffiles(self):
    #Recursive function to analyse the tree up down
    def search_child(item,text):
        text=text+'/'+item.text(0)
        children=item.childCount()
        if children==0 and text not in self.files:
            for i in self.filter:
                if text.endswith(i.split('*')[-1]):
                    self.files.append(text)
                    self.ui.listWidget_selffiles.addItem(text)
                    break
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
            for i in self.filter:
                if text.endswith(i.split('*')[-1]):
                    self.files.append(text)
                    self.ui.listWidget_selffiles.addItem(text)
                    break
        else:
            for i in range(0,children):
                search_child(item.child(i),text)

def select_options(self):
    self.window_options.show()

def clear(self):
    self.ui.treeWidget_ffiles.setHeaderLabel('')
    self.ui.treeWidget_ffiles.clear()
    self.ui.treeWidget_fsummary.clear()
    self.ui.treeWidget_fparserfiles.clear()
    self.ui.listWidget_selffiles.clear()
    self.window_fmodule.ui.listWidget_fmod.clear()
    self.window_fmodule.ui.listWidget_selfmod.clear()
    self.terminal_text.clear()
    self.main_dir=''
    self.files=[] 

def fortran_parser(self):
    self.terminal_text.add_line('Running fortran parser...')
    self.terminal_text.add_line('')
    files=[self.main_dir+'/'+self.files[i] for i in range(0,len(self.files))]
    self.lib=fparser.library_maker(files,comment_style=self.fcomments,terminal=self.terminal_text)
    if self.lib==None:
        pass
    else:
        modules=[mod.name for mod in self.lib.modules]
        self.window_fmodule.ui.listWidget_fmod.addItems(modules)
        self.window_fmodule.show()


class Window_fmodule(QtWidgets.QMainWindow, Ui_MainWindow_fmodules):
    def __init__(self,self_fparser):
        #Configuration 
        QtWidgets.QMainWindow.__init__(self) #Inheritance
        self.ui=Ui_MainWindow_fmodules() #Initiate GUI window 
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
        self.ui.buttonBox_accept.accepted.connect(self.accept_selection)
        self.ui.buttonBox_accept.rejected.connect(self.reject_selection)

    #Methods 
    def select_fmod(self):
        items=self.ui.listWidget_fmod.selectedItems()
        for item in items:
            self.ui.listWidget_selfmod.addItem(item.text())
            
    def accept_selection(self):       
        module_list=[] 
        module_tree={} 
        #Create modules tree 
        for i in range(0,self.ui.listWidget_selfmod.count()):
            item=self.ui.listWidget_selfmod.item(i)
            module=QtWidgets.QTreeWidgetItem(self.self_fparser.ui.treeWidget_fsummary,[item.text()])
            module_tree[item.text()+'_sub']=QtWidgets.QTreeWidgetItem(module,['Subroutines'])
            module_tree[item.text()+'_fun']=QtWidgets.QTreeWidgetItem(module,['Functions'])
            module_list.append(item.text())
        #Create fortran interface 
        self.self_fparser.interface=fparser.interface_writer(self.self_fparser.lib,module_list,terminal=self.self_fparser.terminal_text)
        #Search for subroutines and functions in each module 
        modules=self.self_fparser.lib.modules
        for module in modules:
            if module.name in module_list:
                for x in module.contents:
                    if isinstance(x, fobjects.Subroutine):
                        QtWidgets.QTreeWidgetItem(module_tree[module.name+'_sub'],[x.name])
                    else:
                        QtWidgets.QTreeWidgetItem(module_tree[module.name+'_fun'],[x.name])           
        self.close()
    
    def reject_selection(self):
        self.ui.listWidget_fmod.clear()
        self.ui.listWidget_selfmod.clear()
        self.close()

class Window_options(QtWidgets.QMainWindow, Ui_MainWindow_options):
    def __init__(self,self_fparser):
        #Configuration 
        QtWidgets.QMainWindow.__init__(self) #Inheritance
        self.ui=Ui_MainWindow_options() #Initiate GUI window 
        self.ui.setupUi(self)
        #Properties
        self.self_fparser=self_fparser 
        self.terminal=False
        self.comments=''
        self.filter=[] 
        self.parameters()
        #Signals
        self.ui.lineEdit_fformat.editingFinished.connect(self.select_filter)
        self.ui.radioButton_fcommentsBefore.toggled.connect(self.comments_position)
        self.ui.radioButton_fcommentsAfter.toggled.connect(self.comments_position)
        self.ui.radioButton_terminalYes.toggled.connect(self.show_terminal)
        self.ui.radioButton_terminalNo.toggled.connect(self.show_terminal)
        self.ui.buttonBox_accept.accepted.connect(self.accept_options)
        self.ui.buttonBox_accept.rejected.connect(self.reject_options)

    #Methods 
    def parameters(self): 
        #Fortran files format
        text=self.ui.lineEdit_fformat.text() 
        self.filter=text.split(',')
        for i in range(0,len(self.filter)):
            self.filter[i]=self.filter[i]
        self.self_fparser.filter=self.filter
        #Position of fortran comments 
        if self.ui.radioButton_fcommentsBefore.isChecked():
            self.comments='before'
        else:
            self.comments='after'
        self.self_fparser.fcomments=self.comments
        #Enable terminal
        if self.ui.radioButton_terminalNo.isChecked():
            self.terminal=False
        else:
            self.terminal=True
        self.self_fparser.terminal=self.terminal

    def select_filter(self):
        text=self.ui.lineEdit_fformat.text() 
        self.filter=text.split(',')
        for i in range(0,len(self.filter)):
            self.filter[i]=self.filter[i]

    def comments_position(self):
        if self.ui.radioButton_fcommentsBefore.isChecked():
            self.comments='before'
        else:
            self.comments='after'
    
    def show_terminal(self):
        if self.ui.radioButton_terminalYes.isChecked():
            self.terminal=True
        else:
            self.terminal=False

    def accept_options(self):
        self.self_fparser.filter=self.filter
        self.self_fparser.fcomments=self.comments
        self.self_fparser.terminal=self.terminal
        #Show changes in terminal 
        self.self_fparser.terminal_text.add_line('Selected options:')
        self.self_fparser.terminal_text.add_line('Fortran files format : '+', '.join(self.self_fparser.filter),number=2)
        self.self_fparser.terminal_text.add_line('Position of fortran comments : '+self.self_fparser.fcomments)
        self.self_fparser.terminal_text.add_line('Show terminal : '+str(self.self_fparser.terminal))
        self.self_fparser.terminal_text.add_line('')
        if self.terminal==True:
            self.self_fparser.ui.dockWidget_terminal.show()
        else:
            self.self_fparser.terminal_text.clear()
            self.self_fparser.ui.dockWidget_terminal.close()
        #Close options window 
        self.close()

    def reject_options(self):
        self.ui.lineEdit_fformat.setText(','.join(self.self_fparser.filter)) 
        if self.self_fparser.fcomments=='before':
            self.ui.radioButton_fcommentsBefore.setChecked(True)
        else:
            self.ui.radioButton_fcommentsAfter.setChecked(True)
        if self.self_fparser.terminal:
            self.ui.radioButton_terminalYes.setChecked(True)
        else:
            self.ui.radioButton_terminalNo.setChecked(True)
        self.close()

class Terminal():
    def __init__(self,self_fparser):
        self.self_fparser=self_fparser
        self.text=''
        self.highlighter=Highlighter(self.self_fparser.ui.plainTextEdit_terminal.document())
    def add_text(self,text):
        previous_text=self.self_fparser.ui.plainTextEdit_terminal.toPlainText()
        self.self_fparser.ui.plainTextEdit_terminal.setPlainText(previous_text+text)
    def add_line(self,text,**kwargs):
        n=' \n'
        if 'number' in kwargs:
            for _ in range(1,kwargs['number']):
                n=n+' \n'
        previous_text=self.self_fparser.ui.plainTextEdit_terminal.toPlainText()
        self.self_fparser.ui.plainTextEdit_terminal.setPlainText(previous_text+n+text)
    def clear(self):
        self.self_fparser.ui.plainTextEdit_terminal.clear()

class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.errorFormat = QtGui.QTextCharFormat()
        self.errorFormat.setForeground(QtCore.Qt.red)

    def highlightBlock(self, text):
        if text.startswith('Error:'):
            self.setFormat(0, len(text), self.errorFormat)
        
if __name__ == "__main__":
    # print(sys.path)
    p=subprocess.run(['python','--version'],stdout=subprocess.PIPE)
    print(p.stdout.decode('utf-8'))


    
