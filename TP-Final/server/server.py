#!/usr/bin/python3

import getopt
import sys
import socket
import threading
import os


def handle_client(client_socket, client_address, files_in_progress, client_lock):
    request = client_socket.recv(1024).decode()
    if request.startswith("DOWNLOAD"):
        filename = request.split()[1]
        if not is_file_in_progress(filename, files_in_progress):
            start_file_download(client_socket, filename, files_in_progress)
        else:
            client_socket.sendall(b"ERROR: File download in progress.")
    elif request.startswith("UPLOAD"):
        # print("request: %s" % request)
        filename = request.split()[1]
        # print("filename: ", filename)
        if not is_file_in_progress(filename, files_in_progress):
            start_file_upload(client_socket, filename, files_in_progress)
        else:
            client_socket.sendall(b"ERROR: File upload in progress.")
    elif request == "LIST_UNAVAILABLE_FILES":
        files_list = get_downloading_files_list(files_in_progress)
        client_socket.sendall(files_list.encode())
    elif request == "LIST":
        files_list = get_files_list()
        client_socket.sendall(files_list.encode())
    else:
        client_socket.sendall(b"ERROR: Invalid command.")
    
    client_socket.close()

def is_file_in_progress(filename, files_in_progress):
    return filename in files_in_progress

def start_file_download(client_socket, filename, files_in_progress):
    files_in_progress.add(filename)
    file_path = os.getcwd() + "/files/" + filename
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            client_socket.sendall(file_data)
    except FileNotFoundError:
        client_socket.sendall(b"ERROR: File not found.")
    except:
        client_socket.sendall(b"ERROR: An error occurred while downloading the file.")
    finally:
        files_in_progress.remove(filename)

def start_file_upload(client_socket, filename, files_in_progress):
    files_in_progress.add(filename)
    file_path = os.getcwd() + "/files/" + filename
    # print("file_path: ", file_path)
    try:
        # print("Before client_socket.send")
        client_socket.sendall(b'ready')
        # print("After client_socket.send, before data")
        file_data = client_socket.recv(1024)
        # print("file_data: ", file_data)
        with open(file_path, "wb") as file:
            while file_data:
                file.write(file_data)
                file_data = client_socket.recv(1024)
    except:
        client_socket.sendall(b"ERROR: An error occurred while uploading the file.")
    finally:
        files_in_progress.remove(filename)

def get_downloading_files_list(files_in_progress):
    files_list = ""
    if files_in_progress:
        files_list += "\nFiles in progress:\n"
        files_list += "\n".join(files_in_progress)
        files_list += "\n"
    return files_list

def get_files_list():
    files_list = ""
    files = os.listdir(os.getcwd() + "/files")
    files_list += "\nFiles available:\n"
    files_list += "\n".join(files)
    files_list += "\n"
    return files_list

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP connection
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    files_in_progress = set()
    client_lock = threading.Lock()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        threading.Thread(target=handle_client, args=(client_socket, client_address, files_in_progress, client_lock)).start()


if __name__ == "__main__":
    host = "localhost"
    port = 8080

    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:h:')
    for args in opt:
        if args[0] == '-h':
            host = args[1]
        if args[0] == '-p':
            port = int(args[1])
            
    start_server(host, port)

