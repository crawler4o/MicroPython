"""
The idea is to control the intensity of a LED with potentiometer.

"""
import pyb


blue_led = pyb.LED(4)

on_off_v = pyb.Pin('X1')
on_off_v.init(on_off_v.OUT_PP, pull=on_off_v.PULL_NONE, af=1)
on_off_v.value(1)

on_off_v_0 = pyb.Pin('X5')
on_off_v_0.init(on_off_v.OUT_PP, pull=on_off_v.PULL_NONE, af=1)
on_off_v.value(0)

collector = pyb.ADC('X3')

while True:
    pyb.delay(100)
    intens = collector.read()-3880
    blue_led.intensity(intens)

blue_led.off()

#collector.read()