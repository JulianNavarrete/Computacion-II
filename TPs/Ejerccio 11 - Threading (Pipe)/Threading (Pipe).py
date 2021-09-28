#!/usr/bin/python3

from threading import Thread
from multiprocessing import Queue
from os import getpid
import time


def funcion(num, q):
    pid = str(getpid())
    time.sleep(num/10)
    print("Hilo", str(num) + ",", "PID del padre: " + pid)
    time.sleep(num/2)
    q.put(pid)


if __name__ == '__main__':
    lista_hijos = []
    q = Queue()
    for num in range(10):
        lista_hijos.append(Thread(target=funcion, args=(num, q), daemon=True))
        lista_hijos[-1].start()
    for i in lista_hijos:
        i.join()
    print("Escribiendo lista desde el padre:")
    for i in range(10):
        print(q.get())
    print("Soy el padre, hora de morir...")
