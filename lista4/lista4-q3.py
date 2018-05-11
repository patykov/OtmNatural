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
for iteracao in range(100):
	P = np.empty([tam_populacao, N*2])
	for i in range(tam_populacao):
		xi = np.random.random_sample(N) * 60 - 30
		si = np.random.random_sample(N) + 1
		pi = np.concatenate([xi,si])
		P[i] = pi
	ev = 0

	best.append([P[0], J(P[0,:N])])
	found_best = False

	while ((ev < max_eval) and not found_best):

		# Recombinacao
		filhos = np.empty([n_filhos, N*2])
		# Indice das posicoes para trocar
		pos_id = np.random.randint(0, 2, [n_filhos, N])
		# Indice dos pais
		p_id = np.random.randint(0, tam_populacao, [n_filhos,2])
		for j in range(n_filhos):
			# Selecionando 2 pais
			pais = np.array([P[p_id[j][0]], P[p_id[j][1]]])
			# Recombinacao discreta de x
			x_filho = pais[0, :N]*pos_id[j] + pais[1, :N]*(1 - pos_id[j])
			# recombinacao intermediaria de sigma
			s_filho = (pais[0, N:] + pais[1, N:])/2
			filhos[j] = np.concatenate([x_filho, s_filho])

		# Mutacao 
		for i, xi in enumerate(filhos):
			new_xi = xi[:N] + xi[N:]*np.random.normal(size=N)
			new_si = xi[N:]*np.exp(tau_*np.random.normal() + tau*np.random.normal(size=N))
			filhos[i] = np.concatenate([new_xi, new_si])


		# Selecao de sobreviventes (ranking)
		js = np.array([-J(f[:N]) for f in filhos])
		ev += len(filhos)
		max_indices = js.argsort()[-tam_populacao:][::-1]
		P = [filhos[ind] for ind in max_indices]

		if -js[max_indices[0]] < best[-1][1]:
			best[-1][1] = -js[max_indices[0]]

		if abs(best[-1][1]) < 10**(-5):
			found_best = True

	print(iteracao, best[-1][1], ev)

best_j = [b[1] for b in best]
mean = np.mean(best_j)
std = np.std(best_j)
print(mean, std)
