import asyncio
from bleak import BleakScanner
address = ""
async def run():
    devices = await BleakScanner.discover()
    address = "---"
    for d in devices:
        #print(d)
        if d.name == "STM32IONIS":
            address = d.address
    return address

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
