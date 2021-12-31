import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    header = Header()

    header.data_type = DataType.DISPLAY_DRAW_STRING_ALIGN
    header.length    = DisplayDrawStringAlign.get_size()
    header.from_     = DeviceType.BASE
    header.to_       = DeviceType.CONTROLLER

    data = DisplayDrawStringAlign()

    for i in range(0, 100, 1):

        data.x_start    = 0
        data.x_end      = 127
        data.y          = int(random.randint(0, 63))
        data.align      = DisplayAlign(int(random.randint(0, 2)))
        data.font       = DisplayFont(int(random.randint(0, 1)))
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.message    = "LOVE"

        header.length   = DisplayDrawStringAlign.get_size() + len(data.message)

        data_array = drone.transfer(header, data)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.03)

    drone.close()