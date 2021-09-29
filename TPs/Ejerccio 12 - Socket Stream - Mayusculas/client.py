#!/usr/bin/python3

import socket
import sys
import getopt


host = ""
port = 8000


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:a:')
    for args in opt:
        if args[0] == '-p':
            port = args[1]
        if args[0] == '-a':
            host = args[1]
        else:
            print("Error de parámetros.")

except:
    print("Error de parámetros.")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
msg = input("Introduzca una cadena de texto: ").encode("ascii")
s.send(msg)
print(s.recv(1024).decode("ascii"))
