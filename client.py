import asyncio

async def handle_connection():
    HOST = "localhost"
    PORT = 8000

    reader, writer = await asyncio.open_connection(HOST, PORT)

    while True:
        data = input("Type the message to send:")
        print("Input data: ", data)

        if data == b"close":
            break

        data = data.upper()
        data_bytes = data.encode()

        writer.write(data.encode())
        await writer.drain()

        data_bytes = await reader.read(1024)
        recv_data = data_bytes.decode()

        print("Received: ", recv_data)

        if not recv_data:
            print("Closed by server")
            break

    print("Closed by server2")
    writer.close()
    await writer.wait_closed()

async def main():
    await handle_connection()

if __name__ == "__main__":
    asyncio.run(main())

