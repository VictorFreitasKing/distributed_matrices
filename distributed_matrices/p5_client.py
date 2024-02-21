from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process

def start():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect(('localhost', 65432))
        while True:
            index = cs.recv(1024).decode()
            file = cs.recv(1024)

        print(f'Client conectado!')


Process(target=start()).start()