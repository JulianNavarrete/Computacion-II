#!/usr/bin/python3
import os
import socket
import sys
import getopt
from threading import Thread, Lock
import time as t


def child(clientsock, a, f, l):
    msg = clientsock.recv(1024).decode('utf-8')
    letter = msg[0]
    iterations = msg[1:]
    print("Escribiendo letra", str(msg[0]), str(msg[1:]), "veces en el archivo", f, "...")
    l.acquire()
    with open(f, "a") as file_write:
        for i in range(int(iterations)):
            file_write.write(letter)
            file_write.flush()
            t.sleep(1)
    l.release()
    msg = "Letra(s) escrita(s) en el archivo " + f + " del servidor."
    clientsock.send(str(msg).encode('utf-8'))
    clientsock.close()
    print("Conexión cerrada", a)


if __name__ == '__main__':
    host = "localhost"
    port = 8000
    file = ""
    lock = Lock()

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:')
        for args in opt:
            if args[0] == '-p':
                port = args[1]
            if args[0] == '-f':
                file = args[1]
    except:
        print("Error de parámetros.")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(5)
    if os.path.exists("/tmp/ej-18.txt"):
        os.remove("/tmp/ej-18.txt")
    print("Esperando conexiones...")
    while True:
        clientsocket, addr = s.accept()
        print("Tengo una conexión de", str(addr))
        p = Thread(target=child, args=(clientsocket, addr, file, lock))
        p.start()
