#!/usr/bin/python3

import os
from getopt import getopt
from sys import argv
import time

n = 0

(opt, arg) = getopt(argv[1:], 'n:')

for args in opt:
    if args[0] == "-n":
        n = args[1]

for i in range(int(n)):
    if os.fork() == 0:
        print("Soy el proceso", os.getpid(), "Mi padre es,", os.getppid())
        break

time.sleep(0.1)
