#!/usr/bin/python3

from sys import argv
from getopt import getopt
import socket


host = "0.0.0.0"
port = 8000
op = ""
num1 = 0
num2 = 0

(opt, arg) = getopt(argv[1:], 'h:p:o:n:m:')
for args in opt:
    if args[0] == '-h':
        host = args[1]
    elif args[0] == '-p':
        port = int(args[1])
    elif args[0] == '-o':
        op = args[1]
    elif args[0] == '-n':
        num1 = args[1]
    elif args[0] == '-m':
        num2 = args[1]
    else:
        print("Error de parámetros.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))

s.send(op.encode('utf-8'))
msg = s.recv(1024).decode('utf-8')
if msg == 'ok':
    s.send(num1.encode('utf-8'))
    msg2 = s.recv(1024).decode('utf-8')
    if msg2 == 'ok':
        s.send(num2.encode('utf-8'))
        msg3 = s.recv(1024).decode('utf-8')
        if msg3 == 'ok':
            print("Operador y números enviados con éxito.")
            print("Saliendo...")
            result = s.recv(1024).decode('utf-8')
            print("El resultado es:", result)
            s.close()
