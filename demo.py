#!/usr/bin/python3

import Roomba

if __name__ == '__main__':

    roomba = Roomba(DD_pin = 17)

    roomba.wake_roomba()
    roomba.start()
    roomba.sensors()

    roomba.shutdown()

