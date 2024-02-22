from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process, Pool
import numpy

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
def start():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect(('localhost', 65432))
        wait = True
        while wait:
            rows = cs.recv(4096)
            matrix = cs.recv(4096)
            rowsconv = numpy.frombuffer(rows)
            matrixconv = numpy.frombuffer(matrix)

            #aqui multiplica - Fazer depois dos graficos para caso n dê tempo
            total_clients = 2



Process(target=start()).start()