from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process


curret_target = 0
connections = []
count_connections = 0


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