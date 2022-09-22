import email
from readFile import ReadFile
from grafo import Grafo
import re
import os
 
directory = './dados'
reader = ReadFile()
grafo = Grafo()

def add_to_graph(lines):
  emailRegex = "[\w\-.]+@[\w\-]+\.\w+\.?\w*"
  receive_list = []
  send = ""

  for line in lines:
    line = line.replace("\n", "")

    if "From: " not in line and re.match(emailRegex, line):
      splited = line.split(",")

      for split in splited:
        if re.match(emailRegex, split):
          receive_list.append(re.search(emailRegex, split).group())

    if "From: " in line and re.match(emailRegex, line.replace("From: ", "")):
      send = re.search(emailRegex, line).group()

    if len(receive_list) > 0 and send != "":
      grafo.adiciona_vertice(send)

      for receive in receive_list:
        grafo.adiciona_vertice(receive)
        grafo.adiciona_aresta(send, receive, 1)

      break


def read_directory(root, directory):
  for new_root, new_dirs, new_files in os.walk(os.path.join(root, directory)):
      if len(new_files) > 0:
        for file in new_files:
          lines = reader.readFilesLines(os.path.join(new_root, file))
          add_to_graph(lines)

#read_directory(os.path.dirname("./dados"), directory)

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("F")
grafo.adiciona_vertice("G")
grafo.adiciona_vertice("H")
grafo.adiciona_vertice("I")
grafo.adiciona_vertice("S")
grafo.adiciona_vertice("K")
grafo.adiciona_aresta("S", "A", 1)
grafo.adiciona_aresta("S", "B", 1)
grafo.adiciona_aresta("A", "C", 1)
grafo.adiciona_aresta("A", "D", 1)
grafo.adiciona_aresta("B", "G", 1)
grafo.adiciona_aresta("B", "H", 1)
grafo.adiciona_aresta("C", "E", 1)
grafo.adiciona_aresta("C", "F", 1)
grafo.adiciona_aresta("E", "K", 1)
grafo.adiciona_aresta("G", "I", 1)

#grafo.imprime_lista_adjacencias()

print("\nVértices:", grafo.total_vertices())
print("Arestas:", grafo.total_arestas())
print("É euleriano?", "Sim" if grafo.grafo_e_euleriano() else "Não" )
print(grafo.percorre_largura("S", "K"))