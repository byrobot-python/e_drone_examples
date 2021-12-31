import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    for i in range(0, 10, 1):
        
        r    = int(random.randint(0, 255))
        g    = int(random.randint(0, 255))
        b    = int(random.randint(0, 255))

        dataArray = drone.send_light_default_color(DeviceType.DRONE, LightModeDrone.BODY_DIMMING, 1, r, g, b)
        print("{0} / {1}".format(i, convert_byte_array_to_string(dataArray)))

        sleep(2)
    
    drone.close()