#!/usr/bin/python3

import os
import signal
import time


def handler1(s, f):
    # Leer pipe
    pass


def handler2(s, f):
    # Escribir en pipe
    pass


def handler3(s, f):
    # Escribir en pipe
    pass


r, w = os.pipe()
pid = os.fork()


if pid == 0:
    pid2 = os.fork()
    if pid2 == 0:
        # Proceso C
        signal.signal(signal.SIGUSR1, handler3)
        signal.pause()
        w = os.fdopen(w, "w")
        w.write("Mensaje 2 (PID=" + str(os.getpid()) + ")\n")
        w.close()
        os.kill(int(os.getppid() - 1), signal.SIGUSR2)

    else:
        # Proceso B
        time.sleep(0.2)
        signal.signal(signal.SIGUSR1, handler2)
        signal.pause()
        w = os.fdopen(w, "w")
        w.write("Mensaje 1 (PID=" + str(os.getpid()) + ")\n")
        w.close()
        os.kill(pid2, signal.SIGUSR1)

else:
    # Proceso A
    time.sleep(0.5)
    signal.signal(signal.SIGUSR2, handler1)
    os.kill(pid, signal.SIGUSR1)
    signal.pause()
    os.close(w)
    r = os.fdopen(r)
    cadena = r.readlines()
    print("A (PID=" + str(os.getpid()) + ") leyendo:\n".strip("\n"))
    for i in cadena:
        print(i.strip("\n"))
