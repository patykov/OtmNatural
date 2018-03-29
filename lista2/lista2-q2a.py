import numpy as np

N = 10
x = [np.random.rand()]

J = [0.5, 0.2, 0.3, 0.1, 0.4]

for i in range(N):
	x_k = x[i]
	candidata = x_k + 0.1*(np.random.rand()*2 - 1)
	deltaJ = J(candidata) - J(x_k)
	print('\n{} x_: {}, j_: {}, deltaJ: {}'.format(i, candidata, J(candidata), deltaJ))
	q = pow(np.e, -deltaJ/0.1)
	r = np.random.rand()
	print(q>r)
	x.append(candidata if q>r else x_k)