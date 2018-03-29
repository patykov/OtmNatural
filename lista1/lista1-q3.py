import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


N = 10
x = [np.random.rand()]
print(x)
def J(x):
	return pow(x,2)

for i in range(N):
	x_k = x[i]
	candidata = x_k + 0.1*(np.random.rand()*2 - 1)
	deltaJ = J(candidata) - J(x_k)
	print('\n{} x_: {}, j_: {}, deltaJ: {}'.format(i, candidata, J(candidata), deltaJ))
	q = pow(np.e, -deltaJ/0.1)
	r = np.random.rand()
	print(q>r)
	x.append(candidata if q>r else x_k)


#plt.hist(x, 50, normed=1)
#plt.show()