import asyncio
from base64 import b64encode
from datetime import datetime
from urllib import request
import requests

from messaging import (
    parse_inverter_message
)

HOST = "127.0.0.1"
PORT = 9999
SERVER_IP = "http://200.126.13.223:3030/api/sensorPanelSolar"

async def _read_and_log_response(reader, writer):
    buffer_size = 1024
    data = await reader.read(buffer_size)
    
    return data


async def log_and_forward_response(reader, writer):
    data = await _read_and_log_response(reader, writer)
    writer.write(data)
    await writer.drain()
    if(len(data) == 244):
        inverter_data = parse_inverter_message(data)
        print(inverter_data)
        requests.post(SERVER_IP, json=inverter_data)


async def handle_inverter_message(inverter_reader, inverter_writer):
    server_reader, server_writer = await asyncio.open_connection('47.88.8.200', 10000)
    await log_and_forward_response(inverter_reader, server_writer)
    await log_and_forward_response(server_reader, inverter_writer)
    server_writer.close()
    inverter_writer.close()


async def main():
    server = await asyncio.start_server(handle_inverter_message,
            HOST, PORT)

    print(f"serving on {server.sockets[0].getsockname()}")

    async with server:
        await server.serve_forever()


asyncio.run(main())
