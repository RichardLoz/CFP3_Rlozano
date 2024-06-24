
#TODO: POO
# 1. Abstracción: Proceso de ocultar los detalles complejos de un objeto del mundo exterior. Representar en codigo los objetos del mundo real.
# 2. Herencia: Mecanismo por el cual una clase padre hereda sus propiedades y metodos a una clase hija.
# 3. Encapsulamiento: Restricción del acceso directo a los datos de objeto y su manipulación a través de métodos. (get - set)
# 4. Polimorfismo: Capacidad de diferentes clases de ser tratadas cmo instancias de una misma clase mediante una interfaz comun.

# ========================================================

#TODO: POLIMORFISMO: Se refiere a la capacidad de los objetos de diferentes clases para ser tratados como objetos de una clase comun. Es decir, diferentes clases pueden definir métodos que se llaman igual, pero que tienen comportamientos diferentes. En Python el Polimorfismo se logra principalmente a través de la Herencia.

class Animal: 
    def hacer_sonido(self):
        return "Este metodo debe ser implementado por las clases hijas"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):  
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Animal):  
    def hacer_sonido(self):
        return "Muuu"
    
# Instanciar objetos de los diferentes animales
perro = Perro()
gato = Gato()
vaca = Vaca()

# print(perro.hacer_sonido()) # GUAU
# print(gato.hacer_sonido()) # MIAU
# print(vaca.hacer_sonido()) # MUUU

def imprimir_sonido(animal):
    print(animal.hacer_sonido())
    
# imprimir_sonido(perro)
# imprimir_sonido(gato)
# imprimir_sonido(vaca)


#TODO: EJERCICIOS FIGURAS GEOMETRICAS
# Apartir de una clase padre "Figura" definir un metodo "calcular_area" que debe ser implementado por todas las clases hijas (Rectangulo, Circulo, Triangulo). Cada subclase que implementa el metodo "calcular_area" debe devolver el resultado de la formula aplicada para cada caso.
# Formulas:
#   Rectangulo: B x A
#   Circulo: PI * (radio ** 2)
#   Triangulo: (B * A) / 2
import math
class Figura:
    def calcular_area(self):
        return "Este metodo debe ser implementado por las clases hijas"

class Rectangulo(Figura):
    def __init__(self, base, alto):
        self.base = base
        self.alto = alto
        
    def calcular_area(self):
        return self.base * self.alto

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio **2)
    
class Triangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
#Funcion para mostrar resultados
def imprimir_area(figura):
    print(f"El area de la figura es: {figura.calcular_area()}")
    
# Instanciar objetos de las figuras
rectangulo = Rectangulo(10, 20)
circulo = Circulo(10)
triangulo = Triangulo(10, 20)

figuras = [rectangulo, circulo, triangulo]

for figura in figuras:
    imprimir_area(figura)

# print(rectangulo.calcular_area()) # 200
# print(circulo.calcular_area()) # 314.1592653589793
# print(triangulo.calcular_area()) # 100.0