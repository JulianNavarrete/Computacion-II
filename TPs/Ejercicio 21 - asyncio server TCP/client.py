#!/usr/bin/python3
import asyncio
import socket
import sys
import getopt
from datetime import datetime as dt


async def main():
    host = "localhost"
    port = 8000
    log_file = ""

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'l:')
        for args in opt:
            if args[0] == '-l':
                log_file = args[1]
    except:
        print("Error de parámetros.")

    r, w = await asyncio.open_connection(host, port)
    print("-----------Command Prompt-----------\n")
    msg = input("> ")
    if msg != "exit":
        w.write(msg.encode('utf-8'))
        await w.drain()
        msg = await r.read(29)
        print(msg.decode('utf-8'))
        if log_file != "":
            with open(log_file, "a") as file:
                td = dt.today()
                file.writelines("\n" + str(td) + msg.decode('utf-8'))

    else:
        w.write("exit".encode('utf-8'))
        await w.wait_closed()
        print("\nCerrando conexión...")


asyncio.run(main())
