
#TODO: MANEJO DE VARIABLES

nombre = input("Ingrese su nombre: ").lower()
edad = 19
sexo = True

saludo1 = "Hola! mucho gusto mi nombre es " + nombre
saludo2 = "Hola! mucho gusto mi nombre es %s " %nombre
saludo3 = "Hola! mucho gusto mi nombre es {}" .format(nombre)
saludo4 = f"Hola! mucho gusto mi nombre es {nombre}, tengo {edad} años y mi sexo es {sexo} "
print(f"El nombre ingresado es {nombre}")
print(saludo1)
print(saludo2)
print(saludo3)
print(saludo4)
