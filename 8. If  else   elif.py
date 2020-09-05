op = int(input("Ingrese \n1 para ingresar al menú \nCualqier otra tecla para salir "))
if op == 1:
    op2 = int(input("Ingrese el numero del indice de lo que desea hacer \n1. sumar \n2. restar \n3. multiplicar"))
if op2 == 1:
    num1 = float(input("Ingrese numero uno a sumar"))
    num2 = float(input("Ingrese numero dos a sumar"))
    num3 = float(num1+num2)
    print(num3)
elif op2 == 2:
    num1 = float(input("Ingrese numero uno a restar"))
    num2 = float(input("Ingrese numero dos a restar"))
    num3 = float(num1-num2)
    print(num3)
elif op2 == 3:
    num1 = float(input("Ingrese numero uno a multiplicar"))
    num2 = float(input("Ingrese numero dos a multiplicar"))  
    num3 = float(num1*num2)
    print(num3)  
else:
    print("ha salido del programa")
    
    
