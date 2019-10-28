import random


def get_val_from_vt(vt):
    val = []
    for aux in vt:
        val.append(aux[0])

    return val


def get_pes_from_vt(vt):
    pes = []
    for aux in vt:
        pes.append(aux[1])

    return pes


def check_negative(solution):
    for i in solution:
        if i < 0:
            return True
    return False


def valor_total(s, val):
    soma = 0
    for i in range(len(s)):
        soma += s[i] * val[i]
    return soma


def peso_total(s, pes):
    soma = 0
    for i in range(len(s)):
        soma += s[i] * pes[i]
    return soma


def mochila_excede(s, pes, pes_max):
    return peso_total(s, pes) > pes_max


def melhor_elemento_da_lista(vizinhos, val):
    melhor = []
    valor_melhor = 0
    for aux in vizinhos:
        valor_aux = valor_total(aux, val)
        if valor_aux > valor_melhor:
            valor_melhor = valor_aux
            melhor = aux

    return list(melhor)


def escolher_vizinho_aleatorio(s, pes, pes_max):
    while 1:
        s_aux = list(s)
        random_pos = random.randint(0, len(s) - 1)
        rd = random.randint(-1, 1)
        s_aux[random_pos] += rd
        if s_aux != s and not (mochila_excede(s_aux, pes, pes_max)) and not (check_negative(s_aux)):
            return s_aux


def vizinhos_mais_proximos(s, pes, pes_max):
    lista_vizinhos = []

    for aux in range(len(s)):
        vizinho = list(s)
        vizinho[aux] += 1
        if not mochila_excede(vizinho, pes, pes_max):
            lista_vizinhos.append(vizinho)

    return list(lista_vizinhos)


def expandir_estados(s, pes, pes_max):
    expansao = []

    for aux in s:
        expansao += vizinhos_mais_proximos(aux, pes, pes_max)

    return list(expansao)


def estado_inicial_aleatorio(pes, pes_max):
    # novo_pes_max = pes_max*0.5
    pes_min = pes_max * 0.2
    novo_pes_max = random.uniform(pes_min, pes_max)
    while 1:
        estado = [0] * len(pes)
        for i in range(len(pes)):
            estado[i] = random.randint(0, novo_pes_max // len(pes) // pes[i])
        if not mochila_excede(estado, pes, novo_pes_max):
            return estado


def save_estado(estado, val, pes, nome_arquivo, tempo_execucao, idx, hiper):
    str_estado = ''
    for item in estado:
        str_estado = str_estado + str(item) + ' '

    str_estado = idx + ',' + str_estado[:-1] + ',' + str(valor_total(estado, val)) + ',' + str(peso_total(estado, pes)) + ',' + str(tempo_execucao)

    for param in hiper[:-1]:
        str_estado = str_estado + ',' + str(param)

    str_estado = str_estado + ',' + str(hiper[-1]) + '\n'

    with open(nome_arquivo, 'a+') as arquivo:
        arquivo.write(str_estado)

# val_pesos = [3, 2, 2, 4]
# state = estado_inicial_aleatorio(val_pesos, 100)
# peso = peso_total(state, val_pesos)
# print(state, peso)
