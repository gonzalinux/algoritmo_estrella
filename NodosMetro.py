import math

__name__ = "NodosMetro"

#clase para construir nodos representando estaciones de metro
class NodosMetro:
    #los atributos que se guardan son:
    #las cordenadas x e y,
    #el nombre de la estacion,
    #una lista de sus nodos adyacentes
    #su antecesor, que en principio es ninguno hasta que se ejecute el algoritmo
    #su g a la cual le ocurre lo mismo
    #si es un transbordo o no.
    def __init__(self, estacion, x, y, linea):
        self.x = x
        self.y = y
        self.estacion = estacion
        self.adyacentes = []
        self.linea = linea
        self.antecesor = None
        self.g = 0
        self.transbordo = False

    # calcula una distancia desde este nodo hasta el especificado en el segundo argumento
    # ademas suma el primer argumento, si es 0 no suma nada.
    def calcular_distancia(self, g, destino):
        return g + self.calcular_hn(destino)

    # calcula la h(n) desde este nodo hasta el dado por destino
    # el calculo se hace por distancia directa en el mapa
    # ademas se modifica si hubiera que hacer transbordos
    def calcular_hn(self, destino):
        #se calcula la distancia real
        resultado = math.sqrt(abs(math.pow(self.x - destino.x, 2) + (math.pow(self.y - destino.y, 2))))
        #se comprueban los transbordos
        for i in self.linea:
            #si se mantiene la misma linea la h baja pues es mejor para el usuario
            if i in self.antecesor.antecesor.linea:
                resultado *= 0.7
            #si no cambia a la linea destino la h sube pues es menos optimo
            elif i not in destino.linea:
                resultado *= 1.5

        return resultado
