from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_state(state):
    print("{0}".format(state.headless))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.STATE, event_state)


    # 드론을 Headless 설정을 Headless 모드로 변경
    drone.send_headless(Headless.HEADLESS)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    # 드론을 Headless 설정을 Normal 모드로 변경
    drone.send_headless(Headless.NORMAL)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    drone.close()