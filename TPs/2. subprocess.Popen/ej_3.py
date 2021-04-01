#!/usr/bin/python3

from subprocess import Popen, PIPE
import getopt
import sys
import time

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')

    command = ""
    outFile = ""
    logFile = ""

    for args in opt:
        if args[0] == "-c":
            command = args[1]
        elif args[0] == "-f":
            outFile = args[1]
        elif args[0] == "-l":
            logFile = args[1]
        else:
            print("Error de parámetros.")
            exit()

    try:
        process = Popen(command.split(), stdout=PIPE, stderr=PIPE)
        output = process.communicate()
        stdout = output[0]
        stderr = output[1]

        output_file = open(outFile, "a")
        log_file = open(logFile, "a")

        if stdout.decode() != "":
            output_file.write(stdout.decode() + "\n")
            output_file.close()
            log_file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") +
                           ": Comando " + '"' + command + '"' + " ejecutado correctamente." + "\n")

        else:
            log_file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + ": " + stderr.decode() + "\n")

    except Exception as e:
        log_file = open(logFile, "a")
        log_file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + ": " + str(e) + "\n")
        log_file.close()

except Exception as e:
    print("Error de parámetros:", e)
