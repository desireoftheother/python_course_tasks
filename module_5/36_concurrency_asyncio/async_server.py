import asyncio
import socket

HOST = "127.0.0.1"
PORT = 65435

sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(1)

sock.setblocking(False)


async def handle_connection(conn):
    loop = asyncio.get_event_loop()
    while True:
        data = await loop.sock_recv(conn, 1024)
        print(data)
        if data:
            await loop.sock_sendall(conn, data)


async def main():
    while True:
        loop = asyncio.get_event_loop()
        conn, addr = await loop.sock_accept(sock)
        loop.create_task(handle_connection(conn))
        print("connected: ", addr, "spawned new coroutine")

asyncio.run(main())
