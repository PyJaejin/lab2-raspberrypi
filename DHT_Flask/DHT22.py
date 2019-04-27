import Adafruit_DHT

def get_DHT():
    sensor = Adafruit_DHT.DHT22
    pin=18

    h, t = Adafruit_DHT.read_retry(sensor, pin)
    if h is not None and t is not None:
        return (h, t)
    else:
        print('Fail')
