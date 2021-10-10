import logging

from gateway.gateway_ammeter_influx import GatewayAmmeterInflux

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Gateway Ammeter Influx')


def main():
    logger.info('STARTING AMMETER INFLUX')
    # declare gateway and influxdb (also connect it to stm32)
    gateway_ammeter_influx = GatewayAmmeterInflux(
        "STM32IONIS",
        "http://127.0.0.1:8086",
        "6iEQA6KT_6Ohr9zIONLcA-3NRZ-TMe7VrLr2Dt4EljLObtY4eXVvnOmMnOnbX3iiZKn6me99_qAyNyjRBvrp3w==",
        "Ionis_paris",
        "igem_bucket"
    )
    # gateway forever
    gateway_ammeter_influx.read_ammeter_into_influx_forever()


if __name__ == '__main__':
    main()
