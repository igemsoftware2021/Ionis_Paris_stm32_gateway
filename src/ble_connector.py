import asyncio
import time

from bleak import BleakClient
from bleak.exc import BleakError
from bleak import BleakScanner

MODEL_NBR_UUID = "0000A001-0000-1000-8000-00805F9B34FB"


async def run(address):
    while True:
        try:
            async with BleakClient(address) as client:
                while True:
                    model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                    print(model_number)
                    time.sleep(1)

        except BleakError as error:
            print(error)

async def get_address():
    devices = await BleakScanner.discover()
    for device in devices:
        if d.name == "STM32IONIS":
            return d.address
    return ""

address = ""
while address == "" :
    loop = asyncio.get_event_loop()
    address = loop.run_until_complete(get_address())

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
