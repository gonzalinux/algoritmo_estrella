class Algoritmo:

    def __init__(self, origen, destino, nodos):
        self.listaAbierta = [origen]
        self.listaCerrada = []
        self.pilaNodos = []
        self.recorridoFinal = []
        self.nodos = nodos
        self.origen = origen
        self.destino = destino

    def algoritmo_a_estrella(self):
        recorrido = self.recorrer_grafo()
        self.recorrer_camino_y_almacenar(recorrido)
        self.obtener_recorrido()
        return self.recorridoFinal

    def recorrer_grafo(self):
        actual = None
        hijosActual = []
        # self.listaAbierta.append(self.origen)
        while len(self.listaAbierta) is not 0:
            actual = self.nodo_menor_dist_total(self.listaAbierta)
            self.listaCerrada.append(actual)
            if actual.get_estacion().compare_to(self.destino.getEstacion()) is 0:
                break
            else:
                hijosActual = actual.get_hijos()
                for i in range(hijosActual.size()):
                    if not self.listaAbierta.__contains__(hijosActual.get(1)) and \
                            not self.listaCerrada.__contains__(hijosActual.get(i)):

                        self.calcular_fn(hijosActual.get(i), actual)
                        hijosActual.get(i).set_padre(actual)
                        self.listaAbierta.append(hijosActual.get(i))
                    elif self.listaAbierta.__contains__(hijosActual.get(i)):
                        if hijosActual.get(i).getGN() < actual.getGN():
                            self.calcular_fn(actual, hijosActual.get(i))
            self.listaAbierta.remove(actual)
        return actual

    @staticmethod
    def nodo_menor_dist_total(lista):

        if lista.size() > 1:
            resultado = lista[0]
            fnres = resultado.calcular_fn
            for i in range(lista.size()):

                if lista[i].calcular_fn() < resultado.getFN():
                    resultado = lista.get(i)
        return resultado

    def calcular_fn(self, hijo, padre):
        distancias = padre.getHijosDistancia()
        gn_to_padre = distancias.get(hijo)
        hijo.setGN(padre.getGN() + gn_to_padre)
        hijo.setHN(hijo.calcularHN(self.destino, hijo))
        hijo.setFN(hijo.getGN() + hijo.getHN())

    def recorrer_camino_y_almacenar(self, destiny):
        if destiny.getEstacion().compareTo(self.origen.getEstacion()) == 0:
            self.pilaNodos.append(destiny)


        else:
            self.pilaNodos.append(destiny)
            self.recorrer_camino_y_almacenar(destiny.getPadre())

    def obtener_recorrido(self):
        while not len(self.pilaNodos) is 0:
            self.recorridoFinal.append(self.pilaNodos.pop())
