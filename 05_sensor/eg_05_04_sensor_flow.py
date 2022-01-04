# flow 센서 데이터 확인
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_flow(flow):
    print("event_flow() / {0:0.1f}, {1:0.1f}, {2:0.1f}".format(flow.x, flow.y, flow.z))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.FLOW, event_flow)

    for i in range(100, 0, -1):
        # Range 정보 요청
        drone.send_request(DeviceType.DRONE, DataType.FLOW)
        sleep(0.1)

    drone.close()
