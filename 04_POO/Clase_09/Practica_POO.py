
#TODO: Crear una clase llamada "Libro" que represente un libro. La clase debe tener los siguientes atributos: titulo, autor, paginas, editorial, fecha_publicacion. Y un metodo llamado "informacion" que imprima todos los datos del libro. Crear 2 objetos de la clase Libro

#OPCION_1
class Libro:
    def __init__(self,titulo,autor,paginas,editorial,fecha_publi):
        self.titulo= titulo
        self.autor = autor
        self.paginas= paginas
        self.editorial= editorial
        self.fecha_publi= fecha_publi
        
    def informacion(self):
        print(f"El titulo del libro es {self.titulo}")
        print(f"El autor del libro es {self.autor}")
        print(f"El libro tiene {self.paginas} paginas")
        print(f"La editorial del libro es {self.editorial}")
        print(f"La fecha de publicacion del libro es {self.fecha_publi}")
        
libro1 = Libro("El Alquimista","Paulo Cohelo", 468, "Genios", 1988)
libro2 = Libro("Condorito","Richard", 56, "Condor", 1978)
     
# libro1.informacion()
# print("\n")
# libro2.informacion()


# OPCION_2
class Libro:
    def __init__(self,titulo,autor,paginas,editorial,fecha_publi):
        self.titulo= titulo
        self.autor = autor
        self.paginas= paginas
        self.editorial= editorial
        self.fecha_publi= fecha_publi
        
    def informacion(self):
        info_str = (
        f"El titulo del libro es {self.titulo}\n"
        f"El autor del libro es {self.autor}\n"
        f"El libro tiene {self.paginas} paginas\n"
        f"La editorial del libro es {self.editorial}\n"
        f"La fecha de publicacion del libro es {self.fecha_publi}"
        )
        
        #with: Es una forma segura de trabajar con recursos que necesitan ser cerrados despues de su uso.
        with open("informacion.txt", "a") as archivo: #a ==> append
            archivo.write(info_str)
            archivo.write("\n")
        
        print("Informacion guardada con exito.")
        
  
        
libro1 = Libro("Harry Potter","Jesica", 868, "Mili", 2008)
libro2 = Libro("Condorito","Richard", 56, "Condor", 1978)

libro1.informacion()
libro2.informacion()