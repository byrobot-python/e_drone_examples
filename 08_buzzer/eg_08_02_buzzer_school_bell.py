from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    
    drone.send_buzzer(DeviceType.DRONE, BuzzerMode.MUTE, BuzzerScale.MUTE.value, 100)
    sleep(0.2)
    
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.G4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.G4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.A4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.A4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.G4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.G4, 500);     sleep(0.5)
    drone.send_buzzer_scale(DeviceType.DRONE, BuzzerScale.E4, 500);     sleep(0.5)

    drone.close()