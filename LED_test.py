l1 = pyb.LED(1)
l2 = pyb.LED(2)
l3 = pyb.LED(3)
l4 = pyb.LED(4)

arr = [l1, l2, l3, l4]

while True:
    for x in arr:
        x.toggle()
        pyb.delay(200)
        x.toggle()
        pyb.delay(200)