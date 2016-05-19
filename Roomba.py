import RPi.GPIO as GPIO
import serial
import time

class Roomba:
    def __init__(self, port = '/dev/ttyAMA0', baudrate = 57600, DD_pin = 17):
        self.port = port
        self.baudrate = baudrate
        self.DD_pin = DD_pin

        self.ser = serial.Serial(port, baudrate, timeout = 0.1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DD_pin, GPIO.OUT)

    def wake_roomba(self):
        GPIO.output(self.DD_pin, 0)
        time.sleep(0.1)
        GPIO.output(self.DD_pin, 1)
        time.sleep(2)
 
    def start(self):
        self.ser.write(bytes([128]))
        time.sleep(0.02)

    def sensors(self):
        self.ser.flushInput()

        self.ser.write(bytes([142,0]))


#        sensors = []
        sensors = self.ser.read(26)

        return sensors

    def shutdown(self):
        self.ser.close()
        GPIO.cleanup()

