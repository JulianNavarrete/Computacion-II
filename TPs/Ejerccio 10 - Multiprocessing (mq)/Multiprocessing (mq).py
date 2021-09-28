#!/usr/bin/python3

from multiprocessing import Process, Queue
from os import getpid
import time


def funcion(num, q):
    pid = str(getpid())
    time.sleep(num/10)
    print("Proceso", num, "PID: ", pid)
    time.sleep(num/10)
    q.put(pid)


if __name__ == '__main__':
    lista_hijos = []
    q = Queue()
    for num in range(10):
        lista_hijos.append(Process(target=funcion, args=(num, q)))
        lista_hijos[-1].start()
    for i in lista_hijos:
        i.join()
    for i in range(10):
        print(q.get())
    print("Soy el padre, hora de morir...")
