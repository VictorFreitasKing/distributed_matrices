import matplotlib.pyplot as plt

# Tempos de execução para diferentes tamanhos de matriz (128, 512, 1024, 2048) usando apenas um processador
time_p1_128 = 1.574162483215332
time_p1_512 = 110.90756726264954
time_p1_1024 = 851.7835717201233
time_p1_2048 = 6597.449085474014

# Tempos de execução paralelos para cada tamanho de matriz (128, 512, 1024, 2048) usando 3 processadores
data_128 = [0.30016112327575684, 0.2930641174316406, 0.49961137771606445]
data_512 = [17.266624927520752, 17.897562742233276, 31.755173444747925]
data_1024 = [140.77693152427673, 144.61570978164673, 252.8546233177185]
data_2048 = [1161.0003385543823, 1177.0072283744812, 2111.166804075241]

# Número de processadores utilizados
num_processors = [1, 2, 3]

# Calcula o speedup para cada tamanho de matriz
speedup_128 = [time_p1_128 / t for t in data_128]
speedup_512 = [time_p1_512 / t for t in data_512]
speedup_1024 = [time_p1_1024 / t for t in data_1024]
speedup_2048 = [time_p1_2048 / t for t in data_2048]

# Plota o gráfico de speedup para cada tamanho de matriz
plt.plot(num_processors, speedup_128, marker='o', linestyle='-', label='128x128')
plt.plot(num_processors, speedup_512, marker='o', linestyle='-', label='512x512')
plt.plot(num_processors, speedup_1024, marker='o', linestyle='-', label='1024x1024')
plt.plot(num_processors, speedup_2048, marker='o', linestyle='-', label='2048x2048')

plt.xlabel('Número de Processadores')
plt.ylabel('Speedup')
plt.title('Gráfico de Speedup para Diferentes Tamanhos de Matriz')
plt.legend()
plt.grid(True)
plt.show()
