import numpy as np
from scipy.optimize import linprog
from typing import List, Any, Tuple
from models import Graph
from utils import print_matrix

def simplex(G : Graph, s : int, t : int, benchmark = False):
    adj_mat = G.matriz_adyacencia()
    adj_mat[adj_mat == np.inf] = 0
    c = [] # funcion obj
    non_zeros_index = np.nonzero(adj_mat)
    for i,j in zip(non_zeros_index[0], non_zeros_index[1]):
        c.append(adj_mat[i,j])

    
    A = [] # matriz de flujos
    
    for n in G.nodos:
        row = []
        for i,j in zip(non_zeros_index[0], non_zeros_index[1]):
            if n == i:
                row.append(1)
            elif n == j:
                row.append(-1)
            else:
                row.append(0)
        A.append(row)


    b = [] 
    for i in range(len(A)):
        if i == s:
            b.append(1)
        elif i == t:
            b.append(-1)
        else:
            b.append(0)
    if not benchmark:
        print(f"{c=}")
        print_matrix(A)
        print(f"{b=}")

    res = linprog(c, A_eq= A, b_eq=b, method='simplex')
    return res

    