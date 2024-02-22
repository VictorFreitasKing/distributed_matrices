import matplotlib.pyplot as plt

time_p1_128 = 20.79818797
time_p1_512 = 360.71297001
time_p1_1024 = 851.7835717201233
time_p1_2048 = 18500.30801701

data_128 = [28.30985569, 2.16782784, 1.28131246]
data_512 = [57.21580719, 54.56185030, 64.21801948]
data_1024 = [460.93589615, 446.50702381, 5468652009963.9892578]
data_2048 = [7868.08837008, 5547.49227690, 9739.87109661]


num_processors = [1, 2, 3]

speedup_128 = [time_p1_128 / t for t in data_128]
speedup_512 = [time_p1_512 / t for t in data_512]
speedup_1024 = [time_p1_1024 / t for t in data_1024]
speedup_2048 = [time_p1_2048 / t for t in data_2048]

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
