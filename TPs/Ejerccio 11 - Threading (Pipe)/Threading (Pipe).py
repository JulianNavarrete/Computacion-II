#!/usr/bin/python3

from threading import Thread
from multiprocessing import Pipe
from os import getpid
import sys


def th1(w):
    sys.stdin = open(0)
    while True:
        entrada = input("Ingrese un mensaje: ")
        if entrada != "exit":
            w.send(entrada)
            w.recv()
        else:
            w.send(entrada)
            exit(-1)


def th2(r):
    while True:
        mensaje = r.recv()
        if mensaje != "exit":
            print("Leyendo (pid proceso principal = " + str(getpid()) + "):", mensaje + "\n")
            r.send("")
        else:
            print("\nTerminando hilos...")
            exit(-1)


if __name__ == '__main__':
    w, r = Pipe()
    p1 = Thread(target=th1, args=(w,))
    p2 = Thread(target=th2, args=(r,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Soy el proceso principal, hora de morir...")
