#!/usr/bin/python

import sys
import getopt

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')
    file_i = ""
    file_o = ""
    for args in opt:
        if args[0] == '-i':
            file_i = args[1]
        elif args[0] == '-o':
            file_o = args[1]
        else:
            print("Error de parámetros.")

    try:
        file_i = open(file_i, "r")
        file_content = file_i.readlines()
        open(file_o, "w").writelines(file_content)
        print("Archivo copiado con éxito.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

    except Exception as e:
        print(e)

except Exception as e:
    print("Se ha producido un error de parámetros:", e)
