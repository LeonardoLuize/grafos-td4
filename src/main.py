from readFile import ReadFile
import os
 
directory = './dados'
reader = ReadFile()
 
def create_graph_from_directory(directory):
  for root, dirs, files in os.walk(directory):
    for dir in dirs:
      for root2, dirs2, files2 in os.walk(os.path.join(root, dir)):
        for file in files2:
          if file.endswith(".txt"):
            lines = reader.readFilesLines(os.path.join(root, dir, file))
            print(lines)
          
create_graph_from_directory(directory)