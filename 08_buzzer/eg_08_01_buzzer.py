from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    

    drone.send_buzzer(BuzzerMode.MUTE, BuzzerScale.MUTE.value, 500)
    sleep(1)

    drone.send_buzzer(BuzzerMode.SCALE, BuzzerScale.C4.value, 500)
    sleep(1)

    drone.send_buzzer(BuzzerMode.HZ, 500, 500)
    sleep(1)


    drone.send_buzzer_mute(100)
    drone.send_buzzer_mute_reserve(100)
    sleep(1.2)


    drone.send_buzzer_scale(BuzzerScale.C5, 500)
    drone.send_buzzer_scale_reserve(BuzzerScale.D5, 500)
    sleep(1.2)


    drone.send_buzzer_hz(1000, 500)
    drone.send_buzzer_hz_reserve(1200, 500)
    sleep(1.2)
    

    drone.close()
