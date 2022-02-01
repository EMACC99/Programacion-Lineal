import numpy as np
import math
from typing import Any, List, Tuple, Union
from dataclasses import dataclass

@dataclass
class Arista():
    nodos : Tuple[int, int]
    peso  : int

    @classmethod
    def from_list(cls, aristas : List[Tuple]) -> List['Arista']:
        parsed_aristas = []
        for a in aristas:
            u,v,w = a
            parsed_arista = cls((u,v), w)
            if parsed_arista not in parsed_aristas:
                parsed_aristas.append(parsed_arista)
        
        return parsed_aristas

    def __eq__(self, __o: 'Arista') -> bool:
        return sorted(self.nodos) == sorted(__o.nodos) and self.peso == __o.peso

    def __add__(self, __o : 'Arista'):
        return self.peso + __o.peso


class Graph():
    def __init__(self, nodos : List[Any], aristas : List[Tuple[Any, Any, int]], directed : bool = False) -> None:
        self.nodos = nodos
        self.aristas = Arista.from_list(aristas)
        self.directed = directed
    
    def get_peso_arista(self, u, v):
        for a in self.aristas:
            if u in a.nodos and v in a.nodos:
                return a.peso
        
    def get_vecinos(self, u):
        vecinos = []
        for a in self.aristas:
            if u in a.nodos:
                if u == a.nodos[0]:
                    vecinos.append(a.nodos[1])
                else:
                    vecinos.append(a.nodos[0])
        return vecinos

    def matriz_adyacencia(self) -> List[List[int]]:
        adj_mat = np.ones((len(self.nodos), len(self.nodos))) * np.inf
        
        if self.directed:
            for a in self.aristas:
                adj_mat[a.nodos[0]][a.nodos[1]] = a.peso
        
        else:
            for a in self.aristas:
                adj_mat[a.nodos[0]][a.nodos[1]] = a.peso
                adj_mat[a.nodos[1]][a.nodos[0]] = a.peso

        for i in range(len(adj_mat)):
            adj_mat[i][i] = 0
        
        return adj_mat
