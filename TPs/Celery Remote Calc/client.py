#!/usr/bin/python3

from sys import argv
from getopt import getopt


(opt, arg) = getopt(argv[1:], 'h:p:o:n:m:')
for args in opt:
    if args[0] == '-h':
        host = args[1]
    elif args[0] == '-p':
        port = int(args[1])
    elif args[0] == '-o':
        operation = args[1]
    elif args[0] == '-n':
        num1 = args[1]
    elif args[0] == '-m':
        num2 = args[1]
    else:
        print("Error de parámetros.")
