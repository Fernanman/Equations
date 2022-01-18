import socket

HOST = "66.228.47.180"
PORT = 65432

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        x = input()
        s.sendall(x)
        data = s.recv(1024)

        print('Recieved', repr(data))
