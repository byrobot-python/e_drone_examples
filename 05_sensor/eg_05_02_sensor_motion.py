# Motion 센서 데이터 확인
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def event_motion(motion):
    print("event_motion()")
    print("- Accel: {0:5}, {1:5}, {2:5}".format(motion.accel_x, motion.accel_y, motion.accel_z))
    print("-  Gyro: {0:5}, {1:5}, {2:5}".format(motion.gyro_roll, motion.gyro_pitch, motion.gyro_yaw))
    print("- Angle: {0:5}, {1:5}, {2:5}".format(motion.angle_roll, motion.angle_pitch, motion.angle_yaw))


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.MOTION, event_motion)

    # Range 정보 요청
    drone.send_request(DeviceType.DRONE, DataType.MOTION)
    sleep(0.1)

    drone.close()
