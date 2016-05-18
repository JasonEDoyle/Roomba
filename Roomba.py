import RPi.GPIO as GPIO
import serial
import time

class Roomba:
    def __init__(self, port='/dev/ttyAMA0', baudrate=57600, DD_pin):
        self.port = port
        self.baudrate = baudrate
        self.DD_pin = DD_pin

        ser = serial.Serial(port, baudrate, timeout = 0.1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DD_pin, GPIO.OUT)

    def wake_roomha(self):
        GPIO.output(DD_pin, 0)
        time.sleep(0.1)
        GPIO.output(DD_pin, 1)
        time.sleep(2)
 
    def start(self):
        ser.write(bytes([128]))

    def sensors(self):
        ser.write(bytes([132,1]))

    def shutdown(self):
        ser.close()
        GPIO.cleanup()

