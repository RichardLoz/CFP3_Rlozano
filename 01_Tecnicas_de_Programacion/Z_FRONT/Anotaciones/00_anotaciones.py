
#TODO: ANOTACIONES STRING
# nombre = input("Ingrese su nombre: \n ")
# saludo1 = "Hola! mucho gusto " + nombre
# saludo2 = "Hola! mucho gusto %s"  %nombre
# saludo3 = "Hola! mucho gusto {}".format(nombre) 
# saludo4 = f"Hola! mucho gusto {nombre} "

# print(saludo1)
# print(saludo2)
# print(saludo3)
# print(saludo4)


#TODO: Redondeando numeros
#1- Clasico/
numero_decimal = 49.947545
print("Numero Decimal: %.3f" %numero_decimal)

#2- Usando format()
numnero_decimal2 = 124.5647567
print(float('{0:.4f}'.format(numnero_decimal2)))

#3- ROUND
numero_decimal3 = 13.56753432
print(round(numero_decimal3, 2))

#4- Usando format de forma directa
numero_decimal4 = 13.436346347211
print(format(numero_decimal4, '.4f'))

#https://www.udemy.com/course/python-para-el-mundo-real/learn/lecture/17947258#overview