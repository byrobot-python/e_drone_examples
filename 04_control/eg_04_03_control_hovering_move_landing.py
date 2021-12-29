# 이륙, 호버링, 전진, 착륙 테스트
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    print("TakeOff")
    drone.send_takeoff()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Hovering")
    drone.send_control_time(0, 0, 0, 0, 3600)
    for i in range(3, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Go Front 1 meter")
    drone.send_control_position_short(10, 0, 0, 5, 0, 0)
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)

    print("Landing")
    drone.send_landing()
    for i in range(5, 0, -1):
        print("{0}".format(i))
        sleep(1)


    drone.close()
