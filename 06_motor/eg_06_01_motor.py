from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_ack(ack):
    print("event_ack() / {0} / 0x{1:04X} / {2}".format(ack.data_type.name, ack.crc16, ack.system_time))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ACK, event_ack)
    sleep(0.01)


    drone.send_motor(100, 0, 0, 0)
    sleep(3)

    drone.send_motor(0, 100, 0, 0)
    sleep(3)
    
    drone.send_motor(0, 0, 100, 0)
    sleep(3)
    
    drone.send_motor(0, 0, 0, 100)
    sleep(3)

    drone.send_motor(0, 0, 0, 0)
    sleep(0.1)


    drone.close()
