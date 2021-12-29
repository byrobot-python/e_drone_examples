# 자세 확인
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_attitude(attitude):
    print("event_attitude() / {0:0.1f}, {1:0.1f}, {2:0.1f}".format(attitude.roll, attitude.pitch, attitude.yaw))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ATTITUDE, event_attitude)

    # Range 정보 요청
    drone.send_request(DeviceType.DRONE, DataType.ATTITUDE)
    sleep(0.1)

    drone.close()
