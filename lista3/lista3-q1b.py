import matplotlib.pyplot as plt
import numpy as np


X = [0, 4, 6, 9]
Y = [3.0, 3.4]
T = 50.0#0.1 #1.0

p_ = [] #matriz p nao normalizada
for yi in Y:
    line = []
    for xi in X:
        dist = pow(xi-yi, 2)
        line.append(pow(np.e, -dist/T))
    p_.append(line)
p_ = np.array(p_)
print("Matrix nao normalizada:")
print(p_)

mi = [sum(p_[:, i]) for i in range(len(X))]
print("Vetor mi:")
print(mi)

p = np.array([pi/mi for pi in p_])
print("Matrix p(y|x):")
print(p)
