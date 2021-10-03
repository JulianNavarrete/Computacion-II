#!/usr/bin/python3

import socket
import sys
import getopt


host = "localhost"
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

s.bind((host, port))
s.listen(1)

print("Esperando conexiones...")

clientsocket, addr = s.accept()
print("Tengo una conexión de", str(addr))
msg = clientsocket.recv(1024).decode('utf-8')
resp = msg.upper()
clientsocket.send(resp.encode('utf-8'))
print("Enviando", resp, "al cliente...")
print("Cerrando conexión...")
clientsocket.close()
s.close()
