#!/usr/bin/python3

import Roomba

if __name__ == '__main__':

    roomba = Roomba.Roomba(DD_pin = 17)
#    sensors = []

    roomba.wake_roomba()
    roomba.start()

    roomba.control()
    roomba.spot()
#    roomba.power_down()

#    sensors = roomba.sensors()

#    print(sensors)

    roomba.shutdown()

