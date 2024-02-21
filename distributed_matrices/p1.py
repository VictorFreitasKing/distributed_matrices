import time, numpy
from archive import archive, get_rows_from
from matrix import matrix_to_numpy, get_matrix

def multiply(X: numpy.ndarray, Y: numpy.ndarray):
    columnsX = X.shape[0]
    rowsX = X.shape[1]
    columnsY = Y.shape[0]
    rowsY = Y.shape[1]

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

print(matrix)

matrix1 = numpy.zeros((matrix.rows,matrix.columns))
matrix2 = numpy.zeros((matrix.rows,matrix.columns))

matrix_to_numpy(matrix, matrix1)
matrix_to_numpy(matrix, matrix2)

before = time.time()
matrix_result = multiply(matrix1, matrix2)
after = time.time()
runtime = (after - before) * 1000
print(runtime)


print(matrix_result)

archive(result, 'P1\n', f'Numero de cores: Não usa Thread\n',
    f'Numero de clientes: {1}\n',
    f'Numero de linhas: {matrix_result.shape[0]}\n', f'Numero de colunas: {matrix_result.shape[1]}\n',
    f'Tempo de processamento: {runtime} ms\n', matrix_result)

print('Finalizado')
