from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process, Pool
import numpy, time
from matrix import matrix_to_numpy

from archive import *
from matrix import *

path = 'resources/10_float.txt'
connections_await = 2
connections = []
count_connections = 0


def parts_generate():
    rows = get_rows_from(path)
    matrix = get_matrix(rows)

    matrix1 = numpy.zeros((matrix.columns, matrix.columns))
    matrix2 = numpy.zeros((matrix.columns, matrix.columns))

    matrix_to_numpy(matrix, matrix1)
    matrix_to_numpy(matrix, matrix2)

    matrix1_rows = numpy.array_split(matrix1, connections_await, axis=0)

    return matrix1_rows, matrix2


def broadcast_parts(matrix_rows):
    matrixtemp = numpy.zeros((len(matrix_rows),len(matrix_rows)))
    parts = []
    for i, row in enumerate(matrix_rows):
        parts.append((row, matrixtemp, i))


    for i, rows in enumerate(matrix_rows):
        conn, addr = connections[i]
        rows = rows.tobytes()
        conn.send(rows)


def start():
    global count_connections, connections_await
    server_socket = socket(AF_INET, SOCK_STREAM)
    print('Servidor iniciado!\n')
    with server_socket as ss:
        ss.bind(('localhost', 65432))
        ss.listen()
        while True:
            connection_socket, addr = ss.accept()
            connections.append((connection_socket, addr))
            count_connections += 1

            print(f'{addr} conectou-se ao servidor')
            print(f'{len(connections)} clients conectados ao servidor\n')

            if count_connections == connections_await:
                print('Conexões  atingidas')
                break
        rows, matrix = parts_generate()
        broadcast_parts(rows)


Process(target=start()).start()
