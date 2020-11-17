file=open('style.css','w+')
#Definición de propiedades de los objetos de la GUI
QMainWindow={'name':'QMainWindow','background-color': 'white'}
QLabel={'name':'QLabel','font-size': '14px','color': '#A0184B'} 
label={'name':'QLabel#label','border':'2px solid rgb(0,0,255)'}  

objetos=[QMainWindow,QLabel,label] 

#Creación del archivo .css
for widget in objetos:
    file.write(widget['name']+'{\n' )
    for i in range(1,len(widget)):
        parametro=list(widget)[i] 
        file.write(parametro+':'+widget[parametro]+';\n')
    file.write('}\n')

file.close()