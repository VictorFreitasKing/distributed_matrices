from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process

import numpy

from archive import *
from matrix import *

path = 'resources/4_int.txt'
curret_target = 0
connections = []
count_connections = 0

def create_matrix():
    rows = get_rows_from(path)
    matrix = get_matrix(rows)

    matrix1 = numpy.zeros((matrix.columns, matrix.columns))
    matrix2 = numpy.zeros((matrix.columns, matrix.columns))

    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)

    matrix1_rows = numpy.array_split(matrix1, curret_target, axis=0)

    return matrix1_rows, matrix2
def broadcast_matrix(matrix1_rows, client):
    for idx, row in enumerate(matrix1_rows):
        with connections[idx][0] as conn:
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


Process(target=start()).start()