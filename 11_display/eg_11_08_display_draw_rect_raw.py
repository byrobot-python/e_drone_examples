import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    header = Header()
    
    header.data_type = DataType.DISPLAY_DRAW_RECT
    header.length    = DisplayDrawRect.get_size()
    header.from_     = DeviceType.BASE
    header.to_       = DeviceType.CONTROLLER

    data = DisplayDrawRect()

    for i in range(0, 100, 1):

        data.width      = int(random.randint(0, 127))
        data.height     = int(random.randint(0, 63))
        data.x          = int(random.randint(0, 127) - data.width / 2)
        data.y          = int(random.randint(0, 63) - data.height / 2)
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.flag_fill  = bool(random.randint(0, 1))
        data.line       = DisplayLine(int(random.randint(0, 2)))

        data_array = drone.transfer(header, data)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.03)
    
    drone.close()
    