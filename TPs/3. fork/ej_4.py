#!/usr/bin/python

import os

code = os.fork()

if code == 0:
    for i in range(5):
        print("Soy el hijo, PID", os.getpid())
    print("PID", os.getpid(), "terminando")
    os._exit(0)

else:
    for i in range(2):
        print("Soy el padre, PID", os.getpid(), ", mi hijo es", code)
    os.wait()
    print("Mi proceso hijo, PID", code, ", terminó.")
