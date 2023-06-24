import asyncio


class ChatServer:
    def __init__(
        self,
        server_name,
        port,
    ):
        self.server_name = server_name
        self.connections = {}
        self.server = asyncio.streams.start_server(
            self.accept_connection,
            "",
            port,
        )

    def broadcast(self, message):
        for reader, writer in self.connections.values():
            writer.write((message + "\n").encode("utf-8"))

    async def prompt_username(self, reader, writer):
        while True:
            writer.write("Enter username: ".encode("utf-8"))
            data = (await reader.readline()).decode("utf-8")
            if not data:
                return None
            username = data.strip()
            if username and username not in self.connections:
                self.connections[username] = (reader, writer)
                return username
            writer.write("Sorry, that username is taken.\n".encode("utf-8"))

    async def handle_connection(self, username, reader):
        while True:
            data = (await reader.readline()).decode("utf-8")
            if not data:
                del self.connections[username]
                return None
            self.broadcast(username + ": " + data.strip())

    async def accept_connection(self, reader, writer):
        writer.write(("Welcome to " + self.server_name + "\n").encode("utf-8"))
        username = await self.prompt_username(reader, writer)
        if username is not None:
            self.broadcast("User %r has joined the room" % (username,))
            await self.handle_connection(username, reader)
            self.broadcast("User %r has left the room" % (username,))
        await writer.drain()


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    finally:
        loop.close()


main()
