import matplotlib.pyplot as plt
import ga2 as q2

L = 25
tam_populacao = 100
max_geracoes = 100
pc = 0.7  #prob de recombinacao
pm = 1.0/L #prob de mutacao

results = q2.GA(tam_populacao, max_geracoes, pc, pm, L)

geracao = results[:, 0]
best = results[:, 1]
mean = results[:, 2]
worst = results[:, 3]


fig = plt.figure()
plt.ylabel('Aptidao')
plt.xlabel('Geracoes')
plt.plot(geracao, best)
plt.plot(geracao, mean)
plt.plot(geracao, worst)
fig.savefig('lista6-q2a-2.pdf', dpi=100)
plt.show()
