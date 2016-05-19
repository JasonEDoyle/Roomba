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
        time.sleep(0.05)


    def sensors(self):
        self.ser.flushInput()

        self.ser.write(bytes([142,0]))

#        sensors = []
        sensors = self.ser.read(26)

        return sensors


    def control(self):
        # puts roomba into safe mode. start command must be sent first
        self.ser.write(bytes([130]))
        time.sleep(0.02)

    def spot(self):
        # Tells the roomba to spot clean.
        self.ser.write(bytes([134]))


    def power_down(self):
        # posers off roomba must be in safe or full mode
        self.ser.write(bytes([133]))


    def shutdown(self):
        self.ser.close()
        GPIO.cleanup()

