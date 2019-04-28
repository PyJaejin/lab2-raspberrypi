#!/usr/bin/python3
import RPi.GPIO as GPIO
import cgi, cgitb

led = 17
btn = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

status = False
btn_status = False
form = cgi.FieldStorage()

if not None == form.getvalue('on'):
    status = True
    GPIO.output(led, 1)
    
elif not None == form.getvalue('off'):
    status = False
    GPIO.output(led, 0)

elif not None == form.getvalue('btn_on'):
    btn_status = True
    GPIO.output(led, 1)

    
elif not None == form.getvalue('btn_off'):
    btn_status = False
    GPIO.output(led, 0)

#
#
#form = cgi.FieldStorage()
#status = form.getvalue('on')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Test</title>")
print("</head>")
print("<body>")
print("<H2>LED : %s</H2>" % (status))
print("<H2>PushButton : %s</H2>" % (btn_status))
print("</body>")
print("</html>")
