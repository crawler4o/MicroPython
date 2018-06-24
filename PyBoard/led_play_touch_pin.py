### Led play, interrupted by touch pin ###

import pyb


red_led = pyb.LED(1)
green_led = pyb.LED(2)
orange_led = pyb.LED(3)
blue_led = pyb.LED(4)

# The callback function
def my_callback(*args):
    # print(args) # this was to find out what positional arguments the irg returns. It is (Pin(Pin.cpu.A2, mode=Pin.IN),)

    red_led.on()
    green_led.on()
    orange_led.on()
    blue_led.on()
    pyb.delay(300)
    red_led.off()
    green_led.off()
    orange_led.off()
    blue_led.off()
    pyb.delay(300)
    for x in range(3):
        red_led.on()
        pyb.delay(60)
        green_led.on()
        pyb.delay(60)
        orange_led.on()
        pyb.delay(60)
        blue_led.on()
        pyb.delay(60)
        red_led.off()
        green_led.off()
        orange_led.off()
        blue_led.off()
    sys.exit()

# The touch pin
pin_x1 = pyb.Pin('X1')
pin_x1.init(pin_x1.IN, pull=pin_x1.PULL_NONE, af=1)
#pin_x1.callback(my_callback)
pin_x1.irq(handler=my_callback, trigger=pin_x1.IRQ_RISING)

# The LED Play
intens = 0
while True:
    green_led.on()
    pyb.delay(250)
    if intens >= 255:
        red_led.on()
        pyb.delay(200)
        intens = 0
        orange_led.intensity(intens)
        red_led.off()
    else:
        intens += 20
        orange_led.intensity(intens)
        blue_led.on()
        pyb.delay(50)
        blue_led.off()
    pyb.delay(250)
    green_led.off()
    pyb.delay(250)
