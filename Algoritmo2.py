class Algoritmo2:

    def __init__(self):
        self.nodos = None
        self.origen = None
        self.destino = None
        self.listaAbierta = []
        self.listaCerrada = []
        self.pilaNodos = []
        self.recorridoFinal = []
        self.g = 0

    def run(self, origen, destino, nodos):
        self.nodos = nodos
        self.origen = origen
        self.destino = destino
        self.listaAbierta.append(origen)

        while len(self.listaAbierta) is not 0:
            actual = self.nodo_menor_fn()
            self.g=actual.calcular_fn(self.g,self.origen)
            if actual is destino:
                break


    def nodo_menor_fn(self):
        resultado = self.listaAbierta[0]

        for nodo in self.listaAbierta:
            if nodo[0].calcular_fn(self.g, self.destino) < resultado[0].calcular_fn(self.g, self.destino):
                resultado = nodo

        return resultado

    def recorrido(self,nodo):
