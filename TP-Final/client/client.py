#!/usr/bin/python3

import getopt
import sys
import socket
import time


def download_file(host, port, filename):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(f"DOWNLOAD {filename}".encode())

        response = client_socket.recv(1024)
        if response.startswith(b"ERROR"):
            print(response.decode())
        else:
            with open(filename, "wb") as file:
                while response:
                    file.write(response)
                    response = client_socket.recv(1024)
            print("\nFile downloaded successfully.\n")
    except ConnectionRefusedError:
        print("\nERROR: Connection refused.\n")

    client_socket.close()

def upload_file(host, port, filename):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(f"UPLOAD {filename}".encode())
        response = client_socket.recv(1024)
        time.sleep(0.5)
        if response == b'ready':
            with open(filename, "rb") as file:
                file_data = file.read(1024)
                # print("file_data: ", file_data)
                # while file_data:
                client_socket.sendall(file_data)
                # print("After client_socket")
                # file_data = file.read(1024)
                # print("file_data: ", file_data)

        print("\nFile uploaded successfully.\n")
    except ConnectionRefusedError:
        print("\nERROR: Connection refused.\n")

    client_socket.close()
    print("Connection closed successfully")

def list_files(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(b"LIST")

        file_list = client_socket.recv(1024).decode()
        if file_list:
            print(file_list)
        else:
            print("No files to download.")
    except ConnectionRefusedError:
        print("ERROR: Connection refused.")

def list_downloading_files(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(b"LIST_UNAVAILABLE_FILES")

        file_list = client_socket.recv(1024).decode()
        if file_list:
            print(file_list)
        else:
            print("No files in progress!\n")
    except ConnectionRefusedError:
        print("ERROR: Connection refused.")

    client_socket.close()


if __name__ == "__main__":
    host = "localhost"
    port = 8080

    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:h:')
    for args in opt:
        if args[0] == '-h':
            host = args[1]
        if args[0] == '-p':
            port = int(args[1])

    while True:
        print("1. Download file")
        print("2. Upload file")
        print("3. List files available")
        print("4. List files not available")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("\nEnter filename to download: ")
            download_file(host, port, filename)
        elif choice == "2":
            filename = input("\nEnter filename to upload: ")
            upload_file(host, port, filename)
        elif choice == "3":
            # print("Available files to download:")
            list_files(host, port)
        elif choice == "4":
            print("\nUnavailable files:")
            list_downloading_files(host, port)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
