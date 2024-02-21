import numpy

def archive(name, var, colors, clients, rows, columns, time, matrix_response:numpy.ndarray):
    with open(name, 'w+') as arq:
        arq.write(var)            #l1
        arq.write(colors)         #l2
        arq.write(clients)        #l3
        arq.write(rows)           #l4
        arq.write(columns)        #l5
        arq.write(time)           #l6
        arq.write('\n')           #l7

    for i in range(matrix_response.shape[0]):
        for j in range(matrix_response.shape[1]):
            arq.write(str(matrix_response[i][j]) + ' ')
        arq.write('\n')
        arq.close()

def get_rows_from(path):
    with open(path) as arq:
        rows = arq.readlines()
    return rows
