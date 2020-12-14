import os
file=open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css','w+')
#Definición de propiedades de los objetos de la GUI
QMainWindow={'name':'QMainWindow','background-color': 'white'}
terminal={'name':'QPlainTextEdit#plainTextEdit_terminal','background-color': 'black','color':'white',
'font-family':'Consolas','font-size':'13px'} 
tree_widget={'name':'QTreeWidget','font-size':'13px'} 
list_widget={'name':'QListWidget','font-size':'13px'} 
menu={'name':'QMenuBar','font-family':'Georgia','font-size':'14px'} 
dock={'name':'QDockWidget','font-family':'Georgia','font-size':'13px'} 
label={'name':'QLabel','font-family':'Palatino','font-size':'14px'} 
button={'name':'QPushButton','font-weight':'bold','font-size':'14px'} 
tabs={'name':'QTabWidget','font-family':'Georgia','font-weight':'bold','font-size':'13px'}
radiobutton={'name':'QRadioButton','font-family':'Palatino','font-size':'14px'} 
lineedit={'name':'QLineEdit','font-size':'14px'}
combobox={'name':'QComboBox','font-size':'14px'}


objetos=[QMainWindow,terminal,label,button,tabs,radiobutton,lineedit,combobox,menu,dock,tree_widget] 

#Creación del archivo .css
for widget in objetos:
    file.write(widget['name']+'{\n' )
    for i in range(1,len(widget)):
        parametro=list(widget)[i] 
        file.write(parametro+':'+widget[parametro]+';\n')
    file.write('}\n')

file.close()