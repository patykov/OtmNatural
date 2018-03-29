import numpy as np
import os


M = np.array(
	[[0, 1.0/(4*pow(np.e, 3)), 1.0/(4*pow(np.e, 2)), 1.0/(4*pow(np.e, 4)), 1.0/(4*np.e)], 
	[1.0/4, (3.0/4 - 1.0/(4*pow(np.e, 3)) - 1.0/(4*np.e) - 1.0/(4*pow(np.e, 2))), 1.0/4, 1.0/(4*np.e), 1.0/4], 
	[1.0/4, 1.0/(4*np.e), (1.0/2 - 1.0/(4*pow(np.e, 2)) - 1.0/(4*np.e)), 1.0/(4*pow(np.e, 2)), 1.0/4],
	[1.0/4, 1.0/4, 1.0/4, (1.0 - 1.0/(4*pow(np.e, 4)) - 1.0/(4*np.e) - 1.0/(4*pow(np.e, 2)) - 1.0/(4*pow(np.e, 3))), 1.0/4],
	[1.0/4, 1.0/(4*pow(np.e, 2)), 1.0/(4*np.e), 1.0/(4*pow(np.e, 3)), (1.0/4 - 1.0/(4*np.e))]])

p = M[:, x[t]-1]
x = [1]
for t in range(4):
	r = np.random.rand()
	p = M[:, x[t]-1]
	print(t, r)
	print([round(i, 3) for i in p])
	for j in range(len(p)):
		if sum(p[:j])<= r < sum(p[:j+1]):
			print('adding', j+1)
			x.append(j+1)
			break
	print(x)
	#print(t, round(r, 3), [round(i, 3) for i in p], x)