# MotorSingle 동작 테스트
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_ack(ack):
    print("event_ack()")
    print("-   DataType: {0}".format(ack.data_type.name))
    print("-      CRC16: 0x{0:04X}".format(ack.crc16))
    print("- SystemTime: {0}".format(ack.system_time))


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ACK, event_ack)
    sleep(0.01)


    drone.send_motor_single(0, 200)
    sleep(2)

    drone.send_motor_single(0, 0)
    sleep(1)

    drone.send_motor_single(1, 200)
    sleep(2)

    drone.send_motor_single(1, 0)
    sleep(1)

    drone.send_motor_single(2, 200)
    sleep(2)

    drone.send_motor_single(2, 0)
    sleep(1)

    drone.send_motor_single(3, 200)
    sleep(2)

    drone.send_motor_single(3, 0)
    sleep(1)


    drone.close()
