from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    drone.send_request(DeviceType.DRONE, DataType.INFORMATION)

    time_start = time.time()

    while True:
        sleep(0.01)
        dataType = drone.check()
        
        if dataType == DataType.INFORMATION:
            information = drone.get_data(DataType.INFORMATION)
            print("ModeUpdate: {0}".format(information.mode_update))
            print("ModelNumber: {0}".format(information.model_number))
            print("Version: {0}.{1}.{2} / {3} / 0x{3:08X}".format(
                information.version.major,
                information.version.minor,
                information.version.build,
                information.version.v))
            print("Release Date: {0}.{1}.{2}".format(
                information.year,
                information.month,
                information.day))
            break

        if time.time() > time_start + 1:
            break

    drone.close()
