class Algoritmo:

    def __init__(self):
        self.nodos = None
        self.origen = None
        self.destino = None
        self.listaAbierta = []
        self.listaCerrada = []
        self.pilaNodos = []
        self.recorridoFinal = []
        self.lineaactual = []
        self.dist = 0
        self.anterior = None
        self.ntrans = 0

    def run(self, origen, destino, nodos):
        self.nodos = nodos
        self.origen = origen
        self.destino = destino
        self.lineaactual = origen.linea

        self.listaAbierta.append(origen)
        self.origen.antecesor = self.origen
        actual = None

        while len(self.listaAbierta) != 0:
            if actual is destino:
                break

            actual = self.nodo_menor_fn()

            self.lineaactual = actual.linea

            actual.g = actual.calcular_distancia(actual.g, actual.antecesor)
            self.listaCerrada.append(actual)
            self.listaAbierta.remove(actual)
            for i in actual.adyacentes:
                if i[0].antecesor is not None:
                    if i[0].calcular_distancia(i[0].antecesor.g, i[0].antecesor) > i[0].calcular_distancia(actual.g,
                                                                                                           actual) and \
                            i[0].antecesor not in self.listaCerrada:
                        i[0].antecesor = actual
                else:
                    i[0].antecesor = actual
                for j in actual.adyacentes:
                    if j[0] not in self.listaCerrada and j[0] not in self.listaAbierta:
                        self.listaAbierta.append(j[0])

        if actual is not destino:
            print("No se ha encontrado destino")
            return
        return self.recorrer_camino()

    def nodo_menor_fn(self):
        resultado = self.listaAbierta[0]
        for nodo in self.listaAbierta:
            distancianodo = nodo.calcular_distancia(nodo.calcular_distancia(nodo.antecesor.g, nodo.antecesor),
                                                    self.destino)
            distanciares = resultado.calcular_distancia(
                resultado.calcular_distancia(resultado.antecesor.g, resultado.antecesor), self.destino)

            if distancianodo < distanciares:
                resultado = nodo

        return resultado

    def recorrer_camino(self):
        recorrido = [self.destino]
        actual = self.destino

        for linea in actual.linea:
            if linea in actual.antecesor.linea:
                self.lineaactual = linea

        while True:
            if actual == self.origen:
                break
            for linea in actual.linea:
                if linea in actual.antecesor.linea:
                    if linea != self.lineaactual:
                        self.lineaactual = linea
                        self.ntrans += 1

            for nod in actual.adyacentes:
                if nod[0] == actual.antecesor:
                    self.dist += nod[1]
            if self.lineaactual == 2 or self.lineaactual == 1:
                actual.linea.reverse()

            actual = actual.antecesor

            recorrido.append(actual)
        return recorrido
