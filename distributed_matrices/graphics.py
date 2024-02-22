import matplotlib.pyplot as plt

data_128 = {'p1': 20.79818797, 'p2': 28.30985569, 'p3': 2.16782784, 'p4': 1.28131246}
data_512 = {'p1': 360.71297001, 'p2': 57.21580719, 'p3': 54.56185030, 'p4': 64.21801948}
data_1024 = {'p1': 851.7835717201233, 'p2': 460.93589615, 'p3': 446.50702381, 'p4': 546.86520099}
data_2048 = {'p1': 18500.30801701, 'p2': 7868.08837008, 'p3': 5547.49227690, 'p4': 9739.87109661}

algoritmos_128 = list(data_128.keys())
tempos_128 = list(data_128.values())

algoritmos_512 = list(data_512.keys())
tempos_512 = list(data_512.values())

algoritmos_1024 = list(data_1024.keys())
tempos_1024 = list(data_1024.values())

algoritmos_2048 = list(data_2048.keys())
tempos_2048 = list(data_2048.values())

plt.figure(figsize=(10, 8))

plt.subplot(221)
plt.plot(algoritmos_128, tempos_128, marker='o')
plt.xlabel('Algoritmo')
plt.ylabel('Tempo (s)')
plt.title('Tempo de Execução para Diferentes Algoritmos (128)')
plt.grid(True)

plt.subplot(222)
plt.plot(algoritmos_512, tempos_512, marker='o')
plt.xlabel('Algoritmo')
plt.ylabel('Tempo (s)')
plt.title('Tempo de Execução para Diferentes Algoritmos (512)')
plt.grid(True)

plt.subplot(223)
plt.plot(algoritmos_1024, tempos_1024, marker='o')
plt.xlabel('Algoritmo')
plt.ylabel('Tempo (s)')
plt.title('Tempo de Execução para Diferentes Algoritmos (1024)')
plt.grid(True)

plt.subplot(224)
plt.plot(algoritmos_2048, tempos_2048, marker='o')
plt.xlabel('Algoritmo')
plt.ylabel('Tempo (s)')
plt.title('Tempo de Execução para Diferentes Algoritmos (2048)')
plt.grid(True)

plt.tight_layout()
plt.show()