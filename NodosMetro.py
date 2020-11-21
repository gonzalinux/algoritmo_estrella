import math


class NodosMetro:
    def __init__(self, estacion, x, y, linea):
        self.x = x
        self.y = y
        self.estacion = estacion
        self.adyacentes = []
        self.linea = linea
        self.antecesor = None
        self.g = 0

    # calcula una distancia desde este nodo hasta el especificado en el segundo argumento
    # ademas suma el primer argumento, si es 0 no suma nada.
    def calcular_distancia(self, g, destino):
        return g + self.calcular_hn(destino)

    def calcular_hn(self, destino):

        resultado = math.sqrt(abs(math.pow(self.x - destino.x, 2) + (math.pow(self.y - destino.y, 2))))
        for i in self.linea:
            if i in self.antecesor.linea:
                resultado *= 0.75
            if i not in destino.linea:
                resultado *= 1.15

        return resultado
