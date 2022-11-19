from typing import List
from grafo import Grafo
import random

class Network:
    graph: Grafo
    length: int

    def __init__(self, is_directed:bool):
        self.graph = Grafo(is_directed)

    def generate_scale_graph(self, max_edges: int, users_list: List[str], max_size: int = 0, random_graph_size: int = 0)-> Grafo:

        if random_graph_size == 0:
            random_graph_size = len(users_list) // 5
            print(random_graph_size)

        random_graph = self.generate_random_graph(self.graph, users_list, random_graph_size)

        for index in range(random_graph_size, len(users_list)):
            current_node = self.__format_user_name(users_list[index])
            random_graph.adiciona_vertice(current_node)
            steps = 0

            if max_size != 0 and index > max_size:
                break

            for vertex in random_graph.adjacency_list:                
                if steps >= max_edges:
                    break

                high_order = self.get_high_order(random_graph)
                probability = self.get_probability(high_order, len(random_graph.adjacency_list[vertex]))

                random_value = random.randint(0,high_order)

                if random_value <= ((probability/100) * high_order):
                    random_weight = random.randint(0,100)
                    random_graph.adiciona_aresta(current_node, vertex, random_weight)

                    if not self.graph.is_directed:
                        random_graph.adiciona_aresta(vertex, current_node, random_weight)

                    steps += 1

        self.graph = random_graph
        return self.graph

    def get_high_order(self, graph: Grafo):
        max_order = 0

        for vertex in graph.adjacency_list:
            current_order = len(graph.adjacency_list[vertex])
            if current_order > max_order:
                max_order = current_order

        return max_order


    def get_probability(self, high_probability: int, target: int):
        return (target * 100) / high_probability

    def generate_random_graph(self, random_graph: Grafo, users_list: List[str], size: int):
        for index in range(size):
            random_graph.adiciona_vertice(self.__format_user_name(users_list[index]))

        for vertex in random_graph.adjacency_list:
            for second_vertex in random_graph.adjacency_list:
                if random.randint(0,9) == 1:
                    random_graph.adiciona_aresta(vertex, second_vertex, random.randint(0,100))

        return random_graph

    def __format_user_name(self, user_name: str):
        return user_name.replace("\n", "")
