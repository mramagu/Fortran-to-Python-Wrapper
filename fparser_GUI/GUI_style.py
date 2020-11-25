import os
file=open(os.path.dirname(os.path.abspath(__file__))+'/GUI_style.css','w+')
#Definición de propiedades de los objetos de la GUI
QMainWindow={'name':'QMainWindow','background-color': 'black'}

objetos=[QMainWindow] 

#Creación del archivo .css
for widget in objetos:
    file.write(widget['name']+'{\n' )
    for i in range(1,len(widget)):
        parametro=list(widget)[i] 
        file.write(parametro+':'+widget[parametro]+';\n')
    file.write('}\n')

file.close()