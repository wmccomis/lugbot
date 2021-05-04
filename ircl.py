#!/usr/bin/python3

import asyncio
import os
import sys

# Constants

HOST = 'chat.ndlug.org'
PORT = 6697
# NICK = f'ircle-{os.environ["USER"]}'
NICK = 'yaboi'
TARGET = 'pnutzh4x0r'

# Functions

async def ircle():
    reader, writer = await asyncio.open_connection(HOST, PORT, ssl=True)

    # Identify ourselves
    writer.write(f'USER {NICK} 0 * :{NICK}\r\n'.encode())
    writer.write(f'NICK {NICK}\r\n'.encode())
    await writer.drain()

    # Join #bots channel
    writer.write(f'JOIN #bots\r\n'.encode())
    await writer.drain()

    # Read and display
    messageval = 0
    joecount = 0
    while True:
        message = (await reader.readline()).decode().strip()
        print(message)
        # if ' ' in message:

        if f'{TARGET}' in message:
            messageval += 1
        if f'{TARGET}' in message and messageval > 2:
            writer.write(f"PRIVMSG #bots :hoes mad\r\n".encode())
            await writer.drain()
        # if "Joe" or "joe" in message:
        #     writer.write(f"PRIVMSG #bots :joe mama\r\n".encode())
        #     await writer.drain()
        if f'PING {NICK}' in message:
            writer.write(bytes(f'PONG {NICK}\r\n', "UTF-8"))
            await writer.drain()

# Main execution

def main():
    asyncio.run(ircle())

if __name__ == '__main__':
    main()