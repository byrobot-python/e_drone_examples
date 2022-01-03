from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_joystick(joystick):
    print("event_joystick() / " +
        "L: ({0:4}, {1:4}), {2:5}, {3:5} / ".format(joystick.left.x, joystick.left.y, joystick.left.direction.name, joystick.left.event.name) +
        "R: ({0:4}, {1:4}), {2:5}, {3:5}".format(joystick.right.x, joystick.right.y, joystick.right.direction.name, joystick.right.event.name))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.JOYSTICK, event_joystick)

    drone.send_ping(DeviceType.CONTROLLER)

    for i in range(10, 0, -1):
        print(i)
        sleep(1)

    drone.close()
