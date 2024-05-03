
#TODO: POO (Programacion Orientada a Objetos)
# 1- Definicion de clase
class Persona:
    pass

# 2- Atributos: Caracteristica de una clase, puede ser de cualquier tipo, numero, cadena, lista, etc.
#__init__ : Es un metodo especial en Python que se llama automaticamente cuando se crea una clase, es utilizado para inicializar los atributos de una clase con valores especificos.
#self : Se refiere al propio objeto y se utiliza para acceder a sus atributos y metodos dentro de la clase. Es una convencion usar self como el primer parametro
class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Metodo: Accion definida dentro de una clase que puede realizar alguna operacion especifica con los atributos del objeto.
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

#Objeto: Una instancia de una clase, Se crea utilizando la clase como plantilla y representa una entidad del mundo real. Cada objeto tiene sus propios atributos y puede ejecutar sus propios metodos.
#Crear objeto de la clase persona.
# persona1 = Persona("Tomas", 26)
# print("Atributos")
# print(persona1.nombre)
# print(persona1.edad)
# print("\n")
# print("Metodos")
# persona1.saludar()


#TODO: Crear una clase llamada "Libro" que represente un libro. La clase debe tener los siguientes atributos: titulo, autor, paginas, editorial, fecha_publicacion. Y un metodo llamado "informacion" que imprima todos los datos del libro. Crear dos objetos de la clase Libro

class Libro:
    def __init__(self,titulo,autor,paginas,editorial,fecha_publi):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.fecha_publi = fecha_publi
        
    def informacion(self):
        print(f"El titulo del libro es {self.titulo}")
        print(f"El libro lo escribio {self.autor}")
        print(f"El libro tiene {self.paginas} paginas")
        print(f"La editorial es {self.editorial}")
        print(f"Fecha de publicacion: {self.fecha_publi}")
        
libro1 = Libro("El señor de los anillos","Tomas",569, "Genios", 1987)
# print(libro1.autor)
# print(libro1.titulo)
# print(libro1.fecha_publi)

libro1.informacion()