import aux_problema_mochila as mochila
import functools
import random
import math
from time import time


def gerar_populacao_inicial(tam_populacao, pes, pes_max):
    populacao = []
    for i in range(tam_populacao):
        while 1:
            estado = mochila.estado_inicial_aleatorio(pes, pes_max)
            if estado not in populacao:
                populacao.append(estado)
                break

    return populacao


def selecionar_individuo_roleta(s, val):
    tam_populacao = len(s)
    valor_total_populacao = 0
    for aux in s:
        valor_total_populacao += mochila.valor_total(aux, val)

    probabilidades = [0] * tam_populacao
    for i in range(tam_populacao):
        individuo = s[i]
        probabilidades[i] = mochila.valor_total(individuo, val) / valor_total_populacao

    roleta = random.uniform(0, 1)
    aux = 0
    for i in range(tam_populacao):
        aux += probabilidades[i]
        if aux >= roleta:
            return s[i]


def crossover(taxa, s, val):
    total_cruzamentos = math.floor(len(s) * taxa / 2)
    populacao = list(s)

    for i in range(total_cruzamentos):
        indv_1 = selecionar_individuo_roleta(populacao, val)
        populacao.remove(indv_1)
        indv_2 = selecionar_individuo_roleta(populacao, val)
        populacao.remove(indv_2)

        ponto_cruzamento = random.randint(1, len(val) - 1)

        novo_1 = list(indv_1[:ponto_cruzamento] + indv_2[ponto_cruzamento:])
        novo_2 = list(indv_2[:ponto_cruzamento] + indv_1[ponto_cruzamento:])

        # print("point", ponto_cruzamento, indv_1, "+", indv_2, "->", novo_1, "and", novo_2)

        s.append(novo_1)
        s.append(novo_2)


def mutacao(taxa, s):
    for aux in s:
        roleta = random.uniform(0, 1)
        if roleta <= taxa:
            # old = list(aux)
            indice = random.randint(0, len(aux) - 1)
            if random.randint(0, 1) == 1 or aux[indice] == 0:
                aux[indice] += 1
            else:
                aux[indice] -= 1
            # print(old, "mutou para", aux)


def remove_inviaveis(s, pes, pes_max):
    for aux in s:
        if mochila.mochila_excede(aux, pes, pes_max):
            s.remove(aux)


def algoritmo_genetico(tam_populacao, taxa_crossover, taxa_mutacao, pes, val, pes_max):
    inicio = time()
    populacao = gerar_populacao_inicial(tam_populacao, pes, pes_max)
    populacao = sorted(populacao, key=functools.partial(mochila.valor_total, val=val), reverse=True)

    nova_populacao = list(populacao)
    while inicio - time() < 240:
        crossover(taxa_crossover, nova_populacao, val)
        mutacao(taxa_mutacao, nova_populacao)
        remove_inviaveis(nova_populacao, pes, pes_max)
        nova_populacao = sorted(nova_populacao, key=functools.partial(mochila.valor_total, val=val), reverse=True)
        nova_populacao = nova_populacao[:tam_populacao]
        if nova_populacao == populacao:
            break
        populacao = list(nova_populacao)

    return nova_populacao[0]

# v_pesos = [3, 2, 2, 4]
# v_valores = [4, 3, 3, 5]
# ss = algoritmo_genetico(30, 0.8, 0.2, v_pesos, v_valores, 25)
# valor = mochila.valor_total(ss, v_valores)
# peso = mochila.peso_total(ss, v_pesos)
# print(ss, peso, valor)


# val_pesos = [3, 2, 2, 4]
# # state = gerar_populacao_inicial(10, val_pesos, 25)
# # print(state)
#
# selecionado = [[0, 0, 5, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 2, 2, 1], [0, 2, 1, 2], [0, 0, 2, 0], [0, 2, 0, 0],
#                [2, 0, 2, 0], [0, 5, 0, 0], [1, 0, 1, 0]]
#
# crossover(0.7, selecionado, val_pesos)
#
# print(selecionado)
