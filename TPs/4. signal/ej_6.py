#!/usr/bin/python3

import os
import signal
import time


def handler(s, f):
    print("Soy el hijo2 con PID = " + str(os.getpid()) + ": pong")


def handler2(s, f):
    os.kill(pid2, signal.SIGUSR2)


signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGUSR2, handler2)
while True:
    pid = os.fork()

    if pid == 0:
        # Hijo1
        for i in range(10):
            os.kill(os.getppid(), signal.SIGUSR1)
            print("Soy el hijo1 con PID = " + str(os.getpid()) + ": ping")
            time.sleep(5)

    else:
        pid2 = os.fork()
        if pid2 == 0:
            # Hijo2
            while True:
                signal.pause()
        else:
            # Padre
            while True:
                signal.pause()
