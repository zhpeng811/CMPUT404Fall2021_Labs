#!/usr/bin/env python3
import socket
import time 
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_echo(addr, conn):
    print(f"Connected by {addr}")

    data = conn.recv(BUFFER_SIZE)
    conn.sendall(data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

if __name__ == "__main__":
    main()