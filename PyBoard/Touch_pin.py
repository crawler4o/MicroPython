### Touch Pin ###

pin_x1 = pyb.Pin('X1')
pin_x1.init(pin_x1.IN, pull=pin_x1.PULL_NONE, af=1)

# pin_x1.value() # To check the value in shell
