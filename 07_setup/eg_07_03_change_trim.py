from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_trim(trim):
    print("{0}, {1}, {2}, {3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.TRIM, event_trim)


    # 드론 비행 트림 설정 변경
    drone.send_trim(10, 20, 30, 40)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.TRIM)
    sleep(0.1)


    # 드론 비행 트림 설정 변경
    drone.send_trim(0, 0, 0, 0)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.TRIM)
    sleep(0.1)


    drone.close()