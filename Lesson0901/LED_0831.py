from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26)

while True:
    leds.value = (1, 0, 1, 0, 1)
    sleep(1)
    leds.value = (0, 1, 0, 1, 0)
    sleep(1)
    leds.on()
    sleep(1)
    leds.off()
    sleep(1)

pause()
