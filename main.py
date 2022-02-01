from models import Graph
from algorithms import Dijkstra, camino_Dijkstra, FloydWarshall

def print_matrix(mat):
    for l in mat:
        print(l)

def menu():
    print("1. Imprimir el Grafo")
    print("2. Camino Dijkstra")
    print("3. Floyd-Warshall")
    print("4. Salir")

if __name__ == '__main__':
    nodes = [0,1,2,3,4]
    aristas =[(0,1,2,), (3,4,3), (2,3,5), (0,3,2), (1,0,2)]
    G = Graph(nodes, aristas)

    
    while True:
        menu()
        choice = input("elija una opcion: ")

        if choice == "1":
            print(G.nodos)
            print(G.aristas)
        elif choice == "2":
            print(camino_Dijkstra(G, 1, 4))
        elif choice == "3":
            print_matrix(FloydWarshall)
        elif choice == "4":
            break
    
