#!/usr/bin/python3


import socket
import sys
import getopt
from datetime import datetime as dt


host = "localhost"
port = 8000
log_file = ""

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'l:')
    for args in opt:
        if args[0] == '-l':
            log_file = args[1]
except:
    print("Error de parámetros.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))

print("-----------Command Prompt-----------\n")
while True:
    msg = input("> ")
    if msg != "exit":
        s.send(msg.encode('utf-8'))
        msg = s.recv(1024)
        print(msg.decode('utf-8'))
        if log_file != "":
            with open(log_file, "a") as file:
                td = dt.today()
                file.writelines("\n" + str(td) + msg.decode('utf-8'))

    else:
        s.send("exit".encode('utf-8'))
        s.close()
        break

print("\nCerrando conexión...")
