from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

influx_client = InfluxDBClient(url="http://127.0.0.1:8086", token="HDt88lLdX0RSWI9YuJXp8J5rwN6SDMCk391l6cqIfOJZzb6o7WgTcODDlh1pGPXuOxXOeQOWojb3xETRkgffag==")
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

point: Point = Point("ampere_measurement").field("ampere", 10.0)
write_api.write("igem_bucket", "Ionis_paris", point)