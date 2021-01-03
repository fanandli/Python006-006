import socket

#example
HOST = 'localhost'
PORT=10000

def file_deal(file_name):
    try:
        files = open(file_name, "rb")
        content = files.read()
    except:
        print("no such file.")
    else:
        files.close()
        return content

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST,PORT))
    tcp_socket.listen(128)

    while True:
        client_socket,client_addr = tcp_socket.accept()
        file_name = client_socket.recv(4096)
        content = file_deal(file_name)

        if content:
            client_socket.send(content)
        client_socket.close()

if __name__ == "__main__":
    main()