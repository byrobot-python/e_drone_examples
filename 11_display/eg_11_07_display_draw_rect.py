import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    for i in range(0, 100, 1):

        width      = int(random.randint(0, 127))
        height     = int(random.randint(0, 63))
        x          = int(random.randint(0, 127) - width / 2)
        y          = int(random.randint(0, 63) - height / 2)
        pixel      = DisplayPixel(int(random.randint(0, 1)))
        flag_fill  = bool(random.randint(0, 1))
        line       = DisplayLine(int(random.randint(0, 2)))

        data_array = drone.send_display_draw_rect(x, y, width, height, pixel, flag_fill, line)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.03)
    
    drone.close()