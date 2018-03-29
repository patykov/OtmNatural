import numpy as np
import math


T0 = 0.5
eps = 0.1
N = 10000
fim = False
K_max = 5

def J(x):
	return -x +100*pow((x-0.2),2) * pow((x-0.8), 2)

k = 1
x = 0
j = J(x)
x_min = x
j_min = J(x)

while(not fim):
	T = T0/math.log(1+k, 2)

	for i in range(N):
		x_c = x + eps*(np.random.normal()*2-1)
		j_c = J(x_c) 
		deltaJ = j_c - j
		#print('{} xc: {}, jc: {}, deltaj: {}'.format(i, x_c, j_c, deltaJ))
		if deltaJ < 0:
			x = x_c
			j = j_c
		else:
			q = pow(np.e, -deltaJ/T)
			r = np.random.rand()
			a = 0 if r>q else 1
			#print(a)
			x = (1-a)*x + a*x_c
			j = J(x)

		if j < j_min:
			j_min = j
			x_min = x

		#print('xMin: {}, jMin: {} \n'.format(x_min, j_min))

		k +=1
		if k > K_max:
			fim = True



print('xmin: {}, jmin: {}'.format(x_min, j_min))

