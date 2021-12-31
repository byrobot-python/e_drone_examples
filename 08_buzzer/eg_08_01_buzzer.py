from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    

    drone.send_buzzer(DeviceType.DRONE, BuzzerMode.MUTE, BuzzerScale.MUTE.value, 500)
    sleep(1)

    drone.send_buzzer(DeviceType.DRONE, BuzzerMode.SCALE, BuzzerScale.C4.value, 500)
    sleep(1)

    drone.send_buzzer(DeviceType.DRONE, BuzzerMode.HZ, 500, 500)
    sleep(1)


    drone.send_buzzer_mute(DeviceType.CONTROLLER, 100)
    drone.send_buzzer_mute_reserve(DeviceType.CONTROLLER, 100)
    sleep(1.2)


    drone.send_buzzer_scale(DeviceType.CONTROLLER, BuzzerScale.C5, 500)
    drone.send_buzzer_scale_reserve(DeviceType.CONTROLLER, BuzzerScale.D5, 500)
    sleep(1.2)


    drone.send_buzzer_hz(DeviceType.CONTROLLER, 1000, 500)
    drone.send_buzzer_hz_reserve(DeviceType.CONTROLLER, 1200, 500)
    sleep(1.2)
    

    drone.close()
