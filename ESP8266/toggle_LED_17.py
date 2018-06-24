from machine import Pin
import time
 
p = Pin(2, Pin.OUT)
for i in range(0,17):
    print("a1")
    time.sleep_ms(300)
    p.value(0)
    time.sleep_ms(300)
    p.value(1)