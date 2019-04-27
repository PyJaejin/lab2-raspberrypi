import serial

ser = serial.Serial('/dev/ttyS0', 9600)

while True:
    text = str(input("input : "))
    ser.write(text.encode())
