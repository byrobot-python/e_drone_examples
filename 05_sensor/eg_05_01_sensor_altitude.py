# 고도 데이터 확인
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_altitude(altitude):
    print("event_altitude()")
    print("-  Temperature: {0:.3f}".format(altitude.temperature))
    print("-     Pressure: {0:.3f}".format(altitude.pressure))
    print("-     Altitude: {0:.3f}".format(altitude.altitude))
    print("- Range Height: {0:.3f}".format(altitude.range_height))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ALTITUDE, event_altitude)

    # Altitude 정보 요청
    drone.send_request(DeviceType.DRONE, DataType.ALTITUDE)
    sleep(0.1)

    drone.close()
