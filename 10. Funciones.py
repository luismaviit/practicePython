#En esta funcion se trabaja todo internamente y se llama solo para ejecutarse
def sum():
    print ("Hola mundo, se sumara")
sum ()
#----------------------------------------------------------------------------
#Funcion donde hay que pasar parametros
def sum2(a,b):
    print(a+b)
sum2(10,15) #se pasa el parametro (valores de a y b)

#ejemplo 2
def sum3(c,j):
    return(c+j)
sum3(6,6)
#----------------------------------------------------------------------------
#Funcion que utliliza datos de otra funcion -- SE UTILIZA LA FUNCION SUM3

def imprimir(number):
    print(number)
    
imprimir(sum3(10,6))#forma una de imprimir utlizando la funcion imprimir y en su interior la funcion sum3

number = sum3(14,6)#forma dos de imprimir
imprimir(number)
