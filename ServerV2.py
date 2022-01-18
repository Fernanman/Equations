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
        print('Current players:', players)
        print('Connected by', addr)

        while True:
            data = pickle.loads(conn.recv(2048))
            print("Received:", data, "\nSending:", data[::-1])
            conn.sendall(pickle.dumps(data[::-1]))
            
print("Ready to accept Connections.")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    start_new_thread(ConnectPlayer(s, conn, players))
