import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone(True, False, False, True, True)
    drone.open()

    for i in range(0, 100, 1):

        x          = int(random.randint(0, 127))
        y          = int(random.randint(0, 63))
        radius     = int(random.randint(0, 63))
        pixel      = DisplayPixel(int(random.randint(0, 1)))
        flag_fill  = bool(random.randint(0, 1))

        drone.send_display_draw_circle(x, y, radius, pixel, flag_fill)
        sleep(0.05)

    drone.close()