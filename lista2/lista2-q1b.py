import numpy as np

p = [0.3, 0.4, 0.3]
M = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
t_max = 3
x = [1]

for t in range(t_max):
	r = np.random.rand()
	p = M[:, x[t]]
	if 0<= r <= p[0]: x.append(0)
	elif p[0]<= r <= p[0]+p[1]: x.append(1)
	elif p[0]+p[1] <= r <= p[0]+p[1]+p[2]: x.append(2)
	print(t, r, p, x)
print(t, r, p, np.unique(x, return_counts=True))

