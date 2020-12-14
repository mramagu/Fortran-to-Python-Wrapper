import os
file=open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css','w+')
#Definición de propiedades de los objetos de la GUI
QMainWindow={'name':'QMainWindow','background-color': 'white'}
terminal={'name':'QPlainTextEdit#plainTextEdit_terminal','background-color': 'black','color':'white',
'font-family':'Consolas','font-size':'12px'} 
tree_widget={'name':'QTreeWidget'} 
label={'name':'QLabel','font-family':'Palatino','font-size':'13px'} 
button={'name':'QPushButton','font-weight':'bold'} 
tabs={'name':'QTabWidget','font-family':'Georgia','font-weight':'bold','font-size':'13px'} 


objetos=[QMainWindow,terminal,label,button,tabs] 

#Creación del archivo .css
for widget in objetos:
    file.write(widget['name']+'{\n' )
    for i in range(1,len(widget)):
        parametro=list(widget)[i] 
        file.write(parametro+':'+widget[parametro]+';\n')
    file.write('}\n')

file.close()