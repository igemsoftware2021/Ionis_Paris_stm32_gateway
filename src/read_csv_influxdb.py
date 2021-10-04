import csv
import os

from influxdb_client import InfluxDBClient


def main():
    print("Read value from influxdb")

    # You can generate a Token from the "Tokens Tab" in the UI
    token = ""  # ton token pour la conf
    org = "influxdata"
    bucket = "default"

    client = InfluxDBClient(url="http://127.0.0.1:8086", token=token, org=org)
    query_api = client.query_api()

    query = f'from(bucket: "default") |> range(start: -1h) |> filter(fn: (r) => r._measurement == ' \
            f'"ampere_measurement" and r._field == "ampere") '
    csv_result = query_api.query_csv(query)

    # compute place for storing ampere.csv
    script_path = os.path.join(os.getcwd(), 'ampere.csv')

    # writer csv
    with open(script_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in csv_result:
            writer.writerow(row)


if __name__ == "__main__":
    main()
