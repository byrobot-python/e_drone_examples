import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    for i in range(0, 10, 1):
        
        colors = Colors(random.randint(0, Colors.END_OF_TYPE.value))

        data_array = drone.send_light_mode_colors(DeviceType.CONTROLLER, LightModeController.BODY_DIMMING, 1, colors)
        print("{0} / {1}".format(i, convert_byte_array_to_string(data_array)))

        sleep(0.6)
    
    drone.close()