from readFile import ReadFile
from Network import Network

reader = ReadFile()
nw = Network()

users_list = reader.readFilesLines("./src/Users.txt")
graph = nw.generate_scale_graph(max_size=10000, max_edges=5, users_list=users_list)

print("total arestas:", graph.total_arestas())
print("total vertex:", graph.total_vertices())