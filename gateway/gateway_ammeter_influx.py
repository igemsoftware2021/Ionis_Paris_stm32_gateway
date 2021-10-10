import time

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from gateway.ammeter_ble.ammeter_connector import AmmeterConnector
from gateway.ble.ble_connector import BLEConnector

import logging


class GatewayAmmeterInflux:
    def __init__(self, device_name, influx_db_url, token, org, bucket):
        self.__logger = logging.getLogger("GatewayAmmeterInflux")
        # init influxdb client
        self.__influx_client = InfluxDBClient(url=influx_db_url, token=token)
        self.__write_api = self.__influx_client.write_api(write_options=SYNCHRONOUS)
        self.__org = org
        self.__bucket = bucket
        # init ammeter connector
        self.__ammeter_connector = AmmeterConnector(BLEConnector())
        self.__ammeter_connector.connect(device_name)

    def read_ammeter_into_influx_forever(self):
        self.__ammeter_connector.read_ammeter_value(self.__post_ammeter_in_influx)

    def __post_ammeter_in_influx(self, ammeter):
        point: Point = Point("ampere_measurement").field("ampere", ammeter)
        self.__write_api.write(self.__bucket, self.__org, point)
