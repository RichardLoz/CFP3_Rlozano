
#TODO: POO (Programacion Orientada a Objetos) ==> Paradigma de programacion

#Definicion de clase:
class Auto():
    pass

#Atrinutos: Caracteristicas de una clase, puede ser de cualquier tipo: numero, cadena, lista,etc.
# __init__ : Es un metodo especial en Python que se llama automaticamente cuando se crea una clase, es utilizado para inicializar los atributos de una clase con valores especificos.
# self: Se refiere al propio objeto y se utiliza para acceder a sus atributos y metodos dentro de la clase. Es una convención usar self como el primer parametro.
class Auto():
    def __init__(self, marca, modelo, color,altura,asientos):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.altura = altura
        self.asientos = asientos

# Metodo: Accion definida dentro de una clase que puede realizar alguna operacion especifica con los atributos del objeto
    def moverse(self):
        print(f"El auto de marca {self.marca} acelera a 300km/h")

  
# Objeto: Una instancia de una clase, se crea utilizando la clase como plantilla y representa una entidad del mundo real. Cada objeto tiene sus propios atributos y puede ejecutar sus propios metodos.


auto_roberto = Auto("Ferrari","248", "Rojo", "2mts", 2)
auto_jesi = Auto("Kia", "Sportage","Amarillo", "2mts", 5)
auto_mila = Auto("fiat","Fitito", "Azul", "2.2mts", 5)
print("------Auto de Roberto-------")
print(auto_roberto.marca)
print(auto_roberto.modelo)
print(auto_roberto.color)
print(auto_roberto.altura)
print(auto_roberto.asientos)
auto_roberto.moverse()

print("------Auto de Jesica-------")
print(auto_jesi.marca)
print(auto_jesi.modelo)
print(auto_jesi.color)
print(auto_jesi.altura)
print(auto_jesi.asientos)
auto_jesi.moverse()

print("------Auto de Milagros-------")
print(auto_mila.marca)
print(auto_mila.modelo)
print(auto_mila.color)
print(auto_mila.altura)
print(auto_mila.asientos)
