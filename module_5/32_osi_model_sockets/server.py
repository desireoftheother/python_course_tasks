import socket

HOST = "127.0.0.1" #This should be the PRIVATE IP of the server
PORT = 65436

sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(1)

# Uncomment to mack socket unblocking later
sock.setblocking(False)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data.upper())

