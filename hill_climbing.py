import aux_problema_mochila as mochila
from time import time


def hill_climbing(pes, val, pes_max):
    inicio = time()
    sm = [0] * len(pes)

    while 1 and time() - inicio < 120:
        vizinhos = mochila.vizinhos_mais_proximos(sm, pes, pes_max)
        if not vizinhos:
            break
        sm = mochila.melhor_elemento_da_lista(vizinhos, val)

    return sm
