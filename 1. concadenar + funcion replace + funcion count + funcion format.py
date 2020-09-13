variable = "teoria de python \n de de hola"
print(variable + variable)
#forma diferente de concadenar 1
variable = variable.replace("hola","hola mundo")
print (variable)
variable = variable.replace("de","de2",2)
print (variable)
print(variable.count("de"))
#forma diferente de concadenar 2
var1 = 'J2logo'
var2 = 'Hola'
print('{} {}, ¿cómo estás?'.format(var2, var1))
#forma diferente de concadenar 3
var1 = 'J2logo'
var2 = 'Hola'
print('{var2} {var1}, ¿cómo estás?'.format(var1=var1, var2=var2))
#forma diferente de concadenar 4
nombre = "Luis"
oficio = "Programador"
print('Mi nombre es {nombre}, y soy {oficio},'.format(nombre=nombre, oficio=oficio))
