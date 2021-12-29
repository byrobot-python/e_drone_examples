from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_state(state):
    print("{0}".format(state.mode_control_flight))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.STATE, event_state)


    # 비행 제어 모드를 ModeControlFlight.POSITION 으로 변경
    drone.send_mode_control_flight(ModeControlFlight.POSITION)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    # 비행 제어 모드를 ModeControlFlight.Attitude 으로 변경
    drone.send_mode_control_flight(ModeControlFlight.ATTITUDE)
    sleep(0.01)

    # 변경 사항을 확인
    drone.send_request(DeviceType.DRONE, DataType.STATE)
    sleep(0.1)


    drone.close()
