#!/usr/bin/python3

import socket
import sys
import getopt


host = "localhost"
port = 8000
iterations = 0
letter = ""

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:c:r:')
    for args in opt:
        if args[0] == '-h':
            host = args[1]
        if args[0] == '-p':
            port = args[1]
        if args[0] == '-c':
            letter = args[1]
        if args[0] == '-r':
            iterations = args[1]
except:
    print("Error de parámetros.")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))

if int(iterations) > 0:
    msg = (letter + iterations).encode('utf-8')
    s.send(msg)
    print("Se ha enviado al server la letra", letter, "para escribirla",
          iterations, "veces.\nEsperando confirmación del server...")
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    print("Cerrando conexión...")
else:
    s.send("exit".encode('utf-8'))
    print("Número de iteraciones no válido. Saliendo...")

s.close()
