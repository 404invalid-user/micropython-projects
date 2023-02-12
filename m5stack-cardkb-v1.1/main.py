# M5Stack CardKB tiny keyboard - scruss, 2021-06
# MicroPython - Raspberry Pi Pico
 
from machine import Pin, I2C
from time import sleep_ms
 
i2c = I2C(1, scl=Pin(7), sda=Pin(6))
cardkb = i2c.scan()[0]  # should return 95
if cardkb != 95:
    print("!!! Check I2C config: " + str(i2c))
    print("!!! CardKB not found. I2C device", cardkb,
          "found instead.")
    exit(1)
 
ESC = chr(27)
NUL = '\x00'
CR = "\r"
LF = "\n"

arrow_up = b'\xb5'
arrow_right = b'\xb7'
arrow_down= b'\xb6'
arrow_left = b'\xb4'

c = ''
 
print("*** APPALLING TYPEWRITER ***")
print("** Type stuff, Esc to end **")
 
while (c != ESC):
    # returns NUL char if no character read
    
    rkey = i2c.readfrom(cardkb, 1)
    try:
        c = rkey.decode()
    except:
        if rkey == arrow_up:
            c = "ARROW_UP"
        elif rkey == arrow_down:
            c = "ARROW_DOWN"
        elif rkey == arrow_left:
            c = "ARROW_LEFT"
        elif rkey == arrow_right:
            c = "ARROW_RIGHT"
        else:
            print("An exception occurred")
    
    if c == CR:
        # convert CR return key to LF
        c = LF
    if c != NUL or c != ESC:
        print(c, end='')
        
    sleep_ms(50)
