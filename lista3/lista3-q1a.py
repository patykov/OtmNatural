import matplotlib.pyplot as plt
import numpy as np


def D(t):
	X = [0, 4, 6, 9]
	X1 = [xi for xi in X if xi <= t]
	X2 = [xi for xi in X if xi > t]
	if len(X1) > 0 :
		y1 = float(sum(X1))/len(X1)
	if len(X2) > 0 :
		y2 = float(sum(X2))/len(X2)

	dist_x1 = [pow(xi-y1, 2) for xi in X1]
	dist_x2 = [pow(xi-y2, 2) for xi in X2]

	return 0.25*(sum(dist_x1+dist_x2))


x_axis = np.arange(-1, 11)
y_axis = [D(t) for t in x_axis]
print([(t, round(D(t),3)) for t in x_axis])
fig = plt.figure(figsize=(8,4))

plt.xlabel("t")
plt.xlim((-2, 11))
plt.xticks(np.arange(-1, 11))
plt.ylabel("D(t)")
#plt.yticks(y_axis)
plt.plot(x_axis, y_axis, 'ro')
#plt.show()

#fig.savefig('lista3-q1a2.pdf', dpi=100)