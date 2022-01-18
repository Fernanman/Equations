import socket
from _thread import *
import pickle

HOST = ''
PORT = 65432

global players
players = 0

def ConnectPlayer(socket, conn, players):
    players += 1

    with conn:
        print('Connected by', addr)

        while True:
            data = conn.recv(1024)
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    start_new_thread(ConnectPlayer(s, conn, players))
