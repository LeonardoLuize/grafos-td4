from readFile import ReadFile
from Network import Network

reader = ReadFile()
nw = Network()

users_list = reader.readFilesLines("./src/Users.txt")
graph = nw.generate_scale_graph(max_size=8, max_edges=2, users_list=["A", "B", "C", "D", "E", "F", "G", "H"])

graph.imprime_lista_adjacencias()

""" 
Separar exercícios por comentário
"""

""" 01: Geração por escala livre, info dos dados """
print("\n-- info --")
print("total arestas:", graph.total_arestas())
print("total vertex:", graph.total_vertices())

""" 01: Criação da DAG """
dag_obj = graph.cria_dag()
print("\n-- DAG --")
print(f'DAG: { dag_obj["dag"] }')
print(f'Edges to remove: { dag_obj["remove"] }')

