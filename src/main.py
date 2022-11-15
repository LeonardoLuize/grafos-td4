from readFile import ReadFile
from Network import Network

reader = ReadFile()
nw = Network()

users_list = reader.readFilesLines("./src/Users.txt")
graph = nw.generate_scale_graph(max_size=0, max_edges=1, users_list=['A', 'B', 'C', 'D', 'E', 'F'], is_directed=False)

print("total arestas:", graph.total_arestas())
print("total vertex:", graph.total_vertices())

graph.imprime_lista_adjacencias()

#print(graph.percorre_em_profundidade('A', [], []))

# from grafo import Grafo

# G = Grafo()
# G.adiciona_vertice("A")
# G.adiciona_vertice("B")
# G.adiciona_vertice("C")
# G.adiciona_vertice("D")
# G.adiciona_vertice("E")
# G.adiciona_vertice("F")

# G.adiciona_aresta("A", "B", 1)
# G.adiciona_aresta("B", "A", 1)
# G.adiciona_aresta("C", "B", 1)
# G.adiciona_aresta("D", "A", 1)

# G.imprime_lista_adjacencias()

print("numero de componentes: ", graph.numberComponents())