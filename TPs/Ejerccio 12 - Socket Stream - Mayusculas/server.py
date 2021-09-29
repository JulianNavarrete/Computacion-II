#!/usr/bin/python3

import socket
import sys
import getopt


host = ""
port = 8000


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
    for args in opt:
        if args[0] == '-p':
            port = args[1]
        else:
            print("Error de parámetros.")

except:
    print("Error de parámetros.")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Esperando conexiones...")

s.bind((host, port))
s.listen(1)

clientsocket = s.accept()
print("Tengo una conexión de", str(clientsocket[1]))
resp = "Hola"
s.send(resp.encode("ascii"))
print(resp)
s.close()
