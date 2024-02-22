import time, numpy
from multiprocessing import cpu_count, Pool
from archive import archive, get_rows_from
from matrix import matrix_to_numpy, get_matrix

def multiply(matrices: tuple)-> numpy.ndarray:
    X = matrices[0]
    Y = matrices[1]
    columnsX = X.shape[0]
    rowsX = X.shape[1]
    columnsY = Y.shape[0]
    rowsY = Y.shape[1]

    if rowsX != columnsY:
        print('Erro! A matriz não é quadrada.')

    resultado = numpy.zeros((columnsX, rowsY))
    for i in range(columnsX):
        for j in range(rowsY):
            for k in range(rowsX):
                resultado[i][j] += X[i][k] * Y[k][j]

    return resultado

if __name__ == '__main__':
    path = 'resources/2048.txt'
    resultPath = 'resources/results/p3_2048'
    num_cores = cpu_count()
    num_threads = num_cores*2

    matrix = get_matrix(get_rows_from(path))
    matrix1 = numpy.zeros((matrix.rows,matrix.columns))
    matrix2 = numpy.zeros((matrix.rows,matrix.columns))
    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)
    matrixRows = numpy.array_split(matrix1, num_threads, axis=0)

    parts = []
    for i, row in enumerate(matrixRows):
        parts.append((row, matrix2, i))

    with Pool(num_threads) as p:
        before = time.time()
        results = p.map(multiply, parts)
        matrix_result = numpy.zeros((matrix1.shape[0], matrix1.shape[1]))

        j=0
        k=0
        for i, part in enumerate(results):
            for jp in range(part.shape[0]):
                for kp in range(part.shape[1]):
                    matrix_result[j][k] = part[jp][kp]
                    k += 1
                k = 0
                j+=1

        after = time.time()
        runtime = (after - before) * 1000

    archive(resultPath,
        'P3\n',
        f'Numero de cores: {num_cores}\n',
        f'Numero de computadores remotos: {0}\n',
        f'Numero de linhas: {matrix_result.shape[0]}\n',
        f'Numero de colunas: {matrix_result.shape[1]}\n',
        f'Tempo de processamento: {runtime} ms\n',
        matrix_result)

    print('\nProcesso Finalizado')
