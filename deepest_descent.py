import aux_problema_mochila as mochila


def deepest_descent(s, pes, val, pes_max):
    s_melhor = list(s)
    while 1:
        vizinhos = mochila.vizinhos_mais_proximos(s_melhor, pes, pes_max)
        s_linha = mochila.melhor_elemento_da_lista(vizinhos, val)
        if mochila.valor_total(s_linha, val) > mochila.valor_total(s_melhor, val):
            s_melhor = s_linha
        else:
            break

    return s_melhor


# print(deepest_descent([1, 2, 2, 2], [3, 2, 2, 4], [4, 3, 3, 5], 25))
