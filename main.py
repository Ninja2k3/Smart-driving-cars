#keyboard,pyserial

import keyboard,serial
car=serial.Serial("com5",9600)
while True:
    if keyboard.is_pressed("w"):
        car.write(b'f')
    elif keyboard.is_pressed("s"):
        car.write(b'b')
    elif keyboard.is_pressed("a"):
        car.write(b'r')
    elif keyboard.is_pressed("d"):
        car.write(b'l')
    else:
        car.write(b's')

    if keyboard.is_pressed("q"):
        exit()