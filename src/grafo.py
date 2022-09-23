from functools import total_ordering
import numpy as np
from collections import defaultdict

class Grafo:
  def __init__(self):
    self.adjacency_list = defaultdict(list) 
    self.ordem = 0
    self.tamanho = 0

  def adiciona_vertice(self, rotulo):
    isValid = True
    
    for adjacency in self.adjacency_list:
      if rotulo == adjacency:
        isValid = False
        break

    if not isValid: 
      return
      
    self.ordem += 1
    self.adjacency_list[rotulo]
    return self.adjacency_list

  def get_vertice(self, u):
      if u == 1:
        return "A"
      elif u == 2:
          return "B"
      elif u == 3:
          return "C"
      elif u == 4:
          return "D"
      elif u == 5:
          return "E"
      elif u == 6:
          return "F"

  def adiciona_aresta(self, u,  v,  peso):
    isDuplicated = False

    if len(self.adjacency_list) > 0 and len(self.adjacency_list[u]) > 0:
      index = 0
      for adjacency in self.adjacency_list[u]:
        if adjacency[0] == v:
            list_adjacency = list(self.adjacency_list[u][index])
            list_adjacency[1] += 1
            self.adjacency_list[u][index] = tuple(list_adjacency)
            isDuplicated = True

        index += 1

    if not isDuplicated:
      self.adjacency_list[u].append((v, peso)) 

    return self.adjacency_list    

  def tem_aresta(self, u, v):
    if len(self.adjacency_list[u]) == 0:
      return False
    
    if len(self.adjacency_list[u][v]) > 0:
      return True
    else:
      return False

  def total_vertices(self):
    return self.ordem

  def total_arestas(self):
    total_edges = 0

    for vertex in self.adjacency_list:
      for edge in vertex:
        total_edges += 1

    return total_edges

  def peso(self, u, v):
    peso = ""
    
    for aresta in self.adjacency_list[u]:
      if v in aresta:
        peso = aresta

    if peso == "": 
      #print(f"\n Sem aresta entre {u} e {v}") 
      return

    #print(f"Peso da aresta entre {u} e {v} = {peso[1]}")
    return peso[1]
    
  def grafo_e_euleriano(self):
    isEulerian = True

    for vertex in self.adjacency_list:
      if not self.grau(vertex) % 2:
        isEulerian = False

    return isEulerian

  def grau(self, u):
    return len(self.adjacency_list[u])


  def grau_entrada(self, vertice):
    lista = []
    for vertex in self.adjacency_list:
      for adj in self.adjacency_list[vertex]:
        if adj[0] == vertice:
          lista.append(vertex)

    return len(lista)

  def quantidade_grau_entrada(self):
    lista = []
    for vertex in self.adjacency_list:
      quant_vertice = self.grau_entrada(vertex)
      lista.append([quant_vertice, vertex])

    lista.sort(reverse=True)
    return print("20 maiores grau de entrada", lista[:20])


  def grau_saida(self, u):
    return len(self.adjacency_list[u])
    
  def get_quantidade_grau_saida(self):
    lista = []
    for vertex in self.adjacency_list:
      quant_vertice = self.grau_saida(vertex)
      lista.append([quant_vertice, vertex])

    lista.sort(reverse=True)
    return print("20 maiores grau de saida", lista[:20])


  def imprime_lista_adjacencias(self):
 
    for i in self.adjacency_list:
      print(f"\n{i}: ")

      j = 0
      while j < len(self.adjacency_list[i]):
        print(f"\b | {self.adjacency_list[i][j]} -> \n", end="")
        j += 1

  def warshall(self):

    matrizAlcancabilidade = np.zeros((self.ordem, self.ordem))
    for i in range(self.ordem):
        for j in range(self.ordem):
          if self.matrizAdjacencias[i][j] != np.inf:
            matrizAlcancabilidade[i][j] = 1

    print(f"M_0:\n {matrizAlcancabilidade}")

    for k in range(self.ordem):
      for i in range(self.ordem):
        for j in range(self.ordem):
          print(f"M[{i}, {j}] <-- M[{i}, {j}] or (M[{i}, {k}] and M[{k}, {j}])")
          matrizAlcancabilidade[i][j] = matrizAlcancabilidade[i][j] or (matrizAlcancabilidade[i][j] and matrizAlcancabilidade[i][j])
          #print(f"M[{i}, {j}] <-- M[{i}, {j}] or (M[{i}, {k}] and M[{k}, {j}])")
      print(f"M_{k+1}: \n {matrizAlcancabilidade} \n")


  def possuiCaminho (self, u, v):
    matrizAlcancabilidade = self.warshall()
    if matrizAlcancabilidade[u][v]:
      return True
    else:
      return False
  
  def get_adjacent(self, u):
    adjacencias = []
    i = 0
    
    if len(self.adjacency_list[u]) != 0:
      while i < len(self.adjacency_list[u]):
        adjacencias.append(self.adjacency_list[u][i][0])
        i += 1

    return adjacencias

  def vertices_a_x_arestas(self, x, u):
    vertexList = self.adjacency_list[u]
    vertexList = vertexList[:x]
    position = 1

    print(f"\nVértices a uma distância de {x} arestas de {u}: ")
    for vertex in vertexList:
      print(f"\t{position}. {vertex}")
      position += 1

    return vertexList

  def percorre_em_profundidade(self, u, visited, stack):
    currentVertex = u
    visited.append(u)
    isFinish = False

    while((len(visited) != self.ordem) and isFinish == False):
      count = 0
      
      if currentVertex not in stack:
        stack.append(currentVertex)

      if len(self.adjacency_list[currentVertex]) == 0:
        stack.pop()
        if len(stack) == 0: break
        currentVertex = stack[len(stack) - 1]
        continue

      for neighbour in self.adjacency_list[currentVertex]:
        if neighbour[0] in visited:
          if count == (len(self.adjacency_list[currentVertex]) - 1):
            stack.pop()
            if len(stack) == 0: 
              isFinish = True
              break

            currentVertex = stack[len(stack) - 1]
            break

        count += 1

        if neighbour[0] not in visited:
          visited.append(neighbour[0])
          currentVertex = neighbour[0]
          break

    return visited

  def x_alcanca_y_profundidade(self, x, y):
    visitedList = self.percorre_em_profundidade(x, [], [])

    if y not in visitedList:
      print(f"\n{x} não alcança {y} em profundidade")
      return
    else:
      print(f"\n{x} alcança {y} em profundidade")
      print("Caminho percorrido:")

    position = 1

    for visited in visitedList:
      print(f"\t|{position}: {visited}")
      position += 1
      if visited == y:
        break

  def Dijkstra(self, source_node, target_node):
    visited = []
    cost = [ [np.inf, 0] for i in range(self.ordem) ]
    caminho = []
    #cost[source_node][0] = 0
    current_node = source_node

    caminho.append(self.get_vertice(current_node))
    
    while len(visited) < self.ordem:
      adjacent_nodes = self.get_adjacent(current_node)
      for node in adjacent_nodes:
        if node in visited:
          continue
          
        peso = Grafo.peso(self, current_node, node)

        if peso < cost[current_node][0]:
          cost[current_node][0] = peso
          cost[current_node][1] = node

      caminho.append([self.get_vertice(cost[current_node][1]), cost[current_node][0]])
      
      if cost[current_node][1] == target_node:
        break

      visited.append(current_node)
      current_node = cost[current_node][1]
          
    return caminho