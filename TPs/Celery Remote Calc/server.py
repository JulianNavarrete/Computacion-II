#!/usr/bin/python3

import socket
from sys import argv
from getopt import getopt
from multiprocessing import Process
import celery_calc as cc


def calc(op, num1, num2):
    try:
        if op == "suma":
            result = cc.suma.delay(int(num1), int(num2))
        elif op == "resta":
            result = cc.resta.delay(int(num1), int(num2))
        elif op == "mult":
            result = cc.mult.delay(int(num1), int(num2))
        elif op == "div":
            result = cc.div.delay(int(num1), int(num2))
        elif op == "pot":
            result = cc.pot.delay(int(num1), int(num2))
        else:
            return "Operación inválido."
        return result.get()
    except Exception as e:
        return e


def child(cs, a):
    op = cs.recv(1024).decode('utf-8')
    cs.send("ok".encode('utf-8'))
    num1 = cs.recv(1024).decode('utf-8')
    cs.send("ok".encode('utf-8'))
    num2 = cs.recv(1024).decode('utf-8')
    cs.send("ok".encode('utf-8'))
    print("Parámertos recibidos con éxito.")
    print("Realizando operación...")
    oper = calc(op, num1, num2)
    cs.send(str(oper).encode('utf-8'))
    cs.close()
    print("Conexión con", a, "cerrada.")


if __name__ == "__main":
    host = "0.0.0.0"
    port = 8000

    (opt, arg) = getopt(argv[1:], 'h:p:')
    for args in opt:
        if args[0] == '-h':
            host = args[1]
        elif args[0] == '-p':
            port = int(args[1])
        else:
            print("Error de parámetros.")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(5)
    print("Esperando conexiones...")
    while True:
        clientsocket, addr = s.accept()
        print("Tengo una conexión de", str(addr))
        p = Process(target=child, args=(clientsocket, addr))
        p.start()
