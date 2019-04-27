import RPi.GPIO as GPIO
from time import sleep

btn = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN)
#GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        value = GPIO.input(btn)
        print(value)
        sleep(0.1)

        
    except KeyboardInterrupt:
        GPIO.cleanup()
