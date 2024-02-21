import time, numpy
from  multiprocessing import cpu_count
from archive import archive, get_rows_from
from matrix import matrix_to_numpy, get_matrix

def multiply(X: numpy.ndarray, Y: numpy.ndarray):
    columnsX = X.shape[0]
    rowsX = X.shape[1]
    columnsY = Y.shape[0]
    rowsY = Y.shape[1]

    if rowsX != columnsY:
        print('Erro! A matriz não é quadrada.')
        return None

    resultado = numpy.zeros((columnsX, rowsY))
    for i in range(columnsX):
        print(i)
        for j in range(rowsY):
            for k in range(rowsX):
                resultado[i][j] += X[i][k] * Y[k][j]

    return resultado

    path = 'resources/4_int.txt'
    matrix = get_matrix(get_rows_from(path))
    cpus = cpu_count

    matrix1 = numpy.zeros((matrix.columns,matrix.columns))
    matrix2 = numpy.zeros((matrix.columns,matrix.columns))

    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)

    before = time.time()
    matrix_result = multiply(matrix1, matrix2)
    after = time.time()
    runtime = after - before

    archive('resources/results/p1', 'Solução p1 feita com abordagem tradicional O(3)\n', f'Num cores: {num_cpu_cores}\n',
      f'Num cliente: {0}\n',
      f'Num linhas: {final_matrix.shape[0]}\n', f'Num colunas: {final_matrix.shape[1]}\n',
      f'Tempo para multiplicar e juntar: {total_time} segundos\n', final_matrix))

