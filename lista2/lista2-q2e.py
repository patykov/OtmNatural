import matplotlib.pyplot as plt
import numpy as np
import math


T = [0.1000, 0.0631, 0.0500, 0.0431, 0.0387, 0.0356, 0.0333, 0.0315, 0.0301, 0.0289]
J = [0.5, 0.2, 0.3, 0.1, 0.4]
estados = [1, 2, 3, 4, 5]
N = 1000
x_all = [1]

p = [1, 0, 0, 0, 0]
x = 1
j = J[x-1]

for t in T:
	for i in range(N):
		x_c = np.random.choice(estados)
		j_c = J[x_c - 1]
		deltaJ = j_c - j
		q = pow(np.e, -deltaJ/t)
		r = np.random.rand()
		a = 0 if r>q else 1
		x = (1-a)*x + a*x_c
		j = J[x-1]

		x_all.append(x)

fig = plt.figure(figsize=(8,15))
for t in range(10):
	plt.subplot(5,2,(t+1))
	plt.tight_layout()
	plt.ylim(ymax= 1.0)
	init = 1000*t
	limit = 1000*(t+1)
	data = x_all[init:limit]
	print(len(data))
	eixo_y = [round(float(data.count(i))/len(data),5) for i in estados]
	eixo_x = [J[i-1] for i in estados]
	plt.title('t = {}'.format(T[t]))
	plt.xlabel("Custo")
	plt.ylabel("Probabilidade")
	plt.stem(eixo_x, eixo_y)
	print(T[t], eixo_y)
plt.show()
fig.savefig('10graphs-2.pdf', dpi=100)






