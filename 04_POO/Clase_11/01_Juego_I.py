
#TODO:Creacion de clase Personaje
class Personaje:
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print("Nombre: ", self.nombre)
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: " , self.defensa)
        print("Vida: ", self.vida)
        
    def subir_nivel(self,fuerza, inteligencia, defensa,vida):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.vida = self.vida + vida
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} esta muerto")
        
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
        #return f"El daño causado por {self.nombre} es de {self.fuerza - enemigo.defensa} al rival {enemigo.nombre}"
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} ha realizado {daño} puntos al rival {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es de {enemigo.vida}")
        else:
            enemigo.morir()
        

tomas = Personaje("Tomas", 70, 50, 45, 700)
print("Personaje Nivel 1")
tomas.atributos()
tomas.subir_nivel(20,15,15,200)
print("\n")
print("Personaje Nivel 2")
tomas.atributos()
print(tomas.esta_vivo())

#Crear enemigo
print("\n")
milagros = Personaje("Milagros",75,60,50,800)
milagros.atributos()

#Metodo atacar
print("\n")
print(tomas.atacar(milagros))
print(milagros.atributos())