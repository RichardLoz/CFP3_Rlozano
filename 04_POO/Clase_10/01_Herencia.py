
#TODO: HERENCIA: Es un pilar de la POO que permite que una clase herede atributos y metodos de otra clase. En la harencia, una clase principal o Superclase puede definir ciertos comportamientos y caracteristicas  que son comunes en un grupo de clases relacionadas. La herencia promueve la reutilizacion de codigo y ayudar a crear una jerarquia de clases que refleja relaciones del mundo real.

class Mascota(): # Clase Padre  
        
    def comer(self):
        print("La mascota esta comiendo")
    
    def dormir(self):
        print("La mascota esta durmiendo")

class Perro(Mascota): #Clase Hija
    pass

class Gato(Mascota):
    pass

# terry = Perro()
# terry.comer()
# terry.dormir()

# betun = Gato()
# betun.dormir()
# betun.comer()

#TODO: EJEMPLO PRACTICO

class Vehiculo():
    def __init__(self,marca,modelo,color,motor,asientos, velocidad_max):
        self.marca= marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0   
    
    def acelerar(self,incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_max:
            self.velocidad_actual = self.velocidad_max
        print(f"La velocidad actual {self.velocidad_actual}")
        

#TODO: SUPER(): El metodo SUPER es una funcion incorporada en Python que se utiliza para llamar al metodo de la SuperClase. En lugar de tener que especificar todos los atributos nuevamente, lo reemplazamos con el uso de SUPER()

class Moto(Vehiculo):
    def __init__(self,marca,modelo,color,motor,asientos):
        super().__init__(marca,modelo,color,motor,asientos,velocidad_max=200)

class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,color,motor,asientos):
        super().__init__(marca,modelo,color,motor,asientos,velocidad_max=30)
        

# Objeto Moto:
moto1 = Moto("Honda","CBR","Rojo",1000,2)

moto1.acelerar(50)

#Objeto Bicicleta:
bici1 = Bicicleta("Venus","BMX","Azul",False,1)
bici1.acelerar(20)