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

    def connect(self, device):
        self.__connector.connect(device)

    def read_ammeter_value(self, func_read_value):
        return self.__connector.read_value_gatt(func_read_value, AmmeterConnector.AMMETER_VALUE_UID)
