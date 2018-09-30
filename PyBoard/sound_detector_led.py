
inp = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)
blue_led = pyb.LED(4)

while True:
    if inp.value() == 1:
        blue_led.on()
    else:
        blue_led.off()

    pyb.delay(200)


