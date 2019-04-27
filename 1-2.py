import RPi.GPIO as GPIO

led = 18
btn = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        value = GPIO.input(btn)
        if(value):
            GPIO.output(led, True)
        else:
            GPIO.output(led, False)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
