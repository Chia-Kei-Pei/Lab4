from time import sleep
from hal import hal_input_switch as switch
from hal import hal_led as led


def main():
    # initialisation
    switch.init()
    led.init()
    countdown = 0  # Value is in seconds.
    # positive value == counting down, zero == idle, negative value == primed to start countdown
    # I used to make this kind of variable in minecraft

    # logic
    while 1:
        if switch.read_slide_switch() == 1:  # left
            led_blink(5)
            countdown = -1
        elif switch.read_slide_switch() == 0:  # right
            if countdown < 0:  # set the countdown timer!
                countdown = 5
            if countdown > 5:  # counting down from <countdown> seconds
                led_blink(10)
                countdown = countdown - 1/10


def led_blink(freq_in_Hz):
    delay = (1 / freq_in_Hz) / 2  # the divide-by-two is duration LED stays ON, and duration it stays OFF
    led.set_output(0, 1)
    sleep(delay)
    led.set_output(0, 0)
    sleep(delay)


# Main entry point
if __name__ == "__main__":
    main()
