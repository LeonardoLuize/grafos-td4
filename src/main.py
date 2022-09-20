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
        grafo.adiciona_aresta(send, receive, 5)
        

      break


def read_directory(root, directory):
  for new_root, new_dirs, new_files in os.walk(os.path.join(root, directory)):
      if len(new_files) > 0:
        for file in new_files:
          lines = reader.readFilesLines(os.path.join(new_root, file))
          #adicionar verificação para identificar quem enviou e quem recebeu
          #depois adicionar ao grafo
          add_to_graph(lines)

read_directory(os.path.dirname("./dados"), directory)

grafo.imprime_lista_adjacencias()