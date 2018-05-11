import numpy as np
import math
import struct
import itertools


def J(x):
	return sum(x)*1.0


def GA(tam_populacao, max_geracoes, pc, pm, L):
	num_filhos = tam_populacao
	results = [] #[geracao, best, mean, worst]

	P = [np.random.randint(0, 2, size=L) for i in range(tam_populacao)]
	geracao = 0

	while(geracao < max_geracoes):
		geracao += 1

		# Selecao dos pais (SUS)
		aptidao = [J(i) for i in P]
		apt_prob = [a*1.0/sum(aptidao) for a in aptidao]
		apt_sum = [sum(apt_prob[:i+1]) for i in range(len(apt_prob))]

		pais = []
		r = np.random.rand()*1.0/tam_populacao
		for p in range(tam_populacao):
			while (r <= apt_sum[p]):
				pais.append(list(P[p]))
				r = r + (1.0/tam_populacao)

		# Recombinacao
		filhos = []
		for i in range(1, tam_populacao, 2):
			if np.random.rand() < pc:
				posicao = np.random.randint(1,L)
				f1 = pais[i][:(L-posicao)]+pais[i-1][-posicao:]
				f2 = pais[i-1][:(L-posicao)]+pais[i][-posicao:]
			else:
				f1 = pais[i]
				f2 = pais[i-1]
			filhos.append(f1)
			filhos.append(f2)
		assert(len(filhos) == tam_populacao)

		
		# Mutacao (1bit flip)
		for f in filhos:
			if np.random.rand() < pm:
				posicao = np.random.randint(1,L)
				f[posicao] = 1 - f[posicao]


		# Selecao de sobreviventes (geracional)
		P = filhos

		# Resultados para a geracao
		aptidao = [J(i) for i in P]
		best = max(aptidao)
		worst = min(aptidao)
		mean = np.mean(aptidao)
		results.append([geracao, best, mean, worst])
		#results.append(worst)

		if best == 25:
			print("Otimo encontrado em {} geracoes!".format(geracao))
			return np.array(results)

	return np.array(results)



	