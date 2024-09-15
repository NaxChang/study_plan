from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26)
button = Button(18)

leds_blinking = False


def toggle_leds():
    global leds_blinking
    leds_blinking = not leds_blinking


button.when_pressed = toggle_leds


while True:
    if leds_blinking:
        leds.value = (1, 0, 1, 0, 1)
        sleep(1)
        leds.value = (0, 1, 0, 1, 0)
        sleep(1)
        leds.on()
        sleep(1)
        leds.off()
        sleep(1)
    else:
        leds.off()
        sleep(0.1)

pause()
