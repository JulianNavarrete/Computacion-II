#!/usr/bin/python3

import socket
import sys
import getopt
import signal

host = "localhost"
port = 8000
protocol = ""
# exitWhileBool = False

# noinspection PyBroadException
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


'''def exit_while_fnc(s, frame):
    exitWhileBool = True
    return exitWhileBool
'''

def udp(h, p):
    pass


def tcp(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((h, int(p)))
    msg = ""
    exitWhileBool = False
    signal.signal(signal.SIGINT, exitWhileBool=True)
    cadena = input("Introduzca líneas de texto:\n")
    while not exitWhileBool:
        msg = msg + cadena + "\n"
        # exit_while = True
    s.send(msg.encode('utf-8'))
    print("Cerrando conexión...")


if __name__ == '__main__':
    if protocol == "tcp":
        tcp(host, port)
    elif protocol == "udp":
        udp(host, port)
    else:
        print("Error, protocolo no válido.\nSaliendo...")
