from grafo import Grafo

class Network:

    graph: Grafo
    length: int

    def __init__(self, length: int):
        self.graph = Grafo()
        self.length = length

    def generate_scale_graph(self, size:int) -> Grafo:
        random_graph = self.genereta_random_graph(100)


        return self.graph

    def genereta_random_graph(self, size:int):
        random_graph = Grafo()

        return random_graph