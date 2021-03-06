import matplotlib.pyplot as plt
import ga2 as q2
import numpy as np

L = 25
tam_populacao = 100
max_geracoes = 50000
pc = 0.7  #prob de recombinacao
pm = 1.0/L #prob de mutacao


geracoes = []
for i in range(10):
	results = q2.GA(tam_populacao, max_geracoes, pc, pm, L)
	print(i, results[-1, 0])
	geracoes.append(results[-1, 0])


print(geracoes)
mean = np.mean(geracoes)
std = np.std(geracoes)
print(mean, std)
