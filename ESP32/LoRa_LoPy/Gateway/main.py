# This is a LoRa gateway script for SX1276 chip based on ESP32 WIFI increased OLED
# https://www.aliexpress.com/item/TTGO-868MHz-915MHz-SX1276-ESP32-LoRa-0-96-Inch-Blue-OLED-Display-Bluetooth-WIFI-Lora-Kit/32840258107.html?spm=a2g0s.9042311.0.0.7d3b4c4d507lRN

# Some useful links
# https://ifttt.com/
# https://pycom.io/support-community/support/video-tutorials/#
# https://www.thethingsnetwork.org/forum/t/single-channel-gateway-part-3/11546
# https://www.thethingsnetwork.org/

# esptool.py --chip esp32 --port COM9 write_flash -z 0x1000 esp32-20181114-v1.9.4-683-gd94aa577a.bin
# esptool.py --chip esp32 erase_flash

# import webrepl_setup  # to activate the webrepl

import network

# Connecting to the home wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# sta_if.scan()                           # Scan for available access points
sta_if.connect("Amidophen", "x18abe4rz")  # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

