"""
MAIN THREAD
Handles all the connections, creating new games and
request from the client
"""

import socket
import threading
import time
from .player import Player
from .game import Game
from queue import Queue

def player_thread(ip):
    pass

def connection_thread():
    server = ""
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen()
    print("Waiting for the connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("[CONNECT] New connection!")

        threading.Thread(target= player_thread, args=(addr,))


if __name__ == "__main__":
    connection_thread()
