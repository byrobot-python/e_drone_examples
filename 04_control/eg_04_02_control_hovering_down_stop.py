# 이륙, 호버링, 하강, 정지 테스트
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    print("TakeOff")
    drone.send_takeoff()
    sleep(0.01)

    print("Hovering")
    drone.send_control_time(0, 0, 0, 0, 6400)
    sleep(0.01)

    print("Throttle down")
    drone.send_control_time(0, 0, 0, -25, 3600)
    sleep(0.01)

    print("Stop")
    drone.send_stop()
    sleep(0.01)


    drone.close()
