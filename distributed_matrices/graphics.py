import matplotlib.pyplot as plt

# Dados
data_128 = {'p1': 1.574162483215332, 'p2': 0.30016112327575684, 'p3': 0.2930641174316406, 'p4': 0.49961137771606445}
data_512 = {'p1': 110.90756726264954, 'p2': 17.266624927520752, 'p3': 17.897562742233276, 'p4': 31.755173444747925}
data_1024 = {'p1': 851.7835717201233, 'p2': 140.77693152427673, 'p3': 144.61570978164673, 'p4': 252.8546233177185}
data_2048 = {'p1': 6597.449085474014, 'p2': 1161.0003385543823, 'p3': 1177.0072283744812, 'p4': 2111.166804075241}

# Configuração dos dados para o gráfico de 128
algoritmos_128 = list(data_128.keys())
tempos_128 = list(data_128.values())

# Configuração dos dados para o gráfico de 512
algoritmos_512 = list(data_512.keys())
tempos_512 = list(data_512.values())

# Configuração dos dados para o gráfico de 1024
algoritmos_1024 = list(data_1024.keys())
tempos_1024 = list(data_1024.values())

# Configuração dos dados para o gráfico de 2048
algoritmos_2048 = list(data_2048.keys())
tempos_2048 = list(data_2048.values())

# Plotagem dos gráficos de linha
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

# Ajuste de layout e exibição dos gráficos
plt.tight_layout()
plt.show()