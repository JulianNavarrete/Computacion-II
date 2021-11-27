#!/usr/bin/python3

import asyncio
import socket
import subprocess


async def function(cs, a):
    while True:
        msg = cs.recv(1024).decode('utf-8')
        if msg != "exit":
            res = subprocess.Popen([msg], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            std_out, std_err = res.communicate()
            if std_out != "":
                msg = "\nOK\n" + std_out
            if std_err != "":
                msg = "\nERROR\n" + std_err

            cs.send(msg.encode('utf-8'))

        else:
            cs.close()
            # s.close()
            print("Conexión cerrada", a)
            break


async def main():
    host = "localhost"
    port = 8000
    lista_tasks = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(5)
    print("Esperando conexiones...")
    while True:
        clientsocket, addr = s.accept()
        print("Tengo una conexión de", str(addr))
        task = asyncio.create_task(function(clientsocket, addr))
        lista_tasks.append(task)
        await lista_tasks




asyncio.run(main())
