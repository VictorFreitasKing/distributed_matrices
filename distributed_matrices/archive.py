import numpy

def archive(name, var, colors, clients, rows, columns, time, matrix_response:numpy.ndarray):
    with open(name, 'w+') as arq:
        arq.archive(var)            #l1
        arq.archive(colors)         #l2
        arq.archive(clients)        #l3
        arq.archive(rows)           #l4
        arq.archive(columns)        #l5
        arq.archive(time)           #l6
        arq.archive('\n')           #l7

    for i in range(matrix_response.shape[0]):
        for j in range(matrix_response.shape[1]):
            arq.write(str(matrix_response[i][j]) + ' ')
        arq.write('\n')

def get_rows_from(path):
    with open(path) as arq:
        rows = arq.readlines()
    return rows
