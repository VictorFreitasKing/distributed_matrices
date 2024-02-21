from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
import numpy

from archive import *
from matrix import *

path = 'resources/10_int.txt'
curret_target = 2
connections = []
count_connections = 0

def create_matrices():
    rows = get_rows_from(path)
    matrix = get_matrix(rows)

    matrix1 = numpy.zeros((matrix.columns, matrix.columns))
    matrix2 = numpy.zeros((matrix.columns, matrix.columns))

    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)

    matrix1_rows = numpy.array_split(matrix1, curret_target, axis=0)

    return matrix1_rows, matrix2
def broadcast_matrices(matrix1_rows, client):
    for i, row in enumerate(matrix1_rows):
        with connections[i][0] as conn:
            conn.sendall((row, client))

def start():
    global count_connections, connections
    server_socket = socket(AF_INET, SOCK_STREAM)
    with server_socket as ss:
        ss.bind(('localhost', 65432))
        ss.listen()
        print('Servidor iniciado!\n')
        while True:
            connection_socket, addr = ss.accept()
            connections.append((connection_socket, addr))
            count_connections += 1

            connection_socket.sendall(str(connections).encode())

            print(f'{addr} conectou-se ao servidor')
            print(f'{len(connections)} clients conectados ao servidor\n')

            if count_connections == curret_target:
                break

            x, y = create_matrices()
            broadcast_matrices(x,y)


Process(target=start()).start()