#!/usr/bin/python3

from multiprocessing import Process, Pipe
from os import pipe, getpid, fdopen


def ch1(w):
    r.close()
    for i in range(500):
        entrada = input("Ingrese un mensaje: ")
        w.send(entrada)
        w.close()


def ch2(r):
    w.close()
    while True:
        mensaje = r.recv()
        r.close()
        print("Leyendo(PID=" + str(getpid()) + ") leyendo:\n", mensaje)


if __name__ == '__main__':
    r, w = Pipe()
    p1 = Process(target=ch1, args=(w,))
    p2 = Process(target=ch2, args=(r,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Hora de morir tambien... Bye... (x.x)")
