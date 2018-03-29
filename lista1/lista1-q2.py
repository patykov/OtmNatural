import numpy as np

N = 1000000

a = np.random.rand(N,2)
b = a*2 -1
c = [1 if (pow(bi[0],2) + pow(bi[1],2) <1) else 0 for bi in b]

pi = float(4*sum(c))/N
print(pi)