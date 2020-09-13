#En esta funcion se trabaja todo internamente y se llama solo para ejecutarse
def sum():
    print ("Hola mundo, se sumara")
sum ()
#Funcion donde hay que pasar parametros
def sum2(a,b):
    print(a+b)
sum2(10,15)
#Funcion que utliliza datos de otra funcion
def sum3(c,j):
    return(c+j)
sum3(6,6)
def imprimir(number):
    print(number)
    
imprimir(sum3(6,6))#forma una de imprimir

number = sum3(6,6)#forma dos de imprimir
imprimir(number)
