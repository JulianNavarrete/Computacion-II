import threading
from getopt import getopt
from sys import argv
import time


def main(lock, iteraciones, num):
    lock.acquire()  # ----------------------------
    for i in range(iteraciones):
        archivo.write(abecedario[num])
        archivo.flush()
        print(abecedario[num])
        time.sleep(1)
    lock.release()  # ----------------------------


(opt, arg) = getopt(argv[1:], 'n:f:r:')
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
hilos = 0
file_name = ""
iteraciones = 0
lista_hilos = []

for args in opt:
    if args[0] == '-n':
        hilos = int(args[1])
    elif args[0] == '-f':
        file_name = args[1]
    elif args[0] == '-r':
        iteraciones = int(args[1])


if __name__ == '__main__':
    lock = threading.Lock()

    archivo = open(file_name, "w")
    for num in range(hilos):
        lista_hilos.append(threading.Thread(target=main, args=(lock, iteraciones, num)))
        lista_hilos[-1].start()
    for i in lista_hilos:
        i.join()
    archivo.close()
