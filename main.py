import RPi.GPIO as gpio
import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 57600, timeout=1)

if not ser.is_open:
    ser.open()

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

# Send start command to put roomba in passive mode.
#print("Sending start command.")
#ser.write(bytes(128))
#time.sleep(0.1)

# Get roomba sensor data
print("Requesting sensor data.")
ser.write(bytes([142,0]))
sensors = ser.read()
time.sleep(2)

print(sensors)

time.sleep(5)

# Cleanup
ser.close()
gpio.cleanup()
