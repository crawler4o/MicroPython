import os
import machine
import random
import time

# os.listdir()

p = machine.Pin(25)
a = machine.DAC(p)
t = 0

q = machine.Pin(32)
b = machine.ADC(q)


while True:
	reading = b.read()
	print(reading)
	if reading < 256:
		a.write(reading)
	else:
		a.write(reading % 255)


while True:
    b.read()
	time.sleep(0.5)
	
	
while True:
    a.write(random.randint(0, 255))

	
while True:
    a.write(int(t**((t>>9|t>>13)&25&t>>6)) % 256)
    t += 1

	
while True:
	sound = int(t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32) & 255
	print(sound)
	a.write(sound) 
	t += 1
	
	
while True:
    a.write(int(t*((t>>9|t>>13)&25&t>>6)) % 10)
    t += 1


while True:
    a.write(int(t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32) & 15 ) 
    t += 1	
	
	
while True:
    a.write(random.randint(0,2))


while True:
    print(int(t*((t>>9|t>>13)&25&t>>6)) % 255)
    t += 1


