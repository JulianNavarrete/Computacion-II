#!/usr/bin/python3

import socket
import socketserver
import subprocess
import multiprocessing
import threading
import sys
import getopt


class MyTCPHandler(socketserver.BaseRequestHandler):

    # @staticmethod
    def child(self, cs, a):
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
                s.close()
                print("Conexión cerrada", a)
                break


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

    addres = (host, port)

    if multi == "p":

        class ForkingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer, ):
            pass

        # server = ForkingTCPServer(addres, MyTCPHandler)
        socketserver.TCPServer.allow_reuse_address = True
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            with ForkingTCPServer((host, port), MyTCPHandler) as server:
                # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # s.bind((host, int(port)))
                server.serve_forever()
                print("Esperando conexiones...")
                # clientsocket, addr = server.accept()
                # print("Tengo una conexión de", str(addr))
                # server_fork = multiprocessing.Process(target=server.serve_forever)

                # server_fork.daemon = True
                # server_fork.start()
                server_fork = multiprocessing.Process(target=MyTCPHandler.child, args=(clientsocket, addr))
                server_fork.start()

                # server_fork = multiprocessing.Process(target=server.serve_forever)

                # server_fork.daemon = True
                # server_fork.start()
                # server.shutdown()
                server.handle_request()
                #        server.serve_forever()
                server.shutdown()

    elif multi == "t":
        class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
            pass
    else:
        print("Parámetro -m incorrecto.")


    # server_fork = multiprocessing.Process(target=server.serve_forever)

    # server_fork.daemon = True
    # server_fork.start()
    # server.shutdown()
    server.handle_request()
    #        server.serve_forever()
    server.shutdown()