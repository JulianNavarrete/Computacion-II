#!/usr/bin/python3

import socket
import sys
import getopt

host = "localhost"
port = 2222

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:h:')
    for args in opt:
        if args[0] == '-p':
            port = args[1]
        if args[0] == '-h':
            host = args[1]

except:
    print("Error de parámetros.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))

exit_nombre = False
exit_correo = False
exit_pass = False

# Check nombre
while not exit_nombre:
    nombre = "hello|" + input("Introduzca su nombre: ")
    s.send(nombre.encode('utf-8'))
    resp_server = s.recv(1024).decode('utf-8')
    if resp_server == "200":
        print("¡Nombre seteado con éxito! Código", resp_server + ".\n")
        exit_nombre = True
    else:
        print("Nombre no válido, código de error", resp_server + ".\n")

# Check email
while not exit_correo:
    correo = "email|" + input("Introduzca su correo: ")
    s.send(correo.encode('utf-8'))
    resp_server = s.recv(1024).decode('utf-8')
    if resp_server == "200":
        print("¡Correo seteado con éxito! Código", resp_server + ".\n")
        exit_correo = True
    else:
        print("Correo no válido, código de error", resp_server + ".\n")

# Check password
while not exit_pass:
    password = "key|" + input("Introduzca su contraseña: ")
    s.send(password.encode('utf-8'))
    resp_server = s.recv(1024).decode('utf-8')
    if resp_server == "200":
        print("¡Contraseña seteada con éxito! Código", resp_server + ".\n")
        exit_pass = True
    else:
        print("Contraseña no válida, código de error", resp_server + ".\n")


print("Datos seteados exitosamente, enviando", '"' + "exit" + '"', "al servidor...")
s.send("exit".encode('utf-8'))
print("Cerrando conexión...")
s.close()
