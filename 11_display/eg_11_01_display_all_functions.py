from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()

    delay = 0.5
    
    drone.send_display_clear_all(DisplayPixel.BLACK)
    sleep(delay)

    drone.send_display_clear(59, 27, 10, 10, DisplayPixel.WHITE)
    sleep(delay)

    drone.send_display_invert(54, 22, 20, 20)
    sleep(delay)

    drone.send_display_draw_point(64, 32, DisplayPixel.WHITE)
    sleep(delay)

    drone.send_display_draw_line(10, 10, 118, 54, DisplayPixel.WHITE, DisplayLine.DOTTED)
    sleep(delay)

    drone.send_display_draw_rect(44, 12, 40, 40, DisplayPixel.WHITE, False, DisplayLine.DASHED)
    sleep(delay)

    drone.send_display_draw_circle(64, 32, 20, DisplayPixel.WHITE, True)
    sleep(delay)
    
    drone.send_display_draw_string(10, 10, "HELLO", DisplayFont.LIBERATION_MONO_5X8, DisplayPixel.WHITE)
    sleep(delay)
    
    drone.send_display_draw_string_align(0, 128, 30, "E-DRONE", DisplayAlign.CENTER, DisplayFont.LIBERATION_MONO_10X16, DisplayPixel.WHITE)
    sleep(delay)
    
    drone.close()