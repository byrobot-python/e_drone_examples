from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    print("BODY_HOLD - Turn off")
    drone.send_light_mode_color(DeviceType.DRONE, LightModeDrone.BODY_HOLD, 255, 0, 0, 0)
    drone.send_light_mode_color(DeviceType.CONTROLLER, LightModeController.BODY_HOLD, 255, 0, 0, 0)
    sleep(2)

    print("BODY_HOLD - Yellow")
    drone.send_light_mode_color(DeviceType.DRONE, LightModeDrone.BODY_HOLD, 255, 200, 200, 0)
    drone.send_light_mode_color(DeviceType.CONTROLLER, LightModeController.BODY_HOLD, 200, 200, 200, 0)
    sleep(2)


    # send_light_event_color*
    print("BODY_DIMMING 3 - White")
    drone.send_light_event_color(DeviceType.DRONE, LightModeDrone.BODY_DIMMING, 3, 3, 200, 200, 200)
    drone.send_light_event_color(DeviceType.CONTROLLER, LightModeController.BODY_DIMMING, 3, 3, 200, 200, 200)
    sleep(3)

    # send_light_event_colors*
    print("BODY_DIMMING 4 - Cyan")
    drone.send_light_event_colors(DeviceType.DRONE, LightModeDrone.BODY_DIMMING, 3, 3, Colors.CYAN)
    drone.send_light_event_colors(DeviceType.CONTROLLER, LightModeController.BODY_DIMMING, 3, 3, Colors.CYAN)
    sleep(3)


    #send_light_mode_color
    print("BODY_DIMMING 1 - Magenta")
    drone.send_light_mode_color(DeviceType.DRONE, LightModeDrone.BODY_DIMMING, 3, 200, 0, 200)
    drone.send_light_mode_color(DeviceType.CONTROLLER, LightModeController.BODY_DIMMING, 3, 200, 0, 200)
    sleep(3)

    #send_light_mode_colors
    print("BODY_DIMMING 2 - GreenYellow")
    drone.send_light_mode_colors(DeviceType.DRONE, LightModeDrone.BODY_DIMMING, 3, Colors.GREENYELLOW)
    drone.send_light_mode_colors(DeviceType.CONTROLLER, LightModeController.BODY_DIMMING, 3, Colors.GREENYELLOW)
    sleep(3)


    drone.close()