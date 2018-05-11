import numpy as np
import numpy as np
import struct
import itertools


def J(x):
	n = len(x)
	a = -0.2*np.sqrt(1.0/n * sum(np.power(x, 2)))
	b = 1.0/n * sum(np.cos([2*np.pi*xi for xi in x]))

	return round(-20*np.exp(a) - np.exp(b) + 20 + np.e, 10)


N = 30
tam_populacao = 30
n_filhos = 200
max_eval = 200000
tau_ = 1.0/np.sqrt(2*N)
tau = 1.0/np.sqrt(2*np.sqrt(N))

best = []
for k in range(100):
	P = []
	for i in range(tam_populacao):
		xi = np.random.random_sample(N) * 60 - 30
		si = np.random.random_sample(N) + 1
		pi = np.concatenate([xi,si])
		P.append(pi)
	ev = 0

	best.append(J(P[0]))
	found_best = False


	while ((ev < max_eval) or found_best) :

		# Recombinacao
		filhos = []
		for j in range(n_filhos):
			# Posicoes para trocar
			r_id = np.random.randint(0, 2, N)
			# Selecionando 2 pais
			pais_id = np.random.randint(0, N, 2)
			pais = np.array([P[pais_id[0]], P[pais_id[1]]])
			# Recombinacao discreta de x
			x_filho = pais[0, :N]*r_id + pais[1, :N]*(1 - r_id)
			# recombinacao intermediaria de sigma
			s_filho = (pais[0, N:] + pais[1, N:])/2
			f = np.concatenate([x_filho,s_filho])
			filhos.append(f)

		# Mutacao 
		for i, xi in enumerate(filhos):
			# Sigmas
			new_si = xi[N:]*np.exp(tau_*np.random.normal() + tau*np.random.normal())
			new_xi = xi[:N] + new_si*np.random.normal()
			filhos[i] = np.concatenate([new_xi, new_si])

		# Selecao de sobreviventes (ranking)
		all_p = P + filhos
		apt = [[xi, J(xi[:30])] for xi in all_p]
		ev += len(all_p)
		apt = sorted(apt, key=lambda x: x[1])

		P = [xi[0] for xi in apt[:tam_populacao]]


		# Checando o best
		if apt[-1][1] < best[-1]:
			best[-1] = apt[-1][1]

		if abs(best[-1]) < 10**(-5):
			found_best = True


	print(best[-1])

print(best)
mean = np.mean(best)
std = np.std(best)
print(mean, std)







