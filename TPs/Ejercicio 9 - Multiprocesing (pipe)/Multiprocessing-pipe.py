#!/usr/bin/python3


from multiprocessing import Process, Pipe
from os import getpid
import sys


def ch1(w):
    sys.stdin = open(0)
    while True:
        entrada = input("Ingrese un mensaje: ")
        if entrada != "exit":
            w.send(entrada)
            w.recv()
        else:
            w.send(entrada)
            exit(-1)


def ch2(r):
    while True:
        mensaje = r.recv()
        if mensaje != "exit":
            print("Leyendo (pid=" + str(getpid()) + "):", mensaje + "\n")
            r.send("")
        else:
            print("\nMatando hijos...")
            exit(-1)


if __name__ == '__main__':
    w, r = Pipe()
    p1 = Process(target=ch1, args=(w,))
    p2 = Process(target=ch2, args=(r,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Soy el padre, hora de morir tambien...")
