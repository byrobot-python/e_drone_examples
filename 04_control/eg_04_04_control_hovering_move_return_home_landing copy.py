# 이륙, 호버링, 1미터 전진, 1미터 오른쪽 이동, 리턴 홈 테스트
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def wait(message, time):
    print("{0} / ".format(message), end="")
    for i in range(time, 0, -1):
        print("{0} ".format(i), end="")
        sleep(1)
    print("")


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.send_takeoff()
    wait("TakeOff", 5)

    drone.send_control(0, 0, 0, 0)
    wait("Hovering", 3)

    drone.send_control_position(1.0, 0, 0, 0.5, 0, 0)
    wait("Go Front 1 meter", 5)

    drone.send_control_position(0, -1.0, 0, 0.5, 0, 0)
    wait("Go Right 1 meter", 5)

    drone.send_flight_event(FlightEvent.RETURN_HOME)
    wait("Return Home", 5)

    drone.send_landing()
    wait("Landing", 5)


    drone.close()
