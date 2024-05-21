
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
        

# jesica = Personaje("Jesica", 70, 50, 45, 700)
# print("Personaje Nivel 1")
# jesica.atributos()
# jesica.subir_nivel(20,15,15,200)
# print("\n")
# print("Personaje Nivel 2")
# jesica.atributos()
# # print(jesica.esta_vivo())

# # #Crear enemigo
# print("\n")
# roberto = Personaje("Roberto",75,60,50,800)
# roberto.atributos()

# # #Metodo atacar
# print("\n")
# print(jesica.atacar(roberto))
# print(roberto.atributos())
# roberto.atacar(jesica)
# print(jesica.atributos())

class Guerrero(Personaje):
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.espada = espada
        
    # Metodo que nos permite seleccionar un arma
    def cambiar_arma(self):
        tipo_arma = int(input("""
                              Seleccione el tipo de arma:
                              1- Doran - daño 12
                              2- Filo Infinito - daño 70
                              3- Sanguinaria - daño 80
                              4- Espadon - daño 100
                              """
                              ))
        #Logica al elegir el arma.
        if tipo_arma == 1:
            self.espada = 12
        elif tipo_arma == 2:
            self.espada = 70
        elif tipo_arma == 3:
            self.espada = 80
        elif tipo_arma == 4:
            self.espada = 100
        else:
            print("Opción no valida")
        
    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")
        
    #Sobreescribir el metodo daño, ya que incorporamos una accesorio al guerrero
    def daño(self,enemigo):
        return self.fuerza + self.espada - enemigo.defensa
        
        
# roberto = Guerrero("Roberto",100,80,60,600,2)
# roberto.atributos()
# roberto.cambiar_arma()
# jesica = Personaje("Jesica", 100, 89, 100,800)
# roberto.atacar(jesica)
#jesica.atacar(roberto)
# print("\n")
# jesica.atributos()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo
        
    def cambiar_hechizo(self):
        tipo_hechizo = int(input("""
                Seleccione el tipo de arma:
                1- Magia Negra - daño 25
                2- Baston Magico - daño 70
                3- Vara Encantada - daño 80
                4- Libro Oscuro - daño 100
                """
                ))
        if tipo_hechizo == 1:
            self.hechizo = 25
        elif tipo_hechizo == 2:
            self.hechizo = 70
        elif tipo_hechizo == 3:
            self.hechizo = 80
        elif tipo_hechizo == 4:
            self.hechizo = 100
        else:
            print("Elección incorrecta")
        
    #Sobreescribir el metodo atributos()
    def atributos(self):
        super().atributos()
        print(f"Hechizo: {self.hechizo}")
        
    #Sobreescribir el metodo daño()
    def daño(self,enemigo):
        return self.inteligencia + self.hechizo - enemigo.defensa
    
# milagros = Mago("Milagros",100,90,40,800,10)
# milagros.atributos()
# print("\n")
# milagros.cambiar_hechizo()
# milagros.atributos()


#TODO: Simular pelea.
#Jugadores:
tomas = Mago("Tomas",90,120,160,400,40)
milagros = Guerrero("Milagros", 95,120,150,450,40)
#nombre, fuerza, inteligencia, defensa, vida
def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n Turno: {turno}")
        print(f"Accion de {jugador_1.nombre}")
        jugador_1.atacar(jugador_2)
        print(f"Accion de {jugador_2.nombre}")
        jugador_2.atacar(jugador_1)
        turno += 1
        
    #Despues de salir del bucle, imprimo el ganador
    if jugador_1.esta_vivo():
        print(f"\n {jugador_1.nombre} ha ganado")
    elif jugador_2.esta_vivo():
        print(f"\n {jugador_2.nombre} ha ganado")
    else:
        print("\n Fue una dura pelea que termino en empate")
        
combate(tomas, milagros)
