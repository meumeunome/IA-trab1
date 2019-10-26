import aux_problema_mochila as mochila


def hill_climbing(pes, val, pes_max):
    sm = [0] * len(pes)

    while 1:
        vizinhos = mochila.vizinhos_mais_proximos(sm, pes, pes_max)
        if not vizinhos:
            break
        sm = mochila.melhor_elemento_da_lista(vizinhos, val)

    return sm
