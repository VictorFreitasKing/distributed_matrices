from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
import pickle, numpy

def multiply(X: numpy.ndarray, Y: numpy.ndarray):
    columnsX = X.shape[0]
    #rowsX = X.shape[1]
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
            #file = cs.recv(1024)
            rows = cs.recv(4096)
            rowsconv = numpy.frombuffer(rows)
            print(rowsconv)
            #aqui multiplica



Process(target=start()).start()