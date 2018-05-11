import matplotlib.pyplot as plt
import ga1 as q1


tam_populacao = 30
max_geracoes = 50
pc = 0.6  #prob de recombinacao
pm = 1/tam_populacao #prob de mutacao

iteracoes = 5
all_P = []
for i in range(iteracoes):
	p = q1.GA(tam_populacao, max_geracoes, pc, pm)
	all_P += p


x_axis = sorted([q1.fenotype(xi) for xi in all_P])
y_axis = [q1.J(xi) for xi in x_axis]

fig = plt.figure()
plt.ylabel('y(x)')
plt.xlabel('x')
plt.plot(x_axis, y_axis, linewidth=2.0)
fig.savefig('lista4-q1-3.pdf', dpi=100)
plt.show()
