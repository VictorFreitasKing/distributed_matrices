import time, numpy
from multiprocessing import cpu_count, pool
from archive import archive, get_rows_from
from matrix import matrix_to_numpy, get_matrix

def multiply(matrices: tuple):
    columnsX = matrices[0].shape[0]
    rowsX = matrices[0].shape[1]
    columnsY = matrices[1].shape[0]
    rowsY = matrices[1].shape[1]

    if rowsX != columnsY:
        raise 'Erro! A matriz não é quadrada.'

    resultado = numpy.zeros((columnsX, rowsY))
    for i in range(columnsX):
        for j in range(rowsY):
            for k in range(rowsX):
                resultado[i][j] += X[i][k] * Y[k][j]

    return resultado


path = 'resources/128.txt'
result = 'resources/results/p1_teste'
matrix = get_matrix(get_rows_from(path))
num_cores = cpu_count
num_threads = num_cores

print(matrix)

matrix1 = numpy.zeros((matrix.rows,matrix.columns))
matrix2 = numpy.zeros((matrix.rows,matrix.columns))

matrix_to_numpy(matrix, matrix1)
matrix_to_numpy(matrix, matrix2)

matrixRows = numpy.array_split(matrix1, num_threads, axis=0)

pieces = []
for i, row in enumerate(matrixRows):
    pieces.append((row, matrix2, i))

with Pool

before = time.time()
matrix_result = multiply(matrix1, matrix2)
after = time.time()
runtime = (after - before) * 1000
print(runtime)



print(matrix_result)

archive(result, 'P1\n', f'Numero de cores: {num_cores}\n',
    f'Numero de clientes: {1}\n',
    f'Numero de linhas: {matrix_result.shape[0]}\n', f'Numero de colunas: {matrix_result.shape[1]}\n',
    f'Tempo de processamento: {runtime} ms\n', matrix_result)

print('Finalizado')
