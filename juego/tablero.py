import random

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    self.down = None
    self.up = None

class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = [[Node(None) for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n - 1):
                self.tablero[i][j].next = self.tablero[i][j + 1]
                self.tablero[i][j + 1].prev = self.tablero[i][j]

        for j in range(n):
            for i in range(n - 1):
                self.tablero[i][j].down = self.tablero[i + 1][j]
                self.tablero[i + 1][j].up = self.tablero[i][j]

        simbolos = ["+"] * n + ["-"] * n
        random.shuffle(simbolos)

        for simbolo in simbolos:
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            while self.tablero[i][j].value is not None:
                i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            self.tablero[i][j].value = simbolo

    def imprimir(self, alien=None, depredador=None):
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                if alien is not None and alien.nodo_actual == self.tablero[i][j]:
                    fila.append("👽")
                elif depredador is not None and depredador.nodo_actual == self.tablero[i][j]:
                    fila.append("🤖")
                elif self.tablero[i][j].value is None:
                    fila.append(" ")
                else:
                    fila.append(self.tablero[i][j].value)
            print("[" + "|".join(fila) + "]")
