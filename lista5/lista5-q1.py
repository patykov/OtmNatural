import numpy as np
import struct
import itertools


def J(x):
	n = len(x)
	a = -0.2*np.sqrt(1.0/n * sum(np.power(x, 2)))
	b = 1.0/n * sum(np.cos([2*np.pi*xi for xi in x]))
	return -20*np.exp(a) - np.exp(b) + 20 + np.e


N = 30
tam_populacao = 100
max_eval = 200000
tau_ = 0.06/np.sqrt(2*N)
tau = 0.002/np.sqrt(2*np.sqrt(N))
q = 10

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
		# Mutacao
		filhos = np.ones([tam_populacao, N*2])
		for i, xi in enumerate(P):
			new_xi = xi[:N] + xi[N:]*np.random.normal(size=N)
			new_si = xi[N:]*np.exp(tau_*np.random.normal() + tau*np.random.normal(size=N))
			filhos[i] = np.concatenate([new_xi, new_si])

		# Selecao de sobreviventes (torneiro)
		concorrentes = np.concatenate([P, filhos])
		for p_count in range(tam_populacao):
			r_id = np.random.randint(0, len(concorrentes), q)
			x = [concorrentes[r_id_x] for r_id_x in r_id]
			in_p = [i for i in x if i in old_p ]
			j = [J(xi[:N]) for xi in x]

			ev += len(j)
			placar = np.zeros(q)
			for a in range(q-1):
				for b in range(a+1, q):
					if j[a] < j[b]:
						placar[a] += 1
						if j[a] < best[-1][1]:
							best[-1] = [x[a], j[a]]
					else:
						placar[b] += 1
						if j[b] < best[-1][1]:
							best[-1] = [x[b], j[b]]
			winner_id = np.argmax(placar)
			P[p_count] = concorrentes[winner_id]

		# Selecao de sobreviventes (ranking)
		# concorrentes = np.concatenate([P, filhos])
		# js = np.array([-J(f[:N]) for f in concorrentes])
		# ev += len(concorrentes)
		# max_indices = js.argsort()[-tam_populacao:][::-1]
		# P = [concorrentes[ind] for ind in max_indices]

		# if -js[max_indices[0]] < best[-1][1]:
		# 	best[-1][1] = -js[max_indices[0]]

		if abs(best[-1][1]) < 10**(-5):
			found_best = True

	print(iteracao, best[-1][1], ev)

best_j = [b[1] for b in best]
mean = np.mean(best_j)
std = np.std(best_j)
print(mean, std)