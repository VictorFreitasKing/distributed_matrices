from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process

def start():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect(('localhost', 65432))
        print(f'Client conectado!')
        strg = ''
        while True:
            strg += ' '

Process(target=start()).start()