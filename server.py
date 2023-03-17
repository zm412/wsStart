import asyncio
from calculate_factorial import get_factorial

async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print("Connected by", addr)

    while True:
        data = await reader.read(1024)
        print(f"Received data {data} from: {addr}")
        message = data.decode()

        if not data:
            break

        if data == b"close":
            break

        try:
            num = int(message)
            fac = await get_factorial(num)
            print(f"Received {num} from: {addr}")
        except ValueError:
            fac = 'Not a number'
            print(f"Received {fac} from: {addr}")

        data = data.upper()

        strData = str(fac)
        writer.write(strData.encode())

        await writer.drain()

    writer.close()
    await writer.wait_closed()

    print("Disconnected by", addr)

async def main():
    HOST = "localhost"
    PORT = 8000

    server = await asyncio.start_server(handle_connection, HOST, PORT)
    print("Start server...")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
