#!/usr/bin/python3


import socket
import socketserver
import subprocess
import threading
import sys
import getopt


class MyTCPHandler(socketserver.BaseRequestHandler):

    # @staticmethod
    def child(self, cs, a):
        sock, addr = cs
        while True:
            msg = cs.recv(1024).decode('utf-8')
            if msg != "exit":
                res = subprocess.Popen([msg], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                std_out, std_err = res.communicate()
                if std_out != "":
                    msg = "\nOK\n" + std_out
                if std_err != "":
                    msg = "\nERROR\n" + std_err

                cs.send(msg.encode('utf-8'))

            else:
                cs.close()
                # s.close()
                print("Conexión cerrada", a)
                break


'''
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
'''


if __name__ == '__main__':
    host = "localhost"
    port = 8000
    multi = ""

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'm:')
        for args in opt:
            if args[0] == '-m':
                multi = args[1]
    except:
        print("Error de parámetros.")

    addr = (host, port)

    if multi == "p":

        class ForkingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer, ):
            pass

        server = ForkingTCPServer(addr, MyTCPHandler)

    elif multi == "t":

        class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
            pass

        server = ThreadingTCPServer(addr, MyTCPHandler)

    else:
        print("Parámetro -m incorrecto.")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente = s.accept()
    thread = threading.Thread(target=server.serve_forever, args=(cliente,))
    thread.setDaemon(True)
    thread.start()
    ip, port = ('localhost', 0)
    s.connect((ip, port))
    sock, addr = cliente

    while True:
        msg = input("Ingrese un mensaje: ")
        s.send(msg.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        if msg == 'exit':
            server.shutdown()
            s.close()
            server.socket.close()
