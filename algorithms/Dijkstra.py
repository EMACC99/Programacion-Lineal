import math
from models import Graph
from typing import List, Tuple

def get_min(dist, Q) -> int:
    min_index = Q[0]
    for ix in Q:
        if dist[ix] < dist[min_index]:
            min_index = ix
    
    return min_index


def Dijkstra(G : Graph, source : int) -> Tuple[List[int], List[int]]:
    Q = []
    dist = [0 for _ in range(len(G.nodos))]
    prev = [-1 for _ in range(len(G.nodos))]
    for v in G.nodos:
        dist[v] = math.inf
        Q.append(v)
    
    dist[source] = 0

    while len(Q) != 0:
        u = get_min(dist, Q)
        Q.remove(u)

        vecinos = [v for v in G.get_vecinos(u) if v in Q]

        for v in vecinos:
            new_cost = dist[u] + G.get_peso_arista(u,v)
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
    
    return dist, prev

def camino_Dijkstra(G, inicio, destino):
    dist, prev = Dijkstra(G, inicio)
    S = []
    u = destino
    if prev[u] != -1 or u == inicio:
        while u != -1:
            S.append(u)
            u = prev[u]
    return S