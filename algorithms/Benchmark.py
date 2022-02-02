from concurrent.futures import thread
import time
import logging
import threading
from algorithms import camino_Dijkstra, FloydWarshall, simplex


def iterations(name, alg, G, **kwargs):
    logging.info(f"Hilo {name}: iniciado")
    count = 0
    tot_time = 0
    n_iters = 100
    while count < n_iters:
        start = time.perf_counter()
        alg(G, **kwargs)
        tot_time += time.perf_counter() - start
    
    logging.info(f"Hilo {name}: termino. Tiempo promedio: {tot_time/n_iters}")


def time_algorithms(G, s : int, t : int, num_runs = 100):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    t_d = threading.Thread(target=iterations, args=("dijkstra", camino_Dijkstra, G), kwargs={'inicio': s, 'destino' : t})
    t_floyd = threading.Thread(target=iterations, args=("floydW", FloydWarshall, G))
    t_simplex = threading.Thread(target=iterations, args=("simplex", simplex, G), kwargs={'s': s, 't': t, 'benchmark' : True})

    t_d.start()
    t_floyd.start()
    t_simplex.start()


    t_d.join()
    t_floyd.join()
    t_simplex.join()