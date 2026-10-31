import random


class Enemigos:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.dano= dano
        self.salud = salud

    def atacar(self):
        return random.randint(5,15)

    def recibir_dano(self, dano):
        self.salud-= dano
        if self.salud <=0:
            print(f"Haz eliminado a {self.nombre}")
            return True
        return False
        