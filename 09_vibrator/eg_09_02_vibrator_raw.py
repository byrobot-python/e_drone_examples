from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    header = Header()
    
    header.data_type = DataType.VIBRATOR
    header.length    = Vibrator.get_size()
    header.from_     = DeviceType.BASE
    header.to_       = DeviceType.CONTROLLER

    data = Vibrator()

    data.mode        = VibratorMode.INSTANTLY
    data.on          = 100
    data.off         = 200
    data.total       = 1200

    drone.transfer(header, data)
    sleep(1)


    drone.close()