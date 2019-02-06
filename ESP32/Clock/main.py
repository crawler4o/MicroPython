# import webrepl_setup  # to activate the webrepl


### >>> import wave
### >>> from pyb import DAC
### >>> dac = DAC(1)
### >>> f = wave.open('test.wav')
### >>> dac.write_timed(f.readframes(f.getnframes()), f.getframerate())

### clock_IP___192.168.10.124:8266/

import network
import machine
import time
import utime
import random
from ntptime import settime


def wlan_connect(ssid='Amidophen', password='x18abe4rz'):
    global wlan
    wlan = network.WLAN(network.STA_IF)

    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to: ', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('network config:', wlan.ifconfig())


def play_sound(times):
    def chime():
        for t in range(10000):
            dac_a.write(int(t*((15 & t >> 11) % 12) & 55-(t >> 5 | t >> 12) | t*(t >> 10)*32) & 255)

    dac_pin = machine.Pin(25)
    dac_a = machine.DAC(dac_pin)
    for _ in range(times):
        chime()
        time.sleep(0.5)


def clock_run():

    while True:
        if utime.localtime()[4] == 59:
            time.sleep(1)
            continue
        elif not utime.localtime()[4]:
            play_sound(utime.localtime()[3]+2)  # here the dst should be changed manually

        time.sleep(60)


if __name__ == '__main__':
    wlan_connect()
    settime()
    play_sound(3)
    clock_run()
