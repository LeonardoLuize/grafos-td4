from readFile import ReadFile
from grafo import Grafo
import re
import os
 
directory = './dados'
#reader = ReadFile()
grafo = Grafo()

""" def read_directory(root, directory):
  for new_root, new_dirs, new_files in os.walk(os.path.join(root, directory)):
      if len(new_files) > 0:
        for file in new_files:
          lines = reader.readFilesLines(os.path.join(new_root, file))
          add_to_graph(lines)

read_directory(os.path.dirname("./dados"), directory) """