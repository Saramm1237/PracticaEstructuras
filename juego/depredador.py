import random
class Depredador:
    def __init__(self, tablero):
        self.vida = 50
        self.tablero = tablero
        self.nodo_actual = None

    def colocar_en_tablero(self):
        i, j = random.randint(0, self.tablero.n - 1), random.randint(0, self.tablero.n - 1)
        while self.tablero.tablero[i][j].value is not None:
            i, j = random.randint(0, self.tablero.n - 1), random.randint(0, self.tablero.n - 1)
        self.nodo_actual = self.tablero.tablero[i][j]

    def mover(self, alien):
        def generar_numero():
            return random.randint(0, 7)
        movimiento = generar_numero()
        if movimiento == 0 and self.nodo_actual.up is not None:
            self.nodo_actual = self.nodo_actual.up
        if movimiento == 1 and self.nodo_actual.up is not None and self.nodo_actual.up.next is not None :
            self.nodo_actual = self.nodo_actual.up.next
        if movimiento == 2 and self.nodo_actual.next is not None:
            self.nodo_actual = self.nodo_actual.next
        if movimiento == 3 and self.nodo_actual.next is not None and self.nodo_actual.down.next is not None:
            self.nodo_actual = self.nodo_actual.down.next
        if movimiento == 4 and self.nodo_actual.down is not None:
            self.nodo_actual = self.nodo_actual.down
        if movimiento == 5 and self.nodo_actual.next is not None and self.nodo_actual.down.prev is not None:
            self.nodo_actual = self.nodo_actual.down.prev
        if movimiento == 6 and self.nodo_actual.prev is not None:
            self.nodo_actual = self.nodo_actual.prev
        if movimiento == 7 and self.nodo_actual.up is not None and self.nodo_actual.up.prev is not None:
            self.nodo_actual = self.nodo_actual.up.prev

        if self.nodo_actual.value == "+":
            self.vida += 10
            self.nodo_actual.value = None
        elif self.nodo_actual.value == "-":
            self.vida -= 10
            self.nodo_actual.value = None
        elif self.nodo_actual == alien.nodo_actual:
            alien.vida -= 25