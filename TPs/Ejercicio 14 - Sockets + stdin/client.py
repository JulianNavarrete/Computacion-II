#!/usr/bin/python3

import socket
import sys
import getopt


def udp(h, p):
    print("Protocolo UDP elegido.")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print("Error en crear socket")
        sys.exit()

    msg = ""
    print("Ingrese texto:")
    while True:
        try:
            cadena = input(">>> ")
            msg = msg + cadena + "\n"
        except:
            break
    try:
        s.sendto(msg.encode(), (h, int(p)))
        print("\nDatos enviados, cerrando conexión...")
    except Exception as e:
        print("\nError:", e)


def tcp(h, p):
    print("Protocolo TCP elegido.")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((h, int(p)))
    msg = ""
    print("Ingrese texto:")
    while True:
        try:
            cadena = input(">>> ")
            msg = msg + cadena + "\n"
        except:
            break
    s.send(msg.encode('utf-8'))
    print("\nDatos enviados, cerrando conexión...")


if __name__ == '__main__':
    host = "localhost"
    port = 8080
    protocol = ""

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'p:a:t:')
        for args in opt:
            if args[0] == '-p':
                port = args[1]
            if args[0] == '-a':
                host = args[1]
            if args[0] == '-t':
                protocol = args[1]
    except:
        print("Error de parámetros.")

    if protocol == "tcp":
        tcp(host, port)
    elif protocol == "udp":
        udp(host, port)
    else:
        print("Error, protocolo no válido.\nSaliendo...")
