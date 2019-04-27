import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin=18

h, t = Adafruit_DHT.read_retry(sensor, pin)
if h is not None and t is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
else:
    print('Fail')
