import matplotlib.pyplot as plt
import numpy as np

M = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
t_max = 3

A = np.zeros([100,4])
for i in range(100):
	estado_0 = i%3
	x = [estado_0]
	for t in range(t_max):
		r = np.random.rand()
		p = M[:, x[t]]
		if 0<= r < p[0]: x.append(0)
		elif p[0]<= r < p[0]+p[1]: x.append(1)
		else: x.append(2)
	A[i] = x

A0 = A[:, 0]
A1 = A[:, 1]
A2 = A[:, 2]
A3 = A[:, 3]

plt.subplot(221)
x, y = np.unique(A0, return_counts=True)
print(x,y)
plt.title('t = 0')
plt.ylim(ymax= 0.5)
plt.plot(x, [float(yi)/100 for yi in y], 'bo')

plt.subplot(222)
x, y = np.unique(A1, return_counts=True)
print(x,y)
plt.title('t = 1')
plt.ylim(ymax= 0.5)
plt.plot(x, [float(yi)/100 for yi in y], 'bo')

plt.subplot(223)
x, y = np.unique(A2, return_counts=True)
print(x,y)
plt.title('t = 2')
plt.ylim(ymax= 0.5)
plt.plot(x, [float(yi)/100 for yi in y], 'bo')

plt.subplot(224)
x, y = np.unique(A3, return_counts=True)
print(x,y)
plt.title('t = 3')
plt.ylim(ymax= 0.5)
plt.plot(x, [float(yi)/100 for yi in y], 'bo')
plt.show()
