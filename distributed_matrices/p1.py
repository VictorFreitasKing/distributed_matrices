import time, numpy
from  multiprocessing import cpu_count
from archive import archive, get_rows_from
from matrix import matrix_to_numpy, get_matrix

def multiply(X: numpy.ndarray, Y: numpy.ndarray):
    rowsX = X.shape[1]
    columnsY = Y.shape[0]

    if rowsX != columnsY:
        return

    resultado = numpy.zeros((X.shape[0], Y.shape[1]))
    for i in range(X.shape[0]):
        print(i)
        for j in range(Y.shape[1]):
            for k in range(X.shape[1]):
                resultado[i][j] += X[i][k] * Y[k][j]

    return resultado

    num_cores = cpu_count

    path = 'resources/4_int.txt'
    rows = get_rows_from(path)
    matrix = get_matrix(rows)

    matrix1 = numpy.zeros((matrix.columns,matrix.columns))
    matrix2 = numpy.zeros((matrix.columns,matrix.columns))

    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)

    before = time.time()
    matrix_result = multiply(matrix1, matrix2)
    after = time.time()
    runtime = after - before

    print(matrix_result)
    print(f'Tempo de execução: {runtime} ms')
