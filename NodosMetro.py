import math

import Algoritmo


class NodosMetro:
    def __init__(self, estacion, x, y, linea):
        self.x = x
        self.y = y
        self.estacion = estacion
        self.adyacentes = []
        self.linea = linea
        """ self.gn = 0
        self.hn = 0
        self.fn = 0"""

    def calcular_fn(self, g, destino):
        return g + self.calcular_hn(destino)

    def calcular_hn(self, destino):
        resultado = math.sqrt(
            math.pow(self.x, 2) - math.pow(destino.x, 2) + math.pow(self.y, 2) - math.pow(destino.y, 2))
        if isinstance(self.linea, list):
            if isinstance(destino.linea, list):
                if self.linea[0] in destino.linea or self.linea[1] in destino.linea:
                    resultado *= 1.5
            else:
                if destino.linea in self.linea:
                    resultado *= 1.5
        elif isinstance(destino.linea, list) and self.linea in destino.linea:
            resultado *= 1.5
        else:
            if destino.linea != self.linea:
                resultado *= 1.5
        return resultado
