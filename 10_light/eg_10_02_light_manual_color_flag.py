import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.send_light_manual(DeviceType.CONTROLLER, 0xFF, 0)
    sleep(1)


    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_RED.value, 10);        sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_RED.value, 100);       sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_RED.value, 0);         sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_GREEN.value, 10);      sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_GREEN.value, 100);     sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_GREEN.value, 0);       sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_BLUE.value, 10);       sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_BLUE.value, 100);      sleep(1)
    drone.send_light_manual(DeviceType.CONTROLLER, LightFlagsController.BODY_BLUE.value, 0);        sleep(1)


    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_RED.value, 10);        sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_RED.value, 100);       sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_RED.value, 0);         sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_GREEN.value, 10);      sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_GREEN.value, 100);     sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_GREEN.value, 0);       sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_BLUE.value, 10);       sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_BLUE.value, 100);      sleep(1)
    drone.send_light_manual(DeviceType.DRONE, LightFlagsDrone.BODY_BLUE.value, 0);        sleep(1)


    drone.close()