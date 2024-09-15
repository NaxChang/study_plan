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

blinking_sequence = [(1, 0, 1, 0, 1), (0, 1, 0, 1, 0)]

while True:
    if leds_blinking:
        for pattern in blinking_sequence:
            leds.value = pattern
            sleep(1)
        leds.blink(on_time=1, off_time=1)
    else:
        leds.off()
        sleep(0.1)
pause()
