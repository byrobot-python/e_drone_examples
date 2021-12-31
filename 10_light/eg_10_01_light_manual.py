import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.send_light_manual(DeviceType.CONTROLLER, 0xFF, 0)
    sleep(1)


    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000011, 10);     sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000011, 100);    sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000011, 0);      sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000110, 10);     sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000110, 100);    sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000110, 0);      sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000101, 10);     sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000101, 100);    sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, 0b00000101, 0);      sleep(1)

    drone.send_light_manual(DeviceType.DRONE, 0b00000110, 10);     sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00000110, 100);    sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00000110, 0);      sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001100, 10);     sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001100, 100);    sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001100, 0);      sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001010, 10);     sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001010, 100);    sleep(1)
    drone.send_light_manual(DeviceType.DRONE, 0b00001010, 0);      sleep(1)


    drone.close()