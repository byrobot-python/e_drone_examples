from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    header = Header()
    
    header.data_type = DataType.BUZZER
    header.length    = Buzzer.get_size()
    header.from_     = DeviceType.BASE
    header.to_       = DeviceType.CONTROLLER


    data = Buzzer()

    data.mode       = BuzzerMode.SCALE
    data.value      = BuzzerScale.C5.value
    data.time       = 500

    drone.transfer(header, data)
    sleep(1)


    data.mode       = BuzzerMode.HZ
    data.value      = 1200
    data.time       = 500

    drone.transfer(header, data)
    sleep(1)


    drone.close()