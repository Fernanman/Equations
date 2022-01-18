import socket
import pickle

HOST = "66.228.47.180"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        x = input()
        s.sendall(pickle.dumps(x))
        data = pickle.loads(s.recv(2048))

        print('Recieved', data)
