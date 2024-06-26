
#TODO: POO
# 1. Abstracción: Proceso de ocultar los detalles complejos de un objeto del mundo exterior. Representar en codigo los objetos del mundo real.
# 2. Herencia: Mecanismo por el cual una clase padre hereda sus propiedades y metodos a una clase hija.
# 3. Encapsulamiento: Restricción del acceso directo a los datos de objeto y su manipulación a través de métodos. (get - set)
# 4. Polimorfismo: Capacidad de diferentes clases de ser tratadas cmo instancias de una misma clase mediante una interfaz comun.

# ========================================================

#TODO: POLIMORFISMO: Se refiere a la capacidad de los objetos de diferentes clases para ser tratados como objetos de una clase comun. Es decir, diferentes clases pueden definir métodos que se llaman igual, pero que tienen comportamientos diferentes. En Python el Polimorfismo se logra principalmente a través de la Herencia.



class Animal:
    def hacer_sonido(self):
        return "Este metodo debe ser implentado por las clases hijas"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"
    
perro = Perro()
gato = Gato()
vaca = Vaca()

# print(perro.hacer_sonido())
# print(gato.hacer_sonido())
# print(vaca.hacer_sonido())
    
# def imprimir_sonido(animal):
#     print(animal.hacer_sonido())

# imprimir_sonido(perro)
# imprimir_sonido(gato)
# imprimir_sonido(vaca) 
  


#TODO: EJERCICIOS FIGURAS GEOMETRICAS
# Apartir de una clase padre "Figura" definir un metodo "calcular_area" que debe ser implementado por todas las clases hijas (Rectangulo, Circulo, Triangulo). Cada subclase que implementa el metodo "calcular_area" debe devolver el resultado de la formula aplicada para cada caso.
#TODO: FORMULAS 
#Rectangulo = B * A
#Circulo = PI * (radio ** 2)
#Triangulo = (B * A) / 2

import math
class Figura:
    def calcular_area(self):
        return "Este metodo debe ser implementado por las clases hijas"
    
class Rectangulo(Figura):
    def __init__(self,base,alto):
        self.base = base
        self.alto = alto
        
    def calcular_area(self):
        return self.base * self.alto

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
class Triangulo(Figura):
    def __init__(self,base,alto):
        self.base = base
        self.alto = alto
    
    def calcular_area(self):
        return (self.base * self.alto) / 2
    
def imprimir_area(figura):
    print(f"El area de la figura es: {figura.calcular_area()}")
    
rectangulo = Rectangulo(10,20)
circulo = Circulo(10)
triangulo = Triangulo(10,20)

figuras = [rectangulo, circulo, triangulo]

for figura in figuras:
    imprimir_area(figura)

# imprimir_area(rectangulo)
# imprimir_area(circulo)
# imprimir_area(triangulo)
# print(rectangulo.calcular_area())
# print(circulo.calcular_area())
# print(triangulo.calcular_area())

#TODO: Una empresa nos solicita un programa que les permita gestionar los empleados. 
# Tipos de empleados: Tiempo Completo, Medio Tiempo, Freelance
# Debemos poder calcular sus salarios y gestionar una lista de todos sus empleados

#1- Clases y Herencia
    # - Crear una clase base "Empleado" con los siguientes atributos y metodos:
    # ATRIBUTOS: nombre(privado) , id_empleado(privado)
    # Metodos: __init__ , calcular_salario, get y set, __str__

#2- Subclases:
    # - EmpleadoTiempoCompleto(Empleado)
        #- Atributo: salario_mensual(privado)
        #- Metodo: calcular_salario()
    # - EmpleadoMedioTiempo(Empleado)
        #- Atributo: salario_por_hora(privado), horas_trabajadas(privado)
        #- Metodo: calcular_salario()
    # - EmpleadoFreelance(Empleado)
        #- Atributo: tarifa_proyecto(privado)
        #- Metodo: calcular_salario()

#3- Gestion de Empleados
    # - class GestionEmpleados
        # - Atributo: lista_empleados
    # - Metodos:
        # - agregar_empleado()
        # - agregar_varios_empleados()
        # - eliminar_empleado_por_id()
        # - mostrar_empleados()
        #- calcular_salarios() : Calcular y devolver la suma de todos los salarios de todos los empleados de la lista
        # - __str__ : Una representación en cadena de la lista de nombres de empleados

