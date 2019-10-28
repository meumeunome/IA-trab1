import aux_problema_mochila as mochila
import functools
import random
from deepest_descent import deepest_descent
from time import time


def selecionar_aleatoriamente(s):
    random_num = random.randint(0, len(s) - 1)
    return s[random_num]


def greedy_random_construct(m, pes, val, pes_max):
    inicio = time()
    sm = []
    s = [0] * len(pes)
    peso_max_construtor = pes_max / 2

    estados_iniciais = mochila.vizinhos_mais_proximos(s, pes, peso_max_construtor)
    estados_iniciais = sorted(estados_iniciais, key=functools.partial(mochila.valor_total, val=val), reverse=True)

    expansao = estados_iniciais[:m]

    while expansao and time() - inicio < 120:
        fila = sorted(expansao, key=functools.partial(mochila.valor_total, val=val), reverse=True)
        fila = fila[:m]
        sm = selecionar_aleatoriamente(fila)
        expansao = mochila.vizinhos_mais_proximos(sm, pes, peso_max_construtor)

    # print(sm)
    return sm


def grasp(num_iter, m, pes, val, pes_max):
    inicio = time()
    sm = [0] * len(pes)
    for i in range(num_iter):
        s = greedy_random_construct(m, pes, val, pes_max)
        s = deepest_descent(s, pes, val, pes_max)
        if mochila.valor_total(s, val) > mochila.valor_total(sm, val):
            sm = s
        if time() - inicio >= 120:
            break

    return sm


# ss = grasp(1000, 10, [3, 2, 2, 4], [4, 3, 3, 5], 25)
# valor = mochila.valor_total(ss, [4, 3, 3, 5])
# peso = mochila.peso_total(ss, [3, 2, 2, 4])
# print(ss, peso, valor)
