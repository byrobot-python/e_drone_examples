# 조종기의 펌웨어 정보를 요청하고, 이벤트 핸들러를 통해 응답을 출력하는 예제
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_information(information):
    print("event_information()")
    print("ModeUpdate: {0}".format(information.mode_update))
    print("ModelNumber: {0}".format(information.model_number))
    print("Version: {0}.{1}.{2} / {3} / 0x{3:08X}".format(
        information.version.major,
        information.version.minor,
        information.version.build,
        information.version.v))
    print("Release Date: {0}.{1}.{2}".format(
        information.year,
        information.month,
        information.day))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.INFORMATION, event_information)

    # Information 정보 요청
    drone.send_request(DeviceType.DRONE, DataType.INFORMATION)
    sleep(0.1)

    drone.close()
