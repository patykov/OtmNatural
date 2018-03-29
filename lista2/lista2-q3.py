import matplotlib.pyplot as plt
import numpy as np
import math

def norma(a, b):
	return pow((a[0]-b[0]), 2) + pow(abs(a[1]-b[1]), 2)

def get_centroideJ(x, p):
	def J(y):
		return float(sum(norma(xi, y[p[i]]) for i, xi in enumerate(x)))/len(x)
	return J

def SA(x0, J, candidata, T0=0.1, N=10000, K_max=10):
	fim = False
	k = 1
	x = x0
	j = J(x)
	x_min = x
	j_min = J(x)

	while(not fim):
		T = T0/math.log(1+k, 2)
		for i in range(N):
			x_c = candidata(x[:])
			j_c = J(x_c) 
			deltaJ = j_c - j

			q = pow(np.e, -deltaJ/T)
			r = np.random.rand()
			a = 0 if r>q else 1
			x = (1-a)*x + a*x_c
			j = J(x)

			if j < j_min:
				j_min = j
				x_min = x

			k +=1
			if k > K_max:
				fim = True

	print('xMin: {}, jMin: {} \n'.format(x_min, j_min))
	return x


Y = [[1, 0], [4, 0]]
X = [[1, 3], [2, 2], [2, 4], [3, 2], [3, 4], [4, 3], [1, -3], [2, -2], [3, -2], [4, -3]]
particao = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1] # Particao ja definida


J_centroide = get_centroideJ(X, particao)
def candidata(y):
	i = np.random.randint(len(y))
	y[i] = [round(y[i][0] + 0.01+(np.random.rand()*2 - 1), 3), 
			round(y[i][1] + 0.01+(np.random.rand()*2 - 1), 3)]
	return y

new_y = SA(Y, J_centroide, candidata)

fig = plt.figure()
plt.plot([xi[0] for xi in X], [xi[1] for xi in X], 'ro')
plt.plot([yi[0] for yi in Y], [yi[1] for yi in Y], 'g+')
plt.plot([yi[0] for yi in new_y], [yi[1] for yi in new_y], 'bo')
plt.ylabel('Y')
plt.xlabel('X')

plt.show()
fig.savefig('cluster.png', dpi=100)


