# 조종기의 페어링 정보를 변경하고, 변경된 정보를 요청한 후 응답을 기다려 출력하는 예제
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    # 페어링 설정
    drone.send_pairing(DeviceType.CONTROLLER, 0x0001, 0x0002, 0x0003, 0x04, 0x05, 0x06, 0x07, 0x08)
    sleep(0.01)

    # 페어링데이터 요청
    drone.send_request(DeviceType.CONTROLLER, DataType.PAIRING)

    time_start = time.time()

    while True:
        sleep(0.01)
        dataType = drone.check()
        
        if dataType == DataType.PAIRING:
            pairing = drone.get_data(DataType.PAIRING)

            print("Address: 0x{0:04X}{1:04X}{2:04X} / {0}.{1}.{2}".format(
                pairing.address_0, 
                pairing.address_1, 
                pairing.address_2))

            print("Scramble: {0}".format(pairing.scramble))

            print("Channel: {0} / {1} / {2} / {3}".format(
                pairing.channel_0,
                pairing.channel_1,
                pairing.channel_2,
                pairing.channel_3))

            break

        if time.time() > time_start + 1:
            break

    drone.close()
