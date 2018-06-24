### LED play ###
import pyb

red_led = pyb.LED(1)
green_led = pyb.LED(2)
orange_led = pyb.LED(3)
blue_led = pyb.LED(4)

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
