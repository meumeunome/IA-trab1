import math
import random
import aux_problema_mochila as mochila
from time import time


def annealing(t, alfa, num_iter, s, pes, val, pes_max):
    inicio = time()
    sm = [0] * len(pes)

    while time() - inicio < 120:
        for i in range(1, num_iter):
            s2 = mochila.escolher_vizinho_aleatorio(s, pes, pes_max)
            if mochila.valor_total(s2, val) > mochila.valor_total(s, val):
                s = list(s2)
                if mochila.valor_total(s2, val) > mochila.valor_total(sm, val):
                    sm = list(s)
            else:
                prob = math.e ** (-(mochila.valor_total(s2, val) - mochila.valor_total(s, val)) / t)
                aceita = random.uniform(0, 1)
                if aceita < prob:
                    s = list(s2)

        t *= alfa
        if t <= 1:
            break
    return sm


# v_pesos = [3, 2, 2, 4]
# v_valores = [4, 3, 3, 5]
# ss = annealing(500, 0.95, 350, mochila.estado_inicial_aleatorio(v_pesos, 25), v_pesos, v_valores, 25)
# valor = mochila.valor_total(ss, v_valores)
# peso = mochila.peso_total(ss, v_pesos)
# print(ss, peso, valor)
