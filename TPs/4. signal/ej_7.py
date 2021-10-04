#!/usr/bin/python3

import os
import getopt
import time
from sys import argv
import signal


def handler(s, f):
    print("Soy el PID", os.getpid(), ", recibí la señal", str(s), "de mi padre PID", os.getppid())


signal.signal(signal.SIGUSR2, handler)
n = 0

(opts, args) = getopt.getopt(argv[1:], 'p:', ['process'])

for arg in opts:
    if arg[0] == "-p":
        n = arg[1]


ppid = os.getppid()

try:
    if int(n) > 0:
        for i in range(int(n)):
            if ppid == os.getppid():
                pid = os.fork()
                if pid == 0:
                    signal.pause()
                else:
                    time.sleep(0.05)
                    print("Creando proceso:", str(pid))
                    time.sleep(0.05)
                    os.kill(pid, signal.SIGUSR2)

    else:
        print("Ingrese un valor mayor que 0 como parámtero por favor.")

except:
    print("Ingrese un valor mayor que 0 como parámtero por favor.")
