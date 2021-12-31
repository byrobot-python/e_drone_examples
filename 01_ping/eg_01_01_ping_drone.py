from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    drone.send_ping(DeviceType.DRONE)

    time_start = time.time()

    while True:
        sleep(0.01)
        data_type = drone.check()

        if data_type == DataType.ACK:
            ack = drone.get_data(DataType.ACK)
            print("{0} / {1} / {2:04X}".format(ack.data_type.name, ack.system_time, ack.crc16))
            print("T: {0}".format(time.time() - time_start))
            break

        # 1초 동안 응답이 없을 경우 응답 확인을 빠져나감
        if time.time() > time_start + 1:
            print("Time Over")
            break

    drone.close()
