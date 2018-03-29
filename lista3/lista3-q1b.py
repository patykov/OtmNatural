import matplotlib.pyplot as plt
import numpy as np


def D(t, X):
	X1 = [xi for xi in X if xi <= t]
	X2 = [xi for xi in X if xi > t]
	if len(X1) > 0 :
		y1 = float(sum(X1))/len(X1)
	if len(X2) > 0 :
		y2 = float(sum(X2))/len(X2)

	dist_x1 = [pow(xi-y1, 2) for xi in X1]
	dist_x2 = [pow(xi-y2, 2) for xi in X2]

	return 0.25*(sum(dist_x1+dist_x2))



X = [0, 4, 6, 9]
Y = [3.0, 3.4]
T = 1.0

p_ = [] #matriz p nao normalizada
for y1 in Y:
    line = []
    for xi in X:
        dist = pow(xi-yi, 2)
        line.append(pow(np.e, -dist/T))
    p_.append(line)
print(p_)
mi = [sum(p_[i, :]) for i in len(Y)]
print(mi)
p = [pi/mi for pi in p_]
print(p)
