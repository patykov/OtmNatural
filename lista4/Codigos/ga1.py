import numpy as np
import math
import struct
import itertools


fraction = 2.0/2**15

def J(x):
	return x**2 -0.3*math.cos(10*math.pi*x)

def fenotype(gen_array):
	gen_string = ''.join(str(i) for i in gen_array)
	mult = int(gen_string[1:], 2)
	number = mult*fraction
	if gen_array[0] == 0:
		return number
	else:
		return -1*number

def GA(tam_populacao = 30, max_geracoes = 10, pc = 0.4, pm = 0.05, L=16):
	num_pais = int(tam_populacao*0.7)
	num_filhos = num_pais

	P = [np.random.randint(0, 2, size=L) for i in range(tam_populacao)]
	all_P = P
	geracao = 0

	while(geracao < max_geracoes):
		geracao += 1

		# Selecao dos pais
		aptidao = [4-(J(fenotype(i))) for i in P]
		apt_sum = [sum(aptidao[:i+1])/sum(aptidao) for i in range(len(aptidao))]

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

		
		# Mutacao
		for f in filhos:
			if np.random.rand() < pm:
				posicao = np.random.randint(1,L)
				f[posicao] = 1 - f[posicao]


		# Selecao de sobreviventes
		newP = pais + filhos
		aptidao = [4-(J(fenotype(i))) for i in newP]
		apt_sum = [sum(aptidao[:i+1])/sum(aptidao) for i in range(len(aptidao))]

		newG = []
		g_indice = 0
		r = np.random.rand()*1.0/tam_populacao
		while (len(newG) < tam_populacao):
			if (r < apt_sum[g_indice]):
				newG.append(list(newP[g_indice]))
				r = r + (1.0/tam_populacao)
			else:
				g_indice+=1

		P = newG
		all_P += P

	# Melhor resultado
	aptidao = [[i, (4-(J(fenotype(i))))] for i in P]
	best = max(aptidao, key=lambda x:x[1])
	print(fenotype(best[0]), J(fenotype(best[0])))

	return all_P



	
