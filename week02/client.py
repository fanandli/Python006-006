from socket import *
import os

#example
HOST = 'localhost'
PORT=10000

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect((HOST,PORT))

    file_name = input("please input file name:")
    tcp_socket.send(file_name.encode())
    new_file = open(file_name, "wb")
    filesize = 0

    while True:
        data = tcp_socket.recv(4096)
        if data:
            new_file.write(data.decode())
            filesize += len(data)
        else:
            if filesize == 0:
                new_file.close()
                os.remove(file_name)
                print("no such file.")
            else:
                print("download successfully.")
            break
    tcp_socket.close()

if __name__ == '__main__':
    main()