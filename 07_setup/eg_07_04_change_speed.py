from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_state(state):
    print("Speed: {0}".format(state.control_speed))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.STATE, event_state)


    # 제어 속도를 1로 변경(1, 2, 3 중에 선택)
    drone.send_command(DeviceType.DRONE, CommandType.CONTROL_SPEED, 1)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    # 제어 속도를 2로 변경(1, 2, 3 중에 선택)
    drone.send_command(DeviceType.DRONE, CommandType.CONTROL_SPEED, 2)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    # 제어 속도를 3으로 변경(1, 2, 3 중에 선택)
    drone.send_command(DeviceType.DRONE, CommandType.CONTROL_SPEED, 3)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    drone.close()
