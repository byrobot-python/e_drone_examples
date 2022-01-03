
# 드론 센서 캘리브레이션 요청 후 에러로 나타난 캘리브레이션 진행 상태를 화면에 표시
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def check_error(error, flag):
    if error & flag.value != 0:
        return True
    else:
        return False

def event_error(error):
    
    print("* eventError() / SystemTime({0:10}) / ErrorFlagsForSensor({1:032b}) / ErrorFlagsForState({2:032b})".format(error.system_time, error.error_flags_for_sensor, error.error_flags_for_state))

    if check_error(error.error_flags_for_sensor, ErrorFlagsForSensor.MOTION_CALIBRATING):
        print("    - The Motion Sensor is being calibrated.")


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 이벤트 핸들링 함수 등록
    drone.set_event_handler(DataType.ERROR, event_error)

    drone.send_ping(DeviceType.CONTROLLER)
    sleep(0.1)

    drone.send_command(DeviceType.DRONE, CommandType.CLEAR_BIAS)
    sleep(0.1)

    for i in range(30, 0, -1):
        print(i)
        sleep(1)

        error = drone.get_data(DataType.ERROR)
        if error and not check_error(error.error_flags_for_sensor, ErrorFlagsForSensor.MOTION_CALIBRATING):
            print("* The Motion Sensor Calibration is completed.")
            break

    drone.close()