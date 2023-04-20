class Alien:
    def __init__(self, tablero):
        self.vida = 50
        self.tablero = tablero
        self.nodo_actual = None

    def colocar_en_tablero(self, i, j):
        self.nodo_actual = self.tablero.tablero[i][j]

    def mover(self, direccion, depredador):
        if direccion == "arriba" and self.nodo_actual.up is not None:
            self.nodo_actual = self.nodo_actual.up
        elif direccion == "abajo" and self.nodo_actual.down is not None:
            self.nodo_actual = self.nodo_actual.down
        elif direccion == "izquierda" and self.nodo_actual.prev is not None:
            self.nodo_actual = self.nodo_actual.prev
        elif direccion == "derecha" and self.nodo_actual.next is not None:
            self.nodo_actual = self.nodo_actual.next
        else:
            print("movimiento no valido, pierde turno")

        if self.nodo_actual.value == "+":
            self.vida += 10
            self.nodo_actual.value = None
        elif self.nodo_actual.value == "-":
            self.vida -= 10
            self.nodo_actual.value = None
        elif self.nodo_actual == depredador.nodo_actual:
            self.vida -= 25

    def atacar(self, depredador):
        if (self.nodo_actual.up is depredador.nodo_actual or
        self.nodo_actual.down is depredador.nodo_actual or
        self.nodo_actual.next is depredador.nodo_actual or
        self.nodo_actual.prev is depredador.nodo_actual):
            depredador.vida -= 10