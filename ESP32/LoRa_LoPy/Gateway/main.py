# This is a LoRa gateway script for SX1276 chip based on ESP32 WIFI increased OLED
# https://www.aliexpress.com/item/TTGO-868MHz-915MHz-SX1276-ESP32-LoRa-0-96-Inch-Blue-OLED-Display-Bluetooth-WIFI-Lora-Kit/32840258107.html?spm=a2g0s.9042311.0.0.7d3b4c4d507lRN

# Some useful links
# https://ifttt.com/
# https://pycom.io/support-community/support/video-tutorials/#
# https://www.thethingsnetwork.org/forum/t/single-channel-gateway-part-3/11546
# https://www.thethingsnetwork.org/
# https://lemariva.com/blog/2018/10/micropython-esp32-sending-data-using-lora

# And some useful commands
# esptool.py --chip esp32 --port COM9 write_flash -z 0x1000 esp32-20181114-v1.9.4-683-gd94aa577a.bin
# esptool.py --chip esp32 erase_flash

# import webrepl_setup  # to activate the webrepl

import os
import network


def wlan_connect(ssid='Amidophen', password='x18abe4rz'):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to: ', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


if __name__ == '__main__':
    wlan_connect()
