#!/usr/bin/python3

import socket
import sys
import getopt


host = "localhost"
port = 8080
protocol = ""
file_out = '/tmp/ej-14-server.txt'


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')
    for args in opt:
        if args[0] == '-p':
            port = args[1]
        if args[0] == '-t':
            protocol = args[1]
        if args[0] == '-f':
            file_out = args[1]

except:
    print("Error de parámetros.")


def udp(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((h, int(p)))
    # s.listen(1)
    print("Esperando conexiones...")

    msg, addr = s.recvfrom(1024)
    print("Tengo una conexión de", str(addr))
    # msg = clientsocket.recv(1024).decode('utf-8')

    print("Texto recibido, escribiendo en archivo...")
    with open(file_out, "w") as file:
        file.writelines(str(msg))

    print("Cerrando conexión...")
    # clientsocket.close()
    s.close()


def tcp(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((h, int(p)))
    s.listen(1)
    print("Esperando conexiones...")

    clientsocket, addr = s.accept()
    print("Tengo una conexión de", str(addr))
    msg = clientsocket.recv(1024).decode('utf-8')

    print("Texto recibido, escribiendo en archivo...")
    with open(file_out, "w") as file:
        file.writelines(msg)

    print("Cerrando conexión...")
    clientsocket.close()
    s.close()


if __name__ == '__main__':
    if protocol == "tcp":
        tcp(host, port)
    elif protocol == "udp":
        udp(host, port)
    else:
        print("Error, protocolo no válido.\nSaliendo...")

