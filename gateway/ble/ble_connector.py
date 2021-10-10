import asyncio
import logging
import time
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
        self.__is_running = False

    def connect(self, device_name="STM32IONIS"):
        """
        find and connect with device
        :return: void
        """
        self.__find_device(device_name)
        # connect with bleak client
        self.__logger.info("You are connected to our device")
        self.__is_connect = True
        self.__is_running = True

    async def __read_value_gatt(self, func_value_read, characteristics_uid):
        """
        Read value from connected board
        :param characteristics_uid: uid of value
        :return: value of resource
        """
        if self.__is_connect:
            async with BleakClient(self.__address) as client:
                while self.__is_running:
                    func_value_read(
                        await client.read_gatt_char(
                            BLEConnector.CHARACTERISTICS_DEFAULT_UID.format(characteristics_uid)
                        )
                    )
                    time.sleep(1)
        raise NoConnectedDevice("Can't read value because not device connected")

    def read_value_gatt(self, func_value_read, characteristics_uid):
        loop = asyncio.get_event_loop()
        # disconnect ble from device
        loop.run_until_complete(self.__read_value_gatt(func_value_read, characteristics_uid))

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
        device_found = await BleakScanner.find_device_by_filter(
            lambda device, ad: device.name and device.name == device_name
        )
        if device_found is not None:
            self.__address = device_found.address
        else:
            self.__logger.info("No device found, retry...")
