import numpy as np


M = np.array(
	[[0, 1.0/(4*pow(np.e, 3)), 1.0/(4*pow(np.e, 2)), 1.0/(4*pow(np.e, 4)), 1.0/(4*np.e)], 
	[1.0/4, (3.0/4 - 1.0/(4*pow(np.e, 3)) - 1.0/(4*np.e) - 1.0/(4*pow(np.e, 2))), 1.0/4, 1.0/(4*np.e), 1.0/4], 
	[1.0/4, 1.0/(4*np.e), (1.0/2 - 1.0/(4*pow(np.e, 2)) - 1.0/(4*np.e)), 1.0/(4*pow(np.e, 2)), 1.0/4],
	[1.0/4, 1.0/4, 1.0/4, (1.0 - 1.0/(4*pow(np.e, 4)) - 1.0/(4*np.e) - 1.0/(4*pow(np.e, 2)) - 1.0/(4*pow(np.e, 3))), 1.0/4],
	[1.0/4, 1.0/(4*pow(np.e, 2)), 1.0/(4*np.e), 1.0/(4*pow(np.e, 3)), (1.0/4 - 1.0/(4*np.e))]])

autovalores, autovetor = np.linalg.eig(M)

p = autovetor[:, 0]

# Questao 2c
print([round(a/sum(p), 4) for a in p])


#Questao 2d
e = [1.0/pow(np.e, 5), 1.0/pow(np.e, 2), 1.0/pow(np.e, 3), 1.0/np.e, 1.0/pow(np.e, 4)]

print([round(ei, 3) for ei in e])


print([pi/ei for pi, ei in zip(p,e)])