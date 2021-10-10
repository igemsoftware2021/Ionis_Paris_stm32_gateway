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
        "ceE9SpBrY9MfaslDFycbinx_b4bypMFPCEXba8i9pmoIef6_oRhufUPfE2kIDWqFh1GtuJqMC_5AsXOb2MHe7Q==",
        "Ionis_paris",
        "igem_bucket"
    )
    # gateway forever
    gateway_ammeter_influx.read_ammeter_into_influx_forever()


if __name__ == '__main__':
    main()
