#Es casi como una clase pero como una clase mucha mas sencilla
#Un Ejemplo seria crear una estructura para controlar los colores de la app
from  enum import Enum

class Color(Enum):  #Se definen una serie de constantes
    RED = 1
    BLUE = 2
    BLACK = 3

print(Color.RED)
print(Color.RED.value)#para mostrar el dato

#------ Otra manera de hacerlo-----------
#Seria guardar el dato en una variable y luego mostrarla

f = Color.RED.value
print(f)


    
