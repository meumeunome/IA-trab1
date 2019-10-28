from beam_search import beam_search
from simulated_annealing import annealing
from GRASP import grasp
from algoritmo_genetico import algoritmo_genetico
import aux_problema_mochila as mochila
from timeit import default_timer

hyper_param_beam_search = [10, 25, 50, 100]  # Numero de Melhores Elementos

hyper_param_annealing = [[500, 100, 50],  # Temperatura inicial
                         [0.95, 0.85, 0.7],  # Alfa
                         [350, 500]]  # Numero de Iterações

hyper_param_grasp = [[50, 100, 200, 350, 500],  # Numero de Iterações
                     [2, 5, 10, 15]]  # Numero de Melhores Elementos

hyper_param_genetic = [[10, 20, 30],  # Tamanho da População
                       [0.75, 0.85, 0.95],  # Taxa de Crossover
                       [0.10, 0.20, 0.30]]  # Taxa de Mutação

problemas = [
             ["P1", 19, [(1, 3), (4, 6), (5, 7)]],
             ["P3", 58, [(1, 3), (4, 6), (5, 7), (3, 4)]],
             ["P4", 58, [(1, 3), (4, 6), (5, 7), (3, 4), (8, 10), (4, 8), (3, 5), (6, 9)]],
             ["P6", 58, [(1, 3), (4, 6), (5, 7), (3, 4), (8, 10), (4, 8), (3, 5), (6, 9), (2, 1)]],
             ["P8", 120, [(1, 2), (2, 3), (4, 5), (5, 10), (14, 15), (15, 20), (24, 25), (29, 30), (50, 50)]],
             ["P9", 120, [(1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)]],
             ["P11", 120, [(24, 25), (29, 30), (50, 50)]],
             ["P14", 138,
              [(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (2, 3), (3, 5), (7, 10), (10, 15),
               (13, 20), (24, 25), (29, 30), (50, 50)]],
             ["P17", 13890000,
              [(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20),
               (24, 25), (29, 37)]],
             ["P20", 45678901,
              [(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (15, 20)]]
             ]


def treino_beam_search():
    with open('Treino/beam_search.csv', 'a+') as arq:
        arq.write('Instancia,Estado,Valor,Tamanho,Execucao,num_best,num_iter\n')
    for problema in problemas:
        # valores = []
        # tempos = []
        print(problema[0], "-----")
        for m in hyper_param_beam_search:
            print(m)
            pes_max = problema[1]
            val = mochila.get_val_from_vt(problema[2])
            pes = mochila.get_pes_from_vt(problema[2])
            estado_inicial = mochila.estado_inicial_aleatorio(pes, pes_max)

            tempo_inicio = default_timer()
            solucao = beam_search(m, estado_inicial, pes, val, pes_max)
            tempo_total = default_timer() - tempo_inicio

            mochila.save_estado(solucao, val, pes, 'Treino/beam_search.csv', tempo_total, problema[0], [m])

            # tempos.append(tempo_total)
            #
            # valor_solucao = mochila.valor_total(solucao, val)
            # valores.append(valor_solucao)

        # melhor_valor = max(valores)
        # valores_normalizados = []
        # for i, aux in enumerate(valores):
        #     valores_normalizados.append(aux / melhor_valor)
        # print(hyper_param_beam_search)
        # print(valores, valores_normalizados, tempos)


def treino_annealing():
    with open('Treino/annealing.csv', 'a+') as arq:
        arq.write('Instancia,Estado,Valor,Tamanho,Execucao,num_best,num_iter\n')
    for problema in problemas:
        pes_max = problema[1]
        val = mochila.get_val_from_vt(problema[2])
        pes = mochila.get_pes_from_vt(problema[2])
        print(problema[0], "-----")
        for t0 in hyper_param_annealing[0]:
            for alfa in hyper_param_annealing[1]:
                for num_iter in hyper_param_annealing[2]:
                    print([t0, alfa, num_iter])
                    estado_inicial = mochila.estado_inicial_aleatorio(pes, pes_max)

                    tempo_inicio = default_timer()
                    solucao = annealing(t0, alfa, num_iter, estado_inicial, pes, val, pes_max)
                    tempo_total = default_timer() - tempo_inicio

                    mochila.save_estado(solucao, val, pes, 'Treino/annealing.csv', tempo_total, problema[0],
                                        [t0, alfa, num_iter])


def treino_grasp():
    with open('Treino/grasp.csv', 'a+') as arq:
        arq.write('Instancia,Estado,Valor,Tamanho,Execucao,num_best,num_iter\n')
    for problema in problemas:
        pes_max = problema[1]
        val = mochila.get_val_from_vt(problema[2])
        pes = mochila.get_pes_from_vt(problema[2])
        print(problema[0], "-----")
        for num_iter in hyper_param_grasp[0]:
            for num_elem in hyper_param_grasp[1]:
                print([num_iter, num_elem])

                tempo_inicio = default_timer()
                solucao = grasp(num_iter, num_elem, pes, val, pes_max)
                tempo_total = default_timer() - tempo_inicio

                mochila.save_estado(solucao, val, pes, 'Treino/grasp.csv', tempo_total, problema[0],
                                    [num_iter, num_elem])


def treino_algoritmo_genetico():
    with open('Treino/genetico.csv', 'a+') as arq:
        arq.write('Instancia,Estado,Valor,Tamanho,Execucao,num_best,num_iter\n')
    for problema in problemas:
        pes_max = problema[1]
        val = mochila.get_val_from_vt(problema[2])
        pes = mochila.get_pes_from_vt(problema[2])
        print(problema[0], "-----")
        for tamanho in hyper_param_genetic[0]:
            for t_crossover in hyper_param_genetic[1]:
                for t_mutacao in hyper_param_genetic[2]:
                    print([tamanho, t_crossover, t_mutacao])

                    tempo_inicio = default_timer()
                    solucao = algoritmo_genetico(tamanho, t_crossover, t_mutacao, pes, val, pes_max)
                    tempo_total = default_timer() - tempo_inicio

                    mochila.save_estado(solucao, val, pes, 'Treino/genetico.csv', tempo_total, problema[0],
                                        [tamanho, t_crossover, t_mutacao])



# m = hyper_param_beam_search[0]
# pes_max = problemas[9][1]
# val = mochila.get_val_from_vt(problemas[9][2])
# pes = mochila.get_pes_from_vt(problemas[9][2])
# estado_inicial = mochila.estado_inicial_aleatorio(pes, pes_max)
# print(estado_inicial)
# tempo_inicio = default_timer()
# solucao = beam_search(m, estado_inicial, pes, val, pes_max)
# tempo_total = default_timer() - tempo_inicio
#
# print(solucao, tempo_total)
