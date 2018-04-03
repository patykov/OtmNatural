import numpy as np 
import math


# Rosenbronk function
def J(X):
    result = 0

    for i in range(len(X)-1):
        result+= 100*(X[i+1] - X[i]**2)**2 + (1 - X[i])**2
    return result

X = np.random.rand(20) #random values from 0 to 20
T0 = 0.5
x = X
j = J(x)
N = 100000
eps = 0.005
K_max = 15
k = 1

fim = False
x_min = x
j_min = j

while(not fim):
    T = T0/math.log(1+k, 2)
    for i in range(N):
        R = np.random.rand()*2 -1
        x_c = [xi + eps*R for xi in x]
        j_c = J(x_c)
        deltaJ = j_c - j

        q = pow(np.e, -deltaJ/T)
        r = np.random.rand()
        if q>r:
            x = x_c
            j = J(x_c)

        if j < j_min:
            print(j)
            j_min = j
            x_min = x

        k +=1
        if k > K_max:
            fim = True

print('xMin: {}, jMin: {} \n'.format(x_min, j_min))
