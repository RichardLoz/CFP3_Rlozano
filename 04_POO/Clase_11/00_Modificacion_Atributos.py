
#TODO: 
class Alumno:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def informacion(self):
        return self.nombre
        
# #INICIALIZAR
alumno1 = Alumno("Mateo","Gonzalez",27)
# print(f"Objeto alumno1: {alumno1.nombre} {alumno1.apellido} {alumno1.edad}\n")
# alumno1.nombre = "Juan"
# alumno1.apellido = "Gonzales"
# alumno1.edad = 24
# print("Informacion de alumno1 luego de la modificacion")
# print(f"Objeto alumno1: {alumno1.nombre} {alumno1.apellido} {alumno1.edad}\n")

alumno2 = Alumno("Laura", "Fernandez", 22)
# print(f"Objeto alumno2: {alumno2.nombre} {alumno2.apellido} {alumno2.edad}\n")

#TODO: Si bien esto es posible, es decir modificar los valores de un objeto accediento a sus atributos, no es la manera mas recomendable, a medida que vayamos avanzando veremos que lo idel es hacerlo mediante metodos (PILAR: Encapsulamiento).

#ATRIBUTOS QUE SOLO APLICAN AL OBJETO alumno1
# alumno1.domicilio = "Humberto Primo 2256"
# print(alumno1.domicilio)

# alumno2.domicilio = "Cabildo 3000"
# print(alumno2.domicilio)

#TODO: Vamos a crear una calculadora usando el paradigma POO

class Calculadora:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2
    
operacion1 = Calculadora(5,3)
# print(f"El resultado de la suma es {operacion1.suma()}")
# print(f"El resultado de la resta es {operacion1.resta()}")
# print(f"El resultado de la multiplicacion es {operacion1.multiplicacion()}")
# print(f"El resultado de la division es {operacion1.division():.2f}")

#TODO: Crear una clase hija que herede de Calculadora (Superclase) sus atributos y metodos y agregarar en esta clase hija los metodos de: Potencia, raiz cuadrada, seno y coseno.

import math
class CalculadoraCientifica(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)
    
    def potencia(self):
        return self.num1 ** self.num2
    def raiz_cuadrada(self):
        return math.sqrt(self.num1)
    def seno(self):
        return math.sin(self.num1)
    def coseno(self):
        return math.cos(self.num1)

operacion2 = CalculadoraCientifica(5,3)
print(f"El resultado de la suma es {operacion2.suma()}")
print(f"El resultado de la resta es {operacion2.resta()}")
print(f"El resultado de la multiplicacion es {operacion2.multiplicacion()}")
print(f"El resultado de la division es {operacion2.division():.2f}")
print(f"El resultado de la potencia es {operacion2.potencia()}")
print(f"El resultado de la raiz cuadrada es {operacion2.raiz_cuadrada()}")
print(f"El resultado del seno es {operacion2.seno()}")
print(f"El resultado del coseno es {operacion2.coseno()}")
    
    
    



