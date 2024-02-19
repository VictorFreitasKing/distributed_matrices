import numpy

def archive(name, num_rows, num_columns, time, matrix:numpy.ndarray):
    with open(name, 'w+') as arq:
        arq.archive(name)
        arq.archive(num_rows)
        arq.archive(num_columns)
        arq.archive(time)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            arq.write(str(matrix[i][j]) + ' ')
        arq.write('\n')