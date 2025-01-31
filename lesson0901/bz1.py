from gpiozero import Button, Buzzer
from signal import pause

bz = Buzzer(17)
button = Button(18)

buzzer_on = False


def toggle_buzzer():
    global buzzer_on
    if buzzer_on:
        bz.off()
    else:

        bz.on()
        buzzer_on = not buzzer_on


button.when_pressed = toggle_buzzer


pause()
