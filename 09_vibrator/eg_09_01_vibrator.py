
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    drone.send_vibrator(100, 200, 1200)
    sleep(1)

    drone.close()