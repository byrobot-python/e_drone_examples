
import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':
    
    drone = Drone()
    drone.open()

    header = Header()

    header.data_type = DataType.DISPLAY_DRAW_STRING
    header.length   = DisplayDrawString.get_size()
    header.from_    = DeviceType.BASE
    header.to_      = DeviceType.CONTROLLER

    data = DisplayDrawString()

    for i in range(0, 100, 1):

        data.x          = int(random.randint(0, 127))
        data.y          = int(random.randint(0, 63))
        data.font       = DisplayFont(int(random.randint(0, 1)))
        data.pixel      = DisplayPixel(int(random.randint(0, 1)))
        data.message    = "HELLO"
        
        header.length   = DisplayDrawString.get_size() + len(data.message)

        data_array = drone.transfer(header, data)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.03)
    
    drone.close()
    