from readFile import ReadFile
import os
 
directory = './dados'
reader = ReadFile()

def read_directory(root, directory):
  for new_root, new_dirs, new_files in os.walk(os.path.join(root, directory)):
      if len(new_files) > 0:
        for file in new_files:
          if file.endswith(".txt"):
            lines = reader.readFilesLines(os.path.join(new_root, file))
            #adicionar verificação para identificar quem enviou e quem recebeu
            #depois adicionar ao grafo
            print(lines)

read_directory(os.path.dirname("./dados"), directory)