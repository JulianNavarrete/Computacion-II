#!/usr/bin/python

import sys
import getopt

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:m:o:')
    num1 = 0
    num2 = 0
    operator = ""
    readyNum1 = bool
    readyNum2 = bool
    readyOperator = bool
    for (op, ar) in opt:
        if op == '-n':
            try:
                if int(ar):
                    print("Opción -n seteada, argumento:", ar)
                    num1 = ar
                    readyNum1 = True
            except:
                print("El valor ingresado para el argumento " + '"' + "-n" + '"' + " no es válido.")
        elif op == '-m':
            try:
                if int(ar):
                    print("Opción -m seteada, argumento:", ar)
                    num2 = ar
                    readyNum2 = True
            except:
                print("El valor ingresado para el argumento " + '"' + "-m" + '"' + " no es válido.")
        elif op == '-o':
            if ar == "+" or ar == "-" or ar == "x" or ar == "/":
                print("Opción -o seteada, operador:", ar)
                operator = ar
                readyOperator = True
            else:
                print("El operador no es válido.")

    if readyNum1 == True and readyNum2 == True and readyOperator == True:
        if operator == "+":
            result = int(num1) + int(num2)
            print("El resultado de la operación " + '"' + str(num1) + " + " + str(num2) + '"' + " es: " + str(result))
        elif operator == "-":
            result = int(num1) - int(num2)
            print("El resultado de la operación " + '"' + str(num1) + " - " + str(num2) + '"' + " es: " + str(result))
        elif operator == "x":
            result = int(num1) * int(num2)
            print("El resultado de la operación " + '"' + str(num1) + " x " + str(num2) + '"' + " es: " + str(result))
        else:
            result = int(num1) / int(num2)
            print("El resultado de la operación " + '"' + str(num1) + "/" + str(num2) + '"' + " es: " + str(result))

except:
    print("Las opciones " + "-n, " + "-m" + " y/o " + "-o" + " no son válidas.")
