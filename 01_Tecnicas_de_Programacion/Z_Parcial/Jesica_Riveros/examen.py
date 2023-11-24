#3-	
#Solicita al usuario que ingrese una palabra. 
#Verifica si la palabra es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# cadena= input("ingrese una palabra: ")
# inicio = 0
# fin = len(cadena) - 1
# while cadena[inicio] == cadena[fin]:
#         print("Es palíndromo")
#         break
# else:
#    print("No es palíndromo")






#5-	El Ministerio de Salud les pide que realicen un algoritmo que pueda clasificar temperaturas en tres categorías: "Baja", "Media" y "Alta".
#  Tu tarea es desarrollar un programa que solicite al usuario ingresar temperaturas y las clasifique según los siguientes criterios:

# Baja: Temperaturas menores o iguales a 10 grados Celsius.
# Media: Temperaturas mayores a 10 grados y menores o iguales a 25 grados Celsius.
# Alta: Temperaturas mayores a 25 grados Celsius.

# Además, se desea que el programa almacene las temperaturas en listas separadas para cada categoría.
# Al finalizar imprimir por pantalla las temperaturas correspondientes a cada categoría



temperaturas= int(input("ingrese la temperatura: ")) 
baja=[]
media=[]
alta=[]
for i in range(temperaturas):
      print(i)
      if i <=10:
            baja.append(i)
           
      if i >10 and  i <=25:
            media.append(i)
            
      if i >25:
            alta.append(i)
            
print(baja,media,alta)

