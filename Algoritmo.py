class Algoritmo:
    # constructor del algoritmo
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

    # Ejecutar el algoritmo dado un origen, un destino y una lista de nodos.
    def run(self, origen, destino, nodos):
        self.nodos = nodos
        self.origen = origen
        self.destino = destino
        # se declara cual es la linea por la que avanza para el calculo de transbordos
        self.lineaactual = origen.linea
        # se incluye el origen a la lista abierta
        self.listaAbierta.append(origen)
        # el antecesor del origen es él mismo para marcar el fin de recorrido
        self.origen.antecesor = self.origen
        actual = None
        # se inicia el calculo del algoritmo
        # si la lista abierta queda vacia se termina con error
        while len(self.listaAbierta) != 0:
            # si se ha llegado al destino se sale del bucle
            if actual is destino:
                break
            # se seleciona el nodo de menor f(n) para ser el actual
            actual = self.nodo_menor_fn()

            self.lineaactual = actual.linea

            # se calcula la g(n) del nodo actual
            actual.g = actual.calcular_distancia(actual.g, actual.antecesor)
            # se añade el acual a la cerrada y se saca de la abierta
            self.listaCerrada.append(actual)
            self.listaAbierta.remove(actual)
            # Este bucle sirve para colocar los antecesores de los adyacentes del nodo actual.
            for i in actual.adyacentes:
                if i[0].antecesor is not None:
                    # cuando el adyacente ya tiene un antecesor se comprueba si el g del actual es mejor que el que tenia
                    if i[0].calcular_distancia(i[0].antecesor.g, i[0].antecesor) > i[0].calcular_distancia(actual.g,
                                                                                                           actual) and \
                            i[0].antecesor not in self.listaCerrada:
                        i[0].antecesor = actual
                        # si el adyacente no tenia antecesor se le asigna el actual
                else:
                    i[0].antecesor = actual
            # se añaden a la abierta los adyacentes no comprobados del actual
            for j in actual.adyacentes:
                if j[0] not in self.listaCerrada and j[0] not in self.listaAbierta:
                    self.listaAbierta.append(j[0])
        # si el bucle ha terminado sin resultado se informa y se termina
        if actual is not destino:
            print("No se ha encontrado destino")
            return
        # en caso contrario se devuelve el camino
        return self.recorrer_camino()

    # Busca el nodo de menor f(n) en la lista abierta y lo devuelve
    def nodo_menor_fn(self):
        resultado = self.listaAbierta[0]
        # se miran todos los de la vista abierta para sacar el de menor f
        for nodo in self.listaAbierta:
            # se calcula la distancia del actual y la del mejor hasta ahora.
            distancianodo = nodo.calcular_distancia(nodo.calcular_distancia(nodo.antecesor.g, nodo.antecesor),
                                                    self.destino)
            distanciares = resultado.calcular_distancia(
                resultado.calcular_distancia(resultado.antecesor.g, resultado.antecesor), self.destino)
            # si el nodo actual tiene mejor f se convierte en el mejor de momento
            if distancianodo < distanciares:
                resultado = nodo
        # se retorna el mejor de todos
        return resultado

    # Recorre el camino hacia atras desde el destino siguiendo los antecesores
    # ademas tambien ejecuta operaciones para la informacion en pantalla.
    def recorrer_camino(self):
        # se comienza en el destino
        recorrido = [self.destino]
        actual = self.destino
        # calculo de la linea final
        for linea in actual.linea:
            if linea in actual.antecesor.linea:
                self.lineaactual = linea
        # bucle que avanza hasta tener el recorrido
        while actual != self.origen:
            # calculo de los transbordos
            for linea in actual.linea:
                if linea in actual.antecesor.linea:
                    if linea != self.lineaactual:
                        self.lineaactual = linea
                        self.ntrans += 1
            # calculo de la distancia real del recorrido
            for nod in actual.adyacentes:
                if nod[0] == actual.antecesor:
                    self.dist += nod[1]

            if self.lineaactual == 2 or self.lineaactual == 1:
                actual.linea.reverse()

            # se pasa al antecesor del actual
            actual = actual.antecesor
            recorrido.append(actual)
        return recorrido
