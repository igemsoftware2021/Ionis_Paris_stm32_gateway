import asyncio
import atexit
import logging
from typing import List

from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice

from gateway.ble.no_connected_device import NoConnectedDevice


class BLEConnector:
    """
    BLE Connector
    """
    CHARACTERISTICS_DEFAULT_UID = "0000{}-0000-1000-8000-00805F9B34FB"

    def __init__(self):
        self.__logger = logging.getLogger("BLEConnector")
        self.__address = None

        self.__client = None
        self.__is_connect = False

        atexit.register(self.__destroy)

    async def connect(self, device_name="STM32IONIS"):
        """
        find and connect with device
        :return: void
        """
        self.__find_device(device_name)
        # connect with bleak client
        self.__client = BleakClient(self.__address)
        self.__logger.info("You are connected to our device")
        self.__is_connect = True

    async def read_value_gatt(self, characteristics_uid="A000"):
        """
        Read value from connected board
        :param characteristics_uid: uid of value
        :return: value of resource
        """
        if self.__is_connect:
            return await self.__client.read_gatt_char(BLEConnector.CHARACTERISTICS_DEFAULT_UID.format(characteristics_uid))

        raise NoConnectedDevice("Can't read value because not device connected")

    def __destroy(self):
        loop = asyncio.get_event_loop()
        # disconnect ble from device
        loop.run_until_complete(self.__disconnect())

    async def __disconnect(self):
        """
        disconnect from device
        :return:
        """
        if self.__is_connect:
            self.__logger.info("Disconnect BLE Client")
            await self.__client.disconnect()

    def __find_device(self, device_name):
        """
        find device to connect with
        :return:
        """
        self.__logger.info("Try to find device...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__find_devices_address(device_name))

    async def __find_devices_address(self, device_name):
        """
        helper for finding BLE Device (Cant be called directly)
        :return:
        """
        devices: List[BLEDevice] = await BleakScanner.discover()
        for device in devices:
            if device.name == device_name:
                self.__address = device.address
                return
        self.__logger.info("No device found, retry...")
        await self.__find_devices_address(device_name)
