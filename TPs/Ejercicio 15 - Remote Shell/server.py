#!/usr/bin/python3

import socket
import subprocess

host = "localhost"
port = 8080


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, int(port)))
s.listen(1)
print("Esperando conexiones...")
clientsocket, addr = s.accept()
print("Tengo una conexión de", str(addr))
while True:
    msg = clientsocket.recv(1024).decode('utf-8')
    if msg != "exit":
        res = subprocess.Popen([msg], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        std_out, std_err = res.communicate()
        if std_out != "":
            msg = "\nOK\n" + std_out
        if std_err != "":
            msg = "\nERROR\n" + std_err

        clientsocket.send(msg.encode('utf-8'))

    else:
        print("\nCerrando conexión...")
        clientsocket.close()
        s.close()
        break
