class Puerta:
    abierta = True
    material = "madera"
    alto = 200
    ancho = 10
    largo = 100
    #-------------------CREACION DE CONSTRUCTOR-------------------
    def __init__(self,abierta,material):#lo que se especifique en el constructor, siempre debera pasarse el valor, ya que su trabajo es inicializar los atributos 
        self.abierta = abierta
        self.material = material


    #-------------------------------------------------------------

    
    def volumen(self): #self es una referencia del objeto 
        return self.alto * self.ancho * self.largo
        #"pass" se utliza para definir un bloque de codigo como vacio 
        

puerta = Puerta(False,"acero") #se crea el objeto llamado puerta que toma forma de la clase Puerta
print(puerta.abierta) #se accede al valor del atributo descrito en la clase
puerta.material="acero"
print(puerta.material)
print(puerta.volumen())
