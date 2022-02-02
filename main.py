import time
from models import Graph
from algorithms import Dijkstra, camino_Dijkstra, FloydWarshall, simplex, time_algorithms
from utils import print_matrix

def menu():
    print("1. Imprimir el Grafo")
    print("2. Camino Dijkstra")
    print("3. Floyd-Warshall")
    print("4. Simplex")
    print("5. Comparacion de tiempo")
    print("6. Salir")

if __name__ == '__main__':
    nodes = [0,1,2,3,4]
    aristas =[(0,1,100,), (0,2,30), (1,2,20), (2,3,10), (2,4,60), (3, 1, 15), (3,4,50)]
    G = Graph(nodes, aristas, directed=True)

    while True:
        menu()
        choice = input("elija una opcion: ")

        if choice == "1":
            print(G.nodos)
            print(G.aristas)
        elif choice == "2":
            print(camino_Dijkstra(G, 0, 1))
        elif choice == "3":
            print_matrix(FloydWarshall(G))
        elif choice == "4":
            print(simplex(G, 0, 1))
        elif choice == "5":
            s, t = tuple(map(int, input("Nodo de inicio y nodo objetivo: ").split()))
            print(time_algorithms(G, s, t))
        elif choice == "6":
            break
    
