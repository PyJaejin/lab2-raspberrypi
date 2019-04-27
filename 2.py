import RPi.GPIO as GPIO

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm_led = GPIO.PWM(led, 100)
pwm_led.start(0)

while True:
    try:
        duty = int(input("input(0 to 100) : "))
        if(duty > 100):
            print("please input number under 100")
            continue
        elif(duty == -1):
            exit(0)
        pwm_led.ChangeDutyCycle(duty)
    except KeyboardInterrupt:
        GPIO.cleanup()

