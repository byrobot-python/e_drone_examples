from time import sleep

from e_drone.drone import *
from e_drone.protocol import *



def event_ack(ack):
    print("event_ack()")
    print("{0} / {1} / {2:04X}".format(ack.data_type.name, ack.system_time, ack.crc16))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ACK, event_ack)

    # Ping 전송
    drone.send_ping(DeviceType.CONTROLLER)
    
    sleep(0.1)

    drone.close()
