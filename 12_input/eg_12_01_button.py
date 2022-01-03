from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def eventButton(button):
    print("eventButton() / " +
        "Button: 0b{0:16}, Event: {1:6}".format(bin(button.button)[2:].zfill(16), button.event.name))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.BUTTON, eventButton)

    drone.send_ping(DeviceType.CONTROLLER)

    for i in range(10, 0, -1):
        print(i)
        sleep(1)

    drone.close()
