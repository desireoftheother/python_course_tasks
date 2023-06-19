import socket
import json

HOST = "127.0.0.1" #This should be the PRIVATE IP of the server
PORT = 65438

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            key = None
            message = None
            if not key:
                key = conn.recv(1024)
            if not message:
                message = conn.recv(1024)
            # cypher
            conn.sendall(cypher_result)
            if key and message:
                key = None
                message = None

