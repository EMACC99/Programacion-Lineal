from typing import List
from models import Graph

def FloydWarshall(G : Graph) -> List[List[int]]:
    """
    Esto sirve para grafos dirigidos
    """
    n = len(G.nodos)
    adj_mat = G.matriz_adyacencia()

    dist = list(map(lambda p : list(map(lambda q: q, p)), adj_mat))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


def FloydWarshallSimple(G : Graph):
    pass