import socket

HOST = "127.0.0.1" #This should be the PUBLIC IP of the server
PORT = 65436

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        inp = bytes(input(), "utf-8")
        s.sendall(inp)
        data = s.recv(1024)
        print("received", repr(data))
