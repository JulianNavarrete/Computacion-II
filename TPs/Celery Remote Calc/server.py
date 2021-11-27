#!/usr/bin/python3

import socket
from sys import argv
from getopt import getopt
from multiprocessing import Process


def child(cs, a):
    pass





if __name__ == "__main":
    host = "0.0.0.0"
    port = 8000

    (opt, arg) = getopt(argv[1:], 'h:p:')
    for args in opt:
        if args[0] == '-h':
            host = args[1]
        elif args[0] == '-p':
            port = int(args[1])
        else:
            print("Error de parámetros.")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(5)
    print("Esperando conexiones...")
    while True:
        clientsocket, addr = s.accept()
        print("Tengo una conexión de", str(addr))
        p = Process(target=child, args=(clientsocket, addr))
        p.start()

