from readFile import ReadFile
from Network import Network

reader = ReadFile()
nw = Network(True)

users_list = reader.readFilesLines("./src/Users.txt")
graph = nw.generate_scale_graph(max_size=1000, max_edges=5, users_list=users_list, random_graph_size=100)

while True:
    print("\n--- Menu ---")
    print("| 1. info do grafo")
    print("| 2. Criação Pajek")
    print("| 4. Quantidade de componentes")
    print("| 6. DAG")
    print("| 7. Histograma Graus")
    print("| 8. Histograma Caminhos")
    print("| 0. Sair")

    selected = int(input("\nSelecione uma opção: "))

    if selected == 0:
        break
    elif selected == 1:
        """ 01: Geração por escala livre, info dos dados """
        print("\n-- info --")
        graph.imprime_lista_adjacencias()
        print("total arestas:", graph.total_arestas())
        print("total vertex:", graph.total_vertices())
        
    elif selected == 2:
        """ 02: Pajek"""
        print("\n-- Criação Pajek --")
        print(graph.pajek())

    elif selected == 4:
        """ 04: Quantidade de componentes"""
        print("\n-- Num Componentes --")
        print("Numero de componentes: ", graph.numberComponents())

    elif selected == 6:
        """ 06: Criação da DAG """
        dag_obj = graph.cria_dag()
        print("\n-- DAG --")
        print(f'DAG: { dag_obj["dag"] }')
        print(f'Edges to remove: { dag_obj["remove"] }')

    elif selected == 7:
        """ 07: Histograma Graus """
        print("\n-- Histograma Graus --")
        dag_obj = graph.histogramaGraus()

    elif selected == 8:
        """ 08: Histograma Caminhos """
        print("\n-- Histograma Caminhos --")
        dag_obj = graph.histogramaCaminhos()
