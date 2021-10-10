from gateway.ble.ble_connector import BLEConnector
import logging


class AmmeterConnector:
    """
    Ammeter connector
    """
    AMMETER_VALUE_UID = "A001"

    def __init__(self, connector: BLEConnector):
        self.__logger = logging.getLogger("AmmeterConnector")
        self.__connector: BLEConnector = connector

    async def connect(self, device):
        await self.__connector.connect(device)

    async def read_ammeter_value(self):
        return await self.__connector.read_value_gatt(AmmeterConnector.AMMETER_VALUE_UID)
