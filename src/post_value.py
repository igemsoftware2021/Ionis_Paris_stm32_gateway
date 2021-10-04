from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


def main():
    print("Post one value inside InfluxDB")
    value = 70.0
    # You can generate a Token from the "Tokens Tab" in the UI
    token = "6iEQA6KT_6Ohr9zIONLcA-3NRZ-TMe7VrLr2Dt4EljLObtY4eXVvnOmMnOnbX3iiZKn6me99_qAyNyjRBvrp3w=="
    org = "Ionis_paris"
    bucket = "igem_bucket"

    client = InfluxDBClient(url="http://127.0.0.1:8086", token=token)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    point = Point("ampere_measurement") \
        .field("ampere", value)

    write_api.write(bucket, org, point)


if __name__ == "__main__":
    main()
