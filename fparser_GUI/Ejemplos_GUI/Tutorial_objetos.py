class Widget(): #Definición del objeto 
    def __init__(self): #Inicialización automática del objeto
        #Propiedades: cualidades asociadas al objeto
        self.size=[10,20]
        self.color='blue'
        self.background_color='white'
        self.position=[100,25] 

        #Almacenamos todas las propiedades
        self.properties={'size':self.size,'color':self.color,'background_color':self.background_color,'position':self.position} 

    #Métodos: funciones asociadas al objeto
    def resize(self,x,y):
        self.size=[x,y]
        self.properties['size']=self.size 

    def  update_position(self,x,y):
        self.position=[x,y] 
        self.properties['position']=self.position

    def move(self,delta_x,delta_y):
        self.position[0] =self.position[0] +delta_x
        self.position[1] =self.position[1] +delta_y
        self.properties['position']=self.position

class Label(Widget): #Definición del objeto Label, que, a su vez, es un Widget
    def __init__(self,text,color):
        super().__init__() #Inicializamos la clase 'padre' Widget para heredar sus propiedades y métodos
        #Propiedades 
        self.text=text  
        self.text_color=color

        #Añadimos las propiedades al diccionario 
        self.properties['text']=self.text
        self.properties['text_color']=self.text_color   

    #Métodos
    def change_color(self,new_color):
        self.color=new_color 
        self.properties['color']=self.color 
    
    def change_text_color(self,new_text_color):
        self.text_color=new_text_color
        self.properties['text_color']=self.text_color 

class Button(Widget): #Definición del objeto Label, que, a su vez, es un Widget
    def __init__(self,text):
        super().__init__() #Inicializamos la clase 'padre' Widget para heredar sus propiedades y métodos
        #Propiedades 
        self.text=text  
        self.clicked=False

        #Añadimos las propiedades al diccionario 
        self.properties['text']=self.text 
        self.properties['clicked']=self.clicked 

    #Métodos
    def change_color(self,new_color):
        self.color=new_color 
        self.properties['color']=self.color 
    
    def click(self):
        self.clicked=True
        self.properties['clicked']=self.clicked 

#%% Main program

#Creamos un objeto Label
texto1=Label('Texto1','black') #Define un objeto Label con un texto: Texto1, y un color de texto: black
texto2=Label('Texto2','red')
pulsador=Button('Pulsa aquí')

print('Texto1:',texto1.properties)
print('Texto2:',texto2.properties)
print('Pulsador',pulsador.properties)


#Cambiamos el color de 'texto1' y el color de texto de 'texto2' llamando a sus métodos
texto1.change_color('green')
texto2.change_text_color('yellow')
print('Color texto1:',texto1.color)
print('Color de texto texto2:',texto2.text_color)

#Movemos el pulsador llamando al método 'move' de la clase padre 'Widget'
pulsador.move(10,2)
print('Posición del pulsador:',pulsador.position)

#Antes de presionar el pulsador
print('click antes:',pulsador.clicked) 
#Se pulsa el pulsador
pulsador.click()
print('click después:',pulsador.clicked) 

