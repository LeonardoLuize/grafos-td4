from grafo import Grafo
import random

class Network:

    graph: Grafo
    length: int

    def __init__(self):
        self.graph = Grafo()

    def generate_scale_graph(self, size:int) -> Grafo:
        random_graph = self.generate_random_graph(self.graph, 100)


        return self.graph

    def generate_random_graph(self, random_graph:Grafo, size:int):
        for index in range(size):
            random_graph.adiciona_vertice(f"{index}")

        for vertex in random_graph.adjacency_list:
            for second_vertex in random_graph.adjacency_list:
                if random.randint(0,9) == 1:
                    random_graph.adiciona_aresta(vertex, second_vertex, 0)

        random_graph.imprime_lista_adjacencias()

        return random_graph