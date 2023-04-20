from alien import Alien
from depredador import Depredador
from tablero import Tablero


class Juego:
    def __init__(self, n):
        self.tablero = Tablero(n)
        self.alien = Alien(self.tablero)
        self.depredador = Depredador(self.tablero)

    def turno_alien(self):
        print("turno del alien")
        accion = input("¿Qué quieres hacer? (mover/atacar): ")
        if accion == "mover":
            direccion = input("¿En qué dirección quieres moverte? (arriba/abajo/izquierda/derecha): ")
            self.alien.mover(direccion, self.depredador)
        elif accion == "atacar":
            self.alien.atacar(self.depredador)
        self.tablero.imprimir(self.alien, self.depredador)

    def turno_depredador(self):
        print("turno del depredador")
        self.depredador.mover(self.alien)
        self.tablero.imprimir(self.alien, self.depredador)
    def jugar(self):
        i = int(input("ingrese la fila en donde quiere poner el alien: "))
        j = int(input("ingrese la columna en donde quiere poner el alien: "))
        self.alien.colocar_en_tablero(i, j)
        self.depredador.colocar_en_tablero()
        self.tablero.imprimir(self.alien, self.depredador)

        while self.alien.vida > 0 and self.depredador.vida > 0:
            print(f"Vida del Alien: {self.alien.vida}")
            print(f"Vida del Depredador: {self.depredador.vida}")
            if (self.depredador.vida > 0):
                self.turno_depredador()

        if self.alien.vida <= 0:
            print("El depredador gano")
        elif self.depredador.vida <= 0:
            print("El alien gano")