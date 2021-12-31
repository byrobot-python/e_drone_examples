import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    
    drone.send_display_clear_all(DisplayPixel(int(random.randint(0, 1))))
    sleep(0.1)

    for i in range(0, 100, 1):

        x1          = int(random.randint(0, 127))
        y1          = int(random.randint(0, 63))
        x2          = int(random.randint(0, 127))
        y2          = int(random.randint(0, 63))
        pixel       = DisplayPixel(int(random.randint(0, 1)))
        line        = DisplayLine(int(random.randint(0, 2)))

        data_array = drone.send_display_draw_line(x1, y1, x2, y2, pixel, line)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.02)
    
    drone.close()